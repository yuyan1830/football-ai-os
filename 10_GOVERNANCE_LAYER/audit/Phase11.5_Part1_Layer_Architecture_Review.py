import os
import json
from datetime import datetime


ROOT = r"E:\football_v"


LAYERS = [

"01_DATA_LAYER",
"02_FEATURE_LAYER",
"03_MODEL_LAYER",
"04_PREDICTION_LAYER",
"05_MARKET_LAYER",
"06_RISK_LAYER",
"07_LEARNING_LAYER",
"08_DECISION_LAYER",
"09_APPLICATION_LAYER",
"10_GOVERNANCE_LAYER",
"11_SIMULATION_LAYER",
"12_API_LAYER",
"13_TEST_LAYER",
"99_DOCUMENTATION"

]


result = {

"Phase":
"PHASE11.5_PART1_LAYER_ARCHITECTURE_REVIEW",

"Architecture":
"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

"Baseline":
"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md",

"Legacy_Source":
"Football_AI_OS_Legacy_Asset_Index_V1.0",

"Rule_Source":
"CLAUDE.md",

"Layers":{},


"Modification":{

"Database_Content":False,
"Business_Logic":False,
"Model_Code":False

},


"Validation_Time":
str(datetime.now())

}



for layer in LAYERS:

    path=os.path.join(ROOT,layer)

    result["Layers"][layer]={

    "Exists":os.path.exists(path),

    "Path":path,

    "Status":
    "PASS" if os.path.exists(path) else "MISSING"

    }



out=os.path.join(

ROOT,

"10_GOVERNANCE_LAYER",

"audit",

"Phase11.5_Part1_Layer_Architecture_Review_V1.0.json"

)


with open(out,"w",encoding="utf-8") as f:

    json.dump(

    result,

    f,

    indent=4,

    ensure_ascii=False

    )


print("PHASE11.5 PART1 COMPLETED")

print(out)

