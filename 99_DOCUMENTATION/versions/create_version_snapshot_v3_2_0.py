from pathlib import Path
import json
import datetime


ROOT = Path(r"E:\football_v")

OUT = ROOT / "99_DOCUMENTATION/versions/v3.2.0"


print("Football AI OS Ω+ V3.2.0 Snapshot")
print("="*60)


# 目录快照

dirs=[]

for p in ROOT.iterdir():

    if p.is_dir():

        dirs.append(str(p.name))


(OUT/"SYSTEM_STRUCTURE_SNAPSHOT_V3.2.0.txt").write_text(
    "\n".join(sorted(dirs)),
    encoding="utf-8"
)


# 模型注册快照

registry = ROOT / "50_MODEL_REGISTRY"


models=[]


if registry.exists():

    for p in registry.rglob("*"):

        if p.is_file():

            models.append(
                str(p.relative_to(ROOT))
            )


(OUT/"MODEL_REGISTRY_SNAPSHOT_V3.2.0.txt").write_text(
    "\n".join(models),
    encoding="utf-8"
)


# 迁移状态

migration = """
Football AI OS Ω+ V3.2.0 Migration Status

Architecture:
FROZEN

Model Layer:
REGISTERED

Models:
- ELO
- Dixon-Coles
- Poisson
- XGBoost
- Fusion

Registry:
COMPLETE

Legacy Scan:
COMPLETE

Cleanup:
PENDING REVIEW

Delete:
NOT EXECUTED
"""


(OUT/"MIGRATION_STATUS_V3.2.0.txt").write_text(
    migration,
    encoding="utf-8"
)


# 架构冻结文件

architecture = """
# Football AI OS Ω+ V3.2.0

Status:
Architecture Freeze

Core Layers:

01 DATA LAYER
02 FEATURE LAYER
05 MODEL AI
50 MODEL REGISTRY
06 PREDICTION ENGINE
05 MARKET LAYER
06 RISK LAYER
08 DECISION LAYER
07 BACKTEST SYSTEM
07 LEARNING LAYER
10 AI AUTONOMOUS ENGINE


Core Models:

ELO
Dixon-Coles
Poisson
XGBoost
Fusion


Version Rule:

V3.2.x:
Bug fix and optimization

V3.3.x:
New model capability

V4.0:
Architecture change
"""


(OUT/"ARCHITECTURE_FREEZE_V3.2.0.md").write_text(
    architecture,
    encoding="utf-8"
)


# Manifest

manifest={

    "system":
    "Football AI OS",

    "version":
    "Ω+ V3.2.0",

    "date":
    str(datetime.datetime.now()),

    "architecture":
    "FROZEN",

    "models":[
        "ELO",
        "Dixon-Coles",
        "Poisson",
        "XGBoost",
        "Fusion"
    ],

    "migration":
    "COMPLETED",

    "cleanup":
    "PENDING"

}


(OUT/"VERSION_MANIFEST_V3.2.0.json").write_text(
    json.dumps(
        manifest,
        indent=4,
        ensure_ascii=False
    ),
    encoding="utf-8"
)


print("="*60)
print("完成")
print("保存:")
print(OUT)