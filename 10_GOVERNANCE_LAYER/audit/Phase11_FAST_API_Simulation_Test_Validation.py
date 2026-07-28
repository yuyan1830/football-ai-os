import os
import json
from datetime import datetime


ROOT = r"E:\football_v"


CHECK_ITEMS = {


    "API_LAYER":
        "12_API_LAYER",


    "SIMULATION_LAYER":
        "11_SIMULATION_LAYER",


    "TEST_LAYER":
        "13_TEST_LAYER",


    "GOVERNANCE_LAYER":
        "10_GOVERNANCE_LAYER"


}



KEYWORDS = [

    "api",

    "simulation",

    "sim",

    "test",

    "runtime",

    "report"

]


result = {


    "Phase":

        "PHASE11_FAST_PART3_API_SIMULATION_TEST_VALIDATION",


    "Architecture":

        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",


    "Baseline":

        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md",


    "Legacy_Source":

        "Football_AI_OS_Legacy_Asset_Index_V1.0",


    "Rule_Source":

        "CLAUDE.md",



    "Layer_Check": {},


    "Runtime_Discovery": [],


    "Modification": {


        "Database_Content": False,

        "Business_Logic": False,

        "Model_Code": False

    },


    "Validation_Time":

        str(datetime.now())

}




for name, folder in CHECK_ITEMS.items():

    path = os.path.join(

        ROOT,

        folder

    )


    result["Layer_Check"][name] = {


        "Path":

            path,


        "Exists":

            os.path.exists(path),


        "Status":

            "PASS" if os.path.exists(path) else "FAIL"


    }




for root, dirs, files in os.walk(ROOT):


    if any(x in root for x in [

        ".venv",

        "__pycache__"

    ]):

        continue


    for file in files:


        lower = file.lower()


        if any(k in lower for k in KEYWORDS):


            result["Runtime_Discovery"].append(

                os.path.join(root,file)

            )



out = os.path.join(

    ROOT,

    "10_GOVERNANCE_LAYER",

    "audit",

    "Phase11_FAST_API_Simulation_Test_Validation_V1.0.json"

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

    "PHASE11 FAST PART3 COMPLETED"

)


for k,v in result["Layer_Check"].items():

    print(

        k,

        v["Status"]

    )


print(

    "Runtime Assets:",

    len(result["Runtime_Discovery"])

)


print(out)

