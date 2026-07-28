import os
import json
from datetime import datetime


ROOT = r"E:\football_v"


AUDIT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit"
)


ARCHITECTURE = "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2"

BASELINE = "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md"

LEGACY_SOURCE = "Football_AI_OS_Legacy_Asset_Index_V1.0"

RULE_SOURCE = "CLAUDE.md"



# Runtime候选入口
RUNTIME_TARGETS = [

    "AI_RUNTIME",

    "11_System_Intelligence",

    "18_MODEL_EXECUTION_ENGINE",

    "06_PREDICTION_INTELLIGENCE_ENGINE",

    "27_MODEL_FUSION_ENGINE",

    "08_DECISION_LAYER",

    "09_APPLICATION_LAYER",

    "12_API_LAYER"

]



KEYWORDS = [

    "main",

    "run",

    "start",

    "execute",

    "predict",

    "fusion",

    "decision",

    "api",

    "runtime"

]



result = {

    "Phase":
    "PHASE11.5_PART3_RUNTIME_MAIN_PATH_CONFIRMATION",


    "Architecture":
    ARCHITECTURE,


    "Baseline":
    BASELINE,


    "Legacy_Source":
    LEGACY_SOURCE,


    "Rule_Source":
    RULE_SOURCE,


    "Status":
    "RUNTIME_SCAN_COMPLETED",


    "Runtime_Candidates": [],


    "Main_Path_Analysis": {


        "Input": [],

        "Model": [],

        "Fusion": [],

        "Decision": [],

        "Output": []

    },


    "Modification": {

        "Database_Content": False,

        "Business_Logic": False,

        "Model_Code": False

    },


    "Validation_Time":
    str(datetime.now())

}



for target in RUNTIME_TARGETS:

    path = os.path.join(ROOT,target)


    if os.path.exists(path):

        files=[]


        for root,dirs,fs in os.walk(path):

            for f in fs:

                if f.endswith(".py"):

                    files.append(
                        os.path.join(root,f)
                    )


        candidate=[]


        for f in files:

            name=f.lower()


            if any(k in name for k in KEYWORDS):

                candidate.append(f)



        item={

            "Path":path,

            "Python_File_Count":len(files),

            "Runtime_Keyword_Files":candidate[:20]

        }


        result["Runtime_Candidates"].append(item)



        lname=target.lower()


        if "prediction" in lname:

            result["Main_Path_Analysis"]["Input"].append(item)


        elif "fusion" in lname:

            result["Main_Path_Analysis"]["Fusion"].append(item)


        elif "decision" in lname:

            result["Main_Path_Analysis"]["Decision"].append(item)


        elif "api" in lname or "application" in lname:

            result["Main_Path_Analysis"]["Output"].append(item)


        else:

            result["Main_Path_Analysis"]["Model"].append(item)



output=os.path.join(

    AUDIT_PATH,

    "Phase11.5_Part3_Runtime_Main_Path_Confirmation_V1.0.json"

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
    "PHASE11.5 PART3 COMPLETED"
)

print(output)

