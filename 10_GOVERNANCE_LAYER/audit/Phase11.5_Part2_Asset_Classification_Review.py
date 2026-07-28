import os
import json
from datetime import datetime


ROOT = r"E:\football_v"


AUDIT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit"
)


ARCHITECTURE = (
    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2"
)


BASELINE = (
    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md"
)


LEGACY_SOURCE = (
    "Football_AI_OS_Legacy_Asset_Index_V1.0"
)


RULE_SOURCE = (
    "CLAUDE.md"
)



# 重点资产扫描范围
TARGET_PATHS = [

    "05_MODEL_AI",

    "06_PREDICTION_INTELLIGENCE_ENGINE",

    "11_System_Intelligence",

    "17_MODEL_STORE_LAYER",

    "18_MODEL_EXECUTION_ENGINE",

    "23_MODEL_TRAINING_ENGINE",

    "27_MODEL_FUSION_ENGINE",

    "40_MODEL_TRAINING_PIPELINE",

    "50_MODEL_REGISTRY",

    "AI_RUNTIME"

]



result = {


    "Phase":
    "PHASE11.5_PART2_ASSET_CLASSIFICATION_REVIEW",


    "Architecture":
    ARCHITECTURE,


    "Baseline":
    BASELINE,


    "Legacy_Source":
    LEGACY_SOURCE,


    "Rule_Source":
    RULE_SOURCE,


    "Status":
    "ASSET_SCAN_COMPLETED",


    "Classification":{


        "Runtime_Core":[],

        "Governance_Asset":[],

        "Training_Asset":[],

        "Legacy_Asset":[],

        "Freeze_Candidate":[]

    },


    "Scanned_Path":[],


    "Modification":{


        "Database_Content":False,

        "Business_Logic":False,

        "Model_Code":False

    },


    "Validation_Time":
    str(datetime.now())

}



for target in TARGET_PATHS:


    path = os.path.join(
        ROOT,
        target
    )


    if os.path.exists(path):


        result["Scanned_Path"].append(path)


        files=[]


        for root,dirs,fs in os.walk(path):

            for f in fs:

                files.append(
                    os.path.join(root,f)
                )


        item={

            "Path":path,

            "File_Count":len(files),

            "Sample_Files":files[:10]

        }



        # 初步分类规则
        name = target.lower()


        if "store" in name or "registry" in name:

            result["Classification"]["Governance_Asset"].append(item)


        elif "training" in name:

            result["Classification"]["Training_Asset"].append(item)


        elif "runtime" in name or "execution" in name:

            result["Classification"]["Runtime_Core"].append(item)


        elif "intelligence" in name or "fusion" in name:

            result["Classification"]["Runtime_Core"].append(item)


        else:

            result["Classification"]["Freeze_Candidate"].append(item)



output = os.path.join(

    AUDIT_PATH,

    "Phase11.5_Part2_Asset_Classification_Review_V1.0.json"

)



with open(
    output,
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
    "PHASE11.5 PART2 COMPLETED"
)


print(
    output
)

