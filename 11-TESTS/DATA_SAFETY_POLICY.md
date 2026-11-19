# Data Safety Policy

## Allowed
- Synthetic data created for this repository.
- Public datasets used within published terms.
- De-identified data only when lawful, authorized and reviewed for re-identification risk.

## Prohibited
- Patient names, phone numbers, addresses, national IDs, prescriptions or identifiable histories.
- Confidential pharmacy/employer exports without written permission.
- Credentials, API keys, access tokens or private URLs.
- Data with unclear licensing or permitted use.

## Safeguards
Preserve units and source labels. Validate medicine identity, strength, dosage form and route. Never guess missing clinical facts. Distinguish report counts from rates and association from causation. Require qualified human review.

Before each commit, inspect changed files for personal data/secrets, confirm data terms, inspect notebook outputs and remove temporary exports.
