# Drug discovery and R&D lifecycle

## 1. From biological question to a candidate

1. **Disease biology and unmet need:** define the biological problem and intended patient/clinical context.
2. **Target identification:** propose a molecular target or biological mechanism supported by evidence.
3. **Target validation:** test whether changing the target produces the expected biological effect, while examining alternative explanations.
4. **Assay development:** establish fit-for-purpose biochemical, cellular or phenotypic assays with controls and reproducibility checks.
5. **Screening and hit confirmation:** identify signals, remove artifacts and confirm activity in independent assays.
6. **Hit-to-lead:** improve potency/selectivity and understand early liabilities.
7. **Lead optimization:** integrate medicinal chemistry, structure–activity relationships (SAR), ADME/DMPK, safety and developability.
8. **Candidate selection:** document the evidence and uncertainties supporting progression.
9. **Preclinical development:** generate relevant pharmacology, pharmacokinetic and toxicology evidence under applicable standards.
10. **Clinical development:** staged human studies, regulatory interactions and continuing evidence generation.
11. **Review and post-market lifecycle:** regulatory assessment, safety monitoring, quality changes and new evidence.

FDA's public overview presents discovery/development, preclinical research, clinical research, review and post-market safety monitoring as major steps. Actual paths vary by product class, indication and jurisdiction.

## 2. Medicinal chemistry and developability literacy

Study:
- Functional groups, ionization, pKa, lipophilicity and solubility.
- Molecular weight, polar surface area, hydrogen-bond donors/acceptors and rotatable bonds.
- Stereochemistry, tautomerism, salts, polymorphs and solid-state properties.
- Structure–activity relationships and selectivity.
- Chemical stability, permeability, metabolic stability and formulation implications.

Descriptors and heuristic filters are summaries, not universal rules for whether a molecule is drug-like or safe.

## 3. ADME, DMPK and safety

Understand the questions behind:
- Absorption, distribution, metabolism and excretion.
- Bioavailability, clearance, half-life, exposure and variability.
- In vitro and in vivo model limitations.
- Drug–drug interaction potential and metabolite characterization.
- Safety pharmacology, genotoxicity and toxicology study concepts.

Do not interpret one ADME result or computational prediction as proof of human exposure or safety.

## 4. Preclinical and clinical development literacy

Preclinical evidence supports decisions about whether and how to begin human research; it does not prove clinical benefit. Clinical development commonly includes:
- Phase 1: initial human safety/tolerability, PK and dose-related learning (designs differ).
- Phase 2: preliminary efficacy and dose/regimen exploration in the target population.
- Phase 3: confirmatory evidence of benefit and risk in larger populations where appropriate.
- Regulatory review, followed by post-market monitoring and additional studies as required.

Learn trial protocol structure, eligibility criteria, endpoints, randomization, blinding, comparators, sample size concepts, missing data, statistical analysis plans and safety reporting. Do not equate statistical significance with clinical importance.

## 5. Computational discovery and AI

A reproducible computational workflow may include:
1. Define a testable question before collecting data.
2. Record database, release/date, identifiers, license and inclusion criteria.
3. Resolve compound identifiers and stereochemistry; preserve salts/mixtures and source records.
4. Inspect assay metadata, units, endpoints, species, cell line, confidence and duplicates.
5. Calculate molecular descriptors with a versioned toolkit such as RDKit.
6. Use similarity, clustering or QSAR only with suitable labels and validation.
7. Split data to avoid analog-series leakage; use scaffold/time-aware validation where justified.
8. Report applicability domain, uncertainty, calibration and baseline comparisons.
9. Treat docking and model scores as prioritization hypotheses requiring experimental confirmation.

Public sources to learn: PubChem (https://pubchem.ncbi.nlm.nih.gov/), ChEMBL (https://www.ebi.ac.uk/chembl/), PubMed (https://pubmed.ncbi.nlm.nih.gov/), ClinicalTrials.gov (https://clinicaltrials.gov/) and RDKit documentation (https://www.rdkit.org/docs/).

## 6. Research quality and ethics

- Distinguish target evidence, association, mechanism and causality.
- Record negative results and failed experiments where available.
- Do not overfit, cherry-pick endpoints or silently remove inconvenient records.
- Respect database licenses, publication rights and data-use terms.
- Never present a predicted molecule as a medicine, therapy or validated candidate.
- Do not attempt synthesis, animal work or human experimentation outside approved, qualified institutions and oversight.
