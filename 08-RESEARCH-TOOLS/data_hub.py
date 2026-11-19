"""Public pharmaceutical research data connectors for PHARMAINTELLIGENCE.

Examples (run from repository root):
  py 08-RESEARCH-TOOLS/data_hub.py openfda-events aspirin --limit 5
  py 08-RESEARCH-TOOLS/data_hub.py openfda-label paracetamol --limit 5
  py 08-RESEARCH-TOOLS/data_hub.py pubchem aspirin
  py 08-RESEARCH-TOOLS/data_hub.py rxnorm metformin

Uses Python standard library only. Saves JSON plus provenance metadata.
Never use for patient-care decisions or to replace authoritative local labeling.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "research_cache"
USER_AGENT = "PHARMAINTELLIGENCE-educational-research/1.0 (public-data-learning)"

def safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip()).strip("._")
    return (cleaned or "query")[:80]

def fetch_json(url: str, timeout: int = 20) -> dict:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(request, timeout=timeout) as response:
            if response.status != 200:
                raise RuntimeError(f"Source returned HTTP {response.status}")
            payload = json.loads(response.read().decode("utf-8"))
            if not isinstance(payload, dict):
                raise RuntimeError("Unexpected response: expected a JSON object")
            return payload
    except HTTPError as exc:
        detail = exc.read(500).decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network/source error: {exc.reason}") from exc
    except TimeoutError as exc:
        raise RuntimeError("Request timed out; retry later.") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError("Source returned invalid JSON.") from exc

def build_request(source: str, term: str, limit: int = 10) -> tuple[str, str]:
    if not term.strip():
        raise ValueError("Search term cannot be empty.")
    if not 1 <= limit <= 100:
        raise ValueError("Limit must be between 1 and 100.")
    key = os.getenv("OPENFDA_API_KEY", "").strip()
    if source == "openfda-events":
        params = {"search": f'patient.drug.medicinalproduct:"{term.strip()}"', "limit": limit}
        if key:
            params["api_key"] = key
        return "https://api.fda.gov/drug/event.json?" + urlencode(params), "openFDA Drug Adverse Event (FAERS) API"
    if source == "openfda-label":
        params = {"search": f'openfda.generic_name:"{term.strip()}"', "limit": limit}
        if key:
            params["api_key"] = key
        return "https://api.fda.gov/drug/label.json?" + urlencode(params), "openFDA Drug Product Labeling API"
    if source == "pubchem":
        name = quote(term.strip(), safe="")
        properties = "MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES,InChIKey"
        return f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/{properties}/JSON", "PubChem PUG REST"
    if source == "rxnorm":
        params = {"term": term.strip(), "maxEntries": limit}
        return "https://rxnav.nlm.nih.gov/REST/approximateTerm.json?" + urlencode(params), "NLM RxNorm/RxNav approximate term API"
    raise ValueError(f"Unknown source: {source}")

def save_result(source: str, term: str, url: str, source_name: str, payload: dict, outdir: Path = DEFAULT_OUT) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{source}_{safe_filename(term)}_{stamp}"
    record = {
        "metadata": {
            "source": source_name,
            "source_url": url,
            "query": term,
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "purpose": "educational research and data-literacy practice",
            "limitations": [
                "Public source data may be incomplete, delayed, duplicated or jurisdiction-specific.",
                "A search match is not confirmation of product identity, clinical equivalence, safety or efficacy.",
                "Review source documentation, field definitions, licensing and intended-use limitations."
            ]
        },
        "data": payload
    }
    path = outdir / f"{stem}.json"
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    return path

def run_query(source: str, term: str, limit: int = 10, outdir: Path = DEFAULT_OUT) -> Path:
    url, source_name = build_request(source, term, limit)
    payload = fetch_json(url)
    return save_result(source, term, url, source_name, payload, outdir)

def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch public pharmaceutical research data and save provenance.")
    parser.add_argument("source", choices=["openfda-events", "openfda-label", "pubchem", "rxnorm"])
    parser.add_argument("term", help="Generic/brand name or compound name")
    parser.add_argument("--limit", type=int, default=10, help="Maximum records for APIs that support limits (1-100)")
    parser.add_argument("--outdir", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    try:
        path = run_query(args.source, args.term, args.limit, args.outdir)
    except (ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Saved research response: {path}")
    print("Review metadata and source limitations before analysis.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
