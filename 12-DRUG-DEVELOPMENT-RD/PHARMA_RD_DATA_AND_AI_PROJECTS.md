# Data and AI projects for pharmaceutical manufacturing and R&D

This guide connects the new specialization to the existing Python, SQL, Power BI, ML and generative-AI tracks.

## Portfolio ladder

| Project | Pharmaceutical question | Skills | Evidence artifact |
|---|---|---|---|
| Manufacturing Process Map | Which steps and records exist for a dosage-form process? | Domain modeling, diagrams, documentation | Process map and data dictionary |
| QbD Risk Register | Which documented material/process factors could affect quality attributes? | Python, CSV validation, structured risk review | Versioned risk register with rationale |
| Development Batch Explorer | How do synthetic development observations vary by formulation/version and stage? | Python, pandas later, visualization, tests | Descriptive batch-trend report |
| Stability Trend Explorer | How do assay/degradation/dissolution observations evolve across timepoints and conditions? | SQL, BI, time-series visualization | Synthetic stability case study |
| Deviation/CAPA Analytics | What themes and recurrence patterns appear in approved, de-identified records? | SQL, Pareto analysis, text categorization | Non-causal trend dashboard |
| Material Supplier Quality | How do incoming material lots and test outcomes vary by supplier/material? | Data quality, SQL, BI | Supplier/material review dashboard |
| Discovery Evidence Mapper | What evidence supports a target or compound hypothesis? | Literature search, data provenance, critical appraisal | Citation-linked evidence matrix |
| Cheminformatics Notebook | How do public compound descriptors and assay labels behave? | Python, RDKit, statistics | Reproducible exploratory notebook |
| QSAR Baseline | Can a transparent baseline predict a defined public assay endpoint within a stated applicability domain? | ML, scaffold-aware splits, calibration | Baseline model card and error analysis |
| CMC Knowledge Assistant | Can an assistant retrieve the correct approved development/quality passages? | RAG, citations, evaluation | Source-grounded answer set with abstention |

## Data sources and provenance

Prefer public resources with clearly stated terms:
- PubChem: chemical substance/compound records and identifiers.
- ChEMBL: curated bioactivity and drug-discovery data.
- PubMed: biomedical literature discovery; full-text access and reuse vary.
- ClinicalTrials.gov: registered study records; registration is not proof of study quality or results.
- Official ICH/WHO/FDA/EMA guidelines for quality and development context.

For every dataset record: source URL, retrieval date, release/version where available, license/terms, inclusion criteria, unit definitions, missingness, deduplication rules and transformations. Preserve original identifiers.

## AI/ML safeguards

- Use time-, scaffold- or group-aware splitting when relevant; random splitting can overstate performance.
- Prevent data leakage across repeated compounds, batches, sites or study arms.
- Compare with a simple baseline and report subgroup errors.
- Do not mix assay endpoints, species, units or test systems without justification.
- Explain model applicability domain and uncertainty.
- Treat model outputs as research hypotheses, not experimental confirmation, clinical recommendations or manufacturing control limits.

## Boundaries for manufacturing data

Do not place proprietary batch records, deviations, formulations, process parameters, validation reports or site-identifying data in a public repository. Use synthetic examples or data explicitly approved for release. Never create or modify official GMP records with an unvalidated script.
