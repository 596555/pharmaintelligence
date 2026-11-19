# PHARMAINTELLIGENCE 365
## Arabic Lab for AI, Data & Digital Transformation in Pharmacy

**Mission:** Build practical, safe, evidence-based digital products for pharmacy, pharmaceutical manufacturing, research and healthcare.

**Primary track:** Pharmacy Informatics & Pharmaceutical Data Analytics (medicine, batch, expiry, consumption and availability analysis)  
**Secondary track:** Pharmacy Operations, Digital Transformation & Automation  
**Specialization extension:** Pharmaceutical Manufacturing, Pharmaceutical Development, R&D and Drug Discovery  
**Long-term technical extensions:** Pharmacovigilance analytics, bioinformatics, cheminformatics and AI-supported drug discovery.

> Educational portfolio only. No output replaces a licensed professional's judgment or a regulated pharmaceutical quality system.

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
- `09-PRODUCTS/` — six portfolio products (some are still planned)
- `10-PORTFOLIO/` — case studies
- `11-TESTS/` — quality, safety and reproducibility
- `12-DRUG-DEVELOPMENT-RD/` — manufacturing, GMP, QbD, CMC, R&D and drug discovery

## Pharmacy and pharmaceutical specialist skills
- [Pharmacy domain skills](05-PHARMACEUTICAL-DATA/PHARMACY_SPECIALIST_SKILLS.md)
- [Advanced stock analytics](09-PRODUCTS/Pharma-Stock-Intelligence/ADVANCED_ANALYTICS.md)
- [Pharmacy ML practice](06-MACHINE-LEARNING/PHARMACY_ML_PRACTICE.md)
- [Pharma RAG practice](07-GENERATIVE-AI/PHARMA_RAG_PRACTICE.md)
- [Pharmacy SQL examples](03-SQL-DATABASES/PHARMACY_ANALYTICS_QUERIES.sql)
- [Manufacturing, R&D and drug discovery learning track](12-DRUG-DEVELOPMENT-RD/README.md)
- [12-week manufacturing and R&D learning plan](12-DRUG-DEVELOPMENT-RD/LEARNING_PLAN_12_WEEKS.md)

## Learning capacity
10 hours/week for 52 weeks (about 520 hours). Free resources and open-source tools are prioritized. The manufacturing/R&D block is integrated as a specialization extension; it does not replace the core data, programming and pharmacy-informatics foundations.

## Safety
Never commit patient-identifiable or confidential pharmacy/manufacturing data. Use synthetic/public data with documented provenance. Spontaneous adverse-event reports do not establish causality or incidence. Validate medicine names, strengths, dosage forms and units; never guess missing clinical facts. Never treat a training model or synthetic development record as a manufacturing instruction, product specification, batch-release decision or clinical recommendation.

## Quality and safety review
- [Pharmaceutical development and manufacturing checklist](11-TESTS/PHARMACEUTICAL_DEVELOPMENT_CHECKLIST.md)

## Completion standard
Each topic produces an artifact: dataset, query, dashboard, tested script, documented workflow, evidence map or case study.

## Interactive stock dashboard
- [Streamlit MVP and Windows instructions](09-PRODUCTS/Pharma-Stock-Intelligence/README.md)
- [Dashboard source](09-PRODUCTS/Pharma-Stock-Intelligence/app.py)
- [Synthetic batch stock](09-PRODUCTS/Pharma-Stock-Intelligence/data/synthetic_stock.csv)
- [Synthetic consumption history](09-PRODUCTS/Pharma-Stock-Intelligence/data/synthetic_consumption.csv)
- [Advanced analytics engine](09-PRODUCTS/Pharma-Stock-Intelligence/src/advanced_analytics.py)
- [Medicine Master Data Validator](09-PRODUCTS/Medicine-Data-Cleaner/README.md)

## New manufacturing and R&D workbench
- [Drug Development & Manufacturing Intelligence Workbench](09-PRODUCTS/Drug-Development-Workbench/README.md)
- [Synthetic development-batch data](09-PRODUCTS/Drug-Development-Workbench/data/synthetic_development_batches.csv)
- [Synthetic QbD risk register](09-PRODUCTS/Drug-Development-Workbench/data/synthetic_qbd_risk_register.csv)

## First runnable product
- [First Product Guide](FIRST_PRODUCT_GUIDE.md)
- [Stock Intelligence CLI](stock_intelligence.py)
- [Synthetic batch data](sample_stock_batches.csv)
- [Unit tests](test_stock_intelligence.py)

Run locally with `py -m unittest -v` and `py stock_intelligence.py sample_stock_batches.csv --as-of 2026-11-19`.
