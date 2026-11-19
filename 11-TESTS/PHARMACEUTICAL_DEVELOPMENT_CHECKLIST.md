# Pharmaceutical development and manufacturing quality checklist

Use this checklist before publishing any manufacturing, CMC, development, R&D or drug-discovery artifact in this repository.

## Product and data identity
- [ ] Drug substance/API and finished drug product are not conflated.
- [ ] Ingredient, strength, salt/form, dosage form, route and release mechanism remain distinct.
- [ ] Units, concentration bases, sample units and conversions are explicit.
- [ ] Batch, material lot, formulation version, stage, site and timepoint are traceable where relevant.
- [ ] Dataset source, retrieval date, version/license, inclusion rules and transformations are documented.
- [ ] Public examples contain only synthetic or explicitly approved data.

## Pharmaceutical development and quality
- [ ] TPP/QTPP and intended product context are stated where relevant.
- [ ] CQA, CMA and CPP terms are used consistently and justified by evidence.
- [ ] Analytical method/version, test conditions, sample context and units are documented.
- [ ] Stability data retain condition, timepoint and packaging context.
- [ ] Risk ratings have defined scales and written rationale; an RPN is only a review aid.
- [ ] Training observations are not presented as approved specifications, proven acceptable ranges or release limits.

## Manufacturing and GMP boundaries
- [ ] The artifact does not generate or modify official GMP records.
- [ ] It does not issue manufacturing instructions or set operating parameters.
- [ ] It does not release, reject or disposition a batch.
- [ ] It does not claim process/cleaning/analytical validation.
- [ ] Deviations, CAPA and change control remain under the approved pharmaceutical quality system.
- [ ] Any model or script is validated and approved before any regulated use; this repository itself is not a validated system.

## Discovery and AI/ML
- [ ] Compound identifiers, stereochemistry, assay endpoint, units, species and assay context are retained.
- [ ] Duplicate structures, salts, repeated measurements and data leakage are considered.
- [ ] Model evaluation uses a justified split strategy and baseline.
- [ ] Applicability domain and uncertainty are reported.
- [ ] Docking, QSAR and ML outputs are explicitly described as hypotheses, not experimental confirmation.
- [ ] No candidate is described as safe, effective or clinically suitable based only on computational output.

## Communication
- [ ] Intended use and limitations are visible in the README.
- [ ] Tests cover invalid, missing, duplicate and boundary-value cases.
- [ ] Results can be reproduced from the documented inputs and commands.
- [ ] A qualified pharmacist, formulation scientist, analytical scientist, quality professional or regulatory specialist is identified as the relevant reviewer where applicable.
