from pathlib import Path


ROOT=Path(r"E:\football_v")

OUT=ROOT/"99_DOCUMENTATION/versions/v3.2.0/MODEL_REGISTRY_SNAPSHOT_V3.2.0_FULL.txt"


models=[
    (
    "ELO",
    "05_MODEL_AI/MODEL_LAYER/models/elo_model.py",
    "50_MODEL_REGISTRY/models/elo_model_V4.0.json",
    "REGISTERED"
    ),

    (
    "Dixon-Coles",
    "05_MODEL_AI/MODEL_LAYER/models/dixon_coles_model.py",
    "",
    "REGISTERED"
    ),

    (
    "Poisson",
    "05_MODEL_AI/MODEL_LAYER/models/poisson_model.py",
    "",
    "REGISTERED"
    ),

    (
    "XGBoost",
    "05_MODEL_AI/MODEL_LAYER/models/xgboost_model.py",
    "",
    "REGISTERED"
    ),

    (
    "Fusion",
    "05_AI_Intelligence_Layer/FUSION_DECISION_ENGINE/fusion_engine.py",
    "",
    "REGISTERED"
    )
]


text=[]

text.append(
"Football AI OS ¦¸+ V3.2.0 MODEL REGISTRY SNAPSHOT"
)

text.append("="*60)


for m in models:

    text.append(
f"""
MODEL:
{m[0]}

FILE:
{m[1]}

REGISTRY:
{m[2]}

STATUS:
{m[3]}

------------------------------
"""
)


OUT.write_text(
    "\n".join(text),
    encoding="utf-8"
)


print("Íê³É")
print(OUT)