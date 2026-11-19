# Generative AI for pharmaceutical knowledge workflows

## Product brief
Build a retrieval assistant over a small, curated set of public official medicine documents. It supports staff education and document navigation, not patient-specific prescribing.

## Required controls
- Store document title, issuing authority, URL, publication/revision date and retrieval date.
- Retrieve passages before generation; cite the exact document and section.
- Validate extracted medicine name, strength, dosage form and route against the source.
- Abstain if sources conflict, are missing, or do not answer the question.
- Clearly distinguish official labeling from local formulary/SOP.
- Never invent dosage, contraindications, interactions or stability facts.
- No patient records or confidential documents in the prototype.

## Evaluation set
At least 30 questions: 10 answerable, 10 unanswerable, 5 conflicting-source and 5 exact-strength/form questions. Score citation support, factual correctness, correct abstention and unsafe-answer rate.
