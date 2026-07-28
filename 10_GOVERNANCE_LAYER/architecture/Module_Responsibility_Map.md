# Football AI OS Module Responsibility Map

Version:
V1.0


| Module | Responsibility | Target Layer |
|---|---|---|
| System Engine | Core system management | 01_SYSTEM_LAYER |
| Data Engine | Data ingestion and storage | 02_DATA_LAYER |
| Feature Engine | Feature generation and management | 03_FEATURE_STORE_LAYER |
| Elo Engine | Team strength rating | 04_MODEL_LAYER |
| Poisson Engine | Goal probability modeling | 04_MODEL_LAYER |
| Dixon-Coles Engine | Goal correlation correction | 04_MODEL_LAYER |
| XGBoost Engine | Machine learning prediction | 04_MODEL_LAYER |
| Fusion Engine | Multi-model fusion | 04_MODEL_LAYER |
| Prediction Engine | Match prediction output | 05_PREDICTION_LAYER |
| Market Engine | Odds and market intelligence | 06_MARKET_INTELLIGENCE_LAYER |
| Decision Engine | Betting decision | 07_DECISION_LAYER |
| Runtime Engine | Task execution | 08_RUNTIME_LAYER |
| Report Engine | Analysis reports | 09_REPORT_LAYER |
| Governance Engine | Architecture control | 10_GOVERNANCE_LAYER |
