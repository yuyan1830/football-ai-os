import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(r"E:\football_v\10_GOVERNANCE_LAYER")

audit = BASE / "audit"
registry = BASE / "registry"
checkpoint = BASE / "checkpoint"


now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================
# Model Governance Approval
# ==========================

governance = [

    [
        "database_registry",
        "CURRENT_MODEL_STORE",
        "GOVERNANCE_ASSET",
        "KEEP_CURRENT",
        "LOW",
        "APPROVED"
    ],

    [
        "model_data_registry",
        "CURRENT_MODEL_STORE",
        "GOVERNANCE_ASSET",
        "KEEP_CURRENT",
        "LOW",
        "APPROVED"
    ],

    [
        "model_registry",
        "CURRENT_MODEL_STORE",
        "GOVERNANCE_ASSET",
        "KEEP_CURRENT",
        "LOW",
        "APPROVED"
    ],

    [
        "runtime_log",
        "CURRENT_MODEL_STORE",
        "RUNTIME_ASSET",
        "KEEP_CURRENT",
        "LOW",
        "APPROVED"
    ],

    [
        "system_registry",
        "CURRENT_MODEL_STORE",
        "GOVERNANCE_ASSET",
        "KEEP_CURRENT",
        "LOW",
        "APPROVED"
    ],


    [
        "elo_model",
        "LEGACY_MODEL_STORE",
        "MODEL_ASSET",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ],

    [
        "dixon_coles_model",
        "LEGACY_MODEL_STORE",
        "MODEL_ASSET",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ],

    [
        "poisson_model",
        "LEGACY_MODEL_STORE",
        "MODEL_ASSET",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ],

    [
        "xgboost_model",
        "LEGACY_MODEL_STORE",
        "MODEL_ASSET",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ],

    [
        "fusion_model",
        "LEGACY_MODEL_STORE",
        "FUSION_MODEL",
        "RETAIN",
        "HIGH",
        "FROZEN"
    ],

    [
        "model_weight",
        "LEGACY_MODEL_STORE",
        "MODEL_PARAMETER",
        "RETAIN",
        "HIGH",
        "FROZEN"
    ],

    [
        "prediction_history",
        "LEGACY_MODEL_STORE",
        "PREDICTION_HISTORY",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ],

    [
        "prediction_result",
        "LEGACY_MODEL_STORE",
        "PREDICTION_RESULT",
        "RETAIN",
        "MEDIUM",
        "FROZEN"
    ]

]


with open(
    audit / "Model_Governance_Approval_V1.0.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "Asset",
        "Source",
        "Asset_Type",
        "Decision",
        "Risk",
        "Status",
        "Validation_Time"
    ])

    for row in governance:
        writer.writerow(row+[now])



# ==========================
# Final Register
# ==========================

with open(
    registry / "Model_Final_Asset_Register_V1.0.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "Asset",
        "Ownership",
        "Lifecycle",
        "Training_Status",
        "Runtime_Status"
    ])

    data = [

        [
            "ELO",
            "LEGACY",
            "FROZEN",
            "DISABLED",
            "ARCHIVE"
        ],

        [
            "Dixon-Coles",
            "LEGACY",
            "FROZEN",
            "DISABLED",
            "ARCHIVE"
        ],

        [
            "Poisson",
            "LEGACY",
            "FROZEN",
            "DISABLED",
            "ARCHIVE"
        ],

        [
            "XGBoost",
            "LEGACY",
            "FROZEN",
            "DISABLED",
            "ARCHIVE"
        ],

        [
            "Fusion_Model",
            "LEGACY",
            "FROZEN",
            "DISABLED",
            "ARCHIVE"
        ],

        [
            "Model_Registry",
            "CURRENT",
            "ACTIVE",
            "ENABLED",
            "ACTIVE"
        ],

        [
            "Model_Data_Registry",
            "CURRENT",
            "ACTIVE",
            "ENABLED",
            "ACTIVE"
        ]

    ]

    writer.writerows(data)



# ==========================
# Freeze Report
# ==========================

with open(
    audit / "Model_Layer_Migration_Freeze_Report_V1.0.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(
f"""
# Model Layer Migration Freeze Report V1.0


Architecture:

Football_AI_OS_Betting_Intelligence_System_Omega_V3.2


Rule Source:

CLAUDE.md


## Decision


Current Governance Assets:

- model_registry
- model_data_registry
- runtime_log
- system_registry


Legacy Frozen Assets:

- Elo
- Dixon-Coles
- Poisson
- XGBoost
- Fusion Model


## Migration Policy


No database modification.

No model deletion.

No legacy overwrite.


Validation Time:

{now}

"""
)



# ==========================
# Checkpoint
# ==========================


checkpoint_data = {

    "Checkpoint":"MODEL_LAYER_V1.3",

    "Architecture":
    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

    "Rule_Source":"CLAUDE.md",

    "Status":
    "MODEL_GOVERNANCE_APPROVED",

    "Completed":[

        "Model Asset Alignment",

        "Legacy Model Review",

        "Model Classification",

        "Freeze Decision",

        "Model Governance Approval"

    ],

    "Pending":[

        "Prediction Layer Integration"

    ],

    "Modification":{

        "Database_Content":False,

        "Business_Logic":False,

        "Model_Code":False

    }

}


with open(
checkpoint / "Checkpoint_MODEL_LAYER_V1.3.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        checkpoint_data,
        f,
        indent=4,
        ensure_ascii=False
    )


print("MODEL GOVERNANCE APPROVAL COMPLETED")

