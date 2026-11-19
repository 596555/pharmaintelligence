# PHARMAINTELLIGENCE 365
## Arabic Lab for AI, Data & Digital Transformation in Pharmacy

**Mission:** Build practical, safe, evidence-based digital products for pharmacy and healthcare.

**Primary track:** Pharmaceutical & Healthcare Data Analytics  
**Secondary track:** Pharmacy Operations, Digital Transformation & Automation  
**Long-term extensions:** Pharmacovigilance analytics, bioinformatics and drug-discovery data.

> Educational portfolio only. No output replaces a licensed professional's judgment.

## Start here
1. [Project charter](00-START-HERE/PROJECT_CHARTER.md)
2. [Windows 11 setup](00-START-HERE/WINDOWS_SETUP.md)
3. [365-day roadmap](00-START-HERE/ROADMAP_365.md)
4. [Working rules](00-START-HERE/WORKING_RULES.md)
5. [Practical execution plan](00-START-HERE/EXECUTION_PLAN.md)

## Repository map
- `00-START-HERE/` — charter, setup, roadmap and rules
- `01-FOUNDATIONS/` — data literacy and statistics
- `02-EXCEL-AND-POWERBI/` — spreadsheets and BI
- `03-SQL-DATABASES/` — SQL and relational data
- `04-PYTHON-ENGINEERING/` — Python, tests and Git
- `05-PHARMACEUTICAL-DATA/` — medicine data and pharmacovigilance
- `06-MACHINE-LEARNING/` — applied ML foundations
- `07-GENERATIVE-AI/` — reliable LLM and retrieval workflows
- `08-PHARMACY-AUTOMATION/` — workflow analysis and automation
- `09-PRODUCTS/` — five portfolio products
- `10-PORTFOLIO/` — case studies
- `11-TESTS/` — quality, safety and reproducibility

## Learning capacity
10 hours/week for 52 weeks (about 520 hours). Free resources and open-source tools are prioritized.

## Safety
Never commit patient-identifiable or confidential pharmacy data. Use synthetic/public data with documented provenance. Spontaneous adverse-event reports do not establish causality or incidence. Validate medicine names, strengths, dosage forms and units; never guess missing clinical facts.

## Completion standard
Each topic produces an artifact: dataset, query, dashboard, tested script, documented workflow or case study.

## Interactive stock dashboard
- [Streamlit MVP and Windows instructions](09-PRODUCTS/Pharma-Stock-Intelligence/README.md)
- [Dashboard source](09-PRODUCTS/Pharma-Stock-Intelligence/app.py)
- [Synthetic dataset](09-PRODUCTS/Pharma-Stock-Intelligence/data/synthetic_stock.csv)

## First runnable product
- [First Product Guide](FIRST_PRODUCT_GUIDE.md)
- [Stock Intelligence CLI](stock_intelligence.py)
- [Synthetic batch data](sample_stock_batches.csv)
- [Unit tests](test_stock_intelligence.py)

Run locally with `py -m unittest -v` and `py stock_intelligence.py sample_stock_batches.csv --as-of 2026-11-19`.
