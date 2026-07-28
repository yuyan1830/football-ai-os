cd E:\football_v

python deploy\deploy_v15_phase2.py

python -m pytest 03_Data_Governance/tests 04_Data_Processing_AI/feature_store/tests 05_MODEL_AI/MODEL_LAYER/tests 06_PREDICTION_ENGINE/tests 07_BACKTEST_AI/tests 08_DECISION_ENGINE/tests 09_AI_ORCHESTRATION_LAYER/tests 10_AI_AUTONOMOUS_ENGINE/tests 11_SYSTEM_INTELLIGENCE/tests

tree /F
