# PHARMAINTELLIGENCE 365
## Arabic Lab for AI, Data & Digital Transformation in Pharmacy

**Mission:** Build practical, safe, evidence-based digital products for pharmacy, pharmaceutical manufacturing, research and healthcare.

**Primary track:** Pharmacy Informatics & Pharmaceutical Data Analytics (medicine, batch, expiry, consumption and availability analysis)  
**Secondary track:** Pharmacy Operations, Digital Transformation & Automation  
**Specialization extension:** Pharmaceutical Manufacturing, Pharmaceutical Development, R&D and Drug Discovery  
**Long-term technical extensions:** Pharmacovigilance analytics, bioinformatics, cheminformatics and AI-supported drug discovery.

> Educational portfolio only. No output replaces a licensed professional's judgment or a regulated pharmaceutical quality system.

## Start here
1. [Open the unified browser lab](13-WEB-LAB/index.html) — Python, Excel/CSV, SQL, research and learning in one interface
2. [Web Lab setup and limitations](13-WEB-LAB/README.md)
3. [Arabic PHARMAINTELLIGENCE Academy](00-START-HERE/ACADEMY_GUIDE_AR.md) — offline lessons, practical tasks, quizzes and local progress tracking
4. [Personal AI tutor prompt](00-START-HERE/AI_TUTOR_PROMPT_AR.md) — turn ChatGPT into an interactive pharmacy/AI tutor
5. [Project charter](00-START-HERE/PROJECT_CHARTER.md)
6. [Windows 11 setup](00-START-HERE/WINDOWS_SETUP.md)
7. [365-day roadmap](00-START-HERE/ROADMAP_365.md)
8. [Working rules](00-START-HERE/WORKING_RULES.md)
9. [Practical execution plan](00-START-HERE/EXECUTION_PLAN.md)

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
- `08-RESEARCH-TOOLS/` — public research APIs, provenance-aware data connectors and integration guide
- `09-PRODUCTS/` — six portfolio products (some are still planned)
- `10-PORTFOLIO/` — case studies
- `10-LEARNING-RESOURCES/` — free courses, badges and certificate guidance
- `11-TESTS/` — quality, safety and reproducibility
- `12-DRUG-DEVELOPMENT-RD/` — manufacturing, GMP, QbD, CMC, R&D and drug discovery
- `13-WEB-LAB/` — unified Arabic browser workspace with Python, spreadsheets, SQL, research and academy

## Pharmacy and pharmaceutical specialist skills
- [Pharmacy domain skills](05-PHARMACEUTICAL-DATA/PHARMACY_SPECIALIST_SKILLS.md)
- [Advanced stock analytics](09-PRODUCTS/Pharma-Stock-Intelligence/ADVANCED_ANALYTICS.md)
- [Pharmacy ML practice](06-MACHINE-LEARNING/PHARMACY_ML_PRACTICE.md)
- [Pharma RAG practice](07-GENERATIVE-AI/PHARMA_RAG_PRACTICE.md)
- [Pharmacy SQL examples](03-SQL-DATABASES/PHARMACY_ANALYTICS_QUERIES.sql)
- [Manufacturing, R&D and drug discovery learning track](12-DRUG-DEVELOPMENT-RD/README.md)
- [12-week manufacturing and R&D learning plan](12-DRUG-DEVELOPMENT-RD/LEARNING_PLAN_12_WEEKS.md)

## Free courses and connected research environment
- [Free courses and certificates (Arabic)](10-LEARNING-RESOURCES/FREE_COURSES_AND_CERTIFICATES_AR.md)
- [Connected scientific research environment](08-RESEARCH-TOOLS/RESEARCH_ENVIRONMENT_AR.md)
- [Public data connector: openFDA, PubChem and RxNorm](08-RESEARCH-TOOLS/data_hub.py)

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
