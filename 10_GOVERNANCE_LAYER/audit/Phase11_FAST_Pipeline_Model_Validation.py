import os
import json
from datetime import datetime


ROOT = r"E:\football_v"


CHECK_PATHS = {

    "DATA":
        "01_DATA_LAYER",

    "FEATURE":
        "02_FEATURE_LAYER",

    "MODEL":
        "03_MODEL_LAYER",

    "PREDICTION":
        "04_PREDICTION_LAYER",

    "MARKET":
        "05_MARKET_LAYER",

    "RISK":
        "06_RISK_LAYER",

    "DECISION":
        "08_DECISION_LAYER",

    "APPLICATION":
        "09_APPLICATION_LAYER"

}


MODEL_KEYWORDS = [

    "elo",
    "dixon",
    "poisson",
    "xgboost",
    "fusion",
    "model"

]


result = {

    "Phase":
        "PHASE11_FAST_PART2_PIPELINE_MODEL_VALIDATION",

    "Architecture":
        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

    "Baseline":
        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md",

    "Legacy_Source":
        "Football_AI_OS_Legacy_Asset_Index_V1.0",

    "Rule_Source":
        "CLAUDE.md",

    "Pipeline_Check": {},

    "Model_Discovery": [],

    "Modification": {

        "Database_Content": False,
        "Business_Logic": False,
        "Model_Code": False

    },

    "Validation_Time":
        str(datetime.now())

}



for name, folder in CHECK_PATHS.items():

    path = os.path.join(
        ROOT,
        folder
    )

    result["Pipeline_Check"][name] = {

        "Path":
            path,

        "Exists":
            os.path.exists(path),

        "Status":
            "PASS" if os.path.exists(path) else "FAIL"

    }



for root, dirs, files in os.walk(ROOT):

    for file in files:

        lower = file.lower()

        for key in MODEL_KEYWORDS:

            if key in lower:

                result["Model_Discovery"].append(
                    os.path.join(root,file)
                )

                break



out = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit",
    "Phase11_FAST_Pipeline_Model_Validation_V1.0.json"
)


with open(
    out,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
    "PHASE11 FAST PART2 COMPLETED"
)


print(
    "Pipeline:"
)

for k,v in result["Pipeline_Check"].items():

    print(
        k,
        v["Status"]
    )


print(
    "Models Found:",
    len(result["Model_Discovery"])
)


print(out)

