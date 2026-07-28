# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\football_v"


checks=[

{
"name":"Framework",
"path":"00_SYSTEM_OS",
"required":False
},

{
"name":"Data Layer",
"path":"01_DATA_LAYER",
"required":False
},

{
"name":"Database Governance",
"path":"16_DATABASE_GOVERNANCE_LAYER",
"required":False
},

{
"name":"Model Store",
"path":"17_MODEL_STORE_LAYER",
"required":True
},

{
"name":"Model Execution",
"path":"18_MODEL_EXECUTION_ENGINE",
"required":True
},

{
"name":"API Layer",
"path":"19_API_LAYER",
"required":True
},

{
"name":"Dashboard",
"path":"20_DASHBOARD_LAYER",
"required":True
},

{
"name":"Product Package",
"path":"21_PRODUCT_PACKAGE",
"required":True
},

{
"name":"AI Feature Store",
"path":"22_AI_FEATURE_STORE_LAYER",
"required":True
},

{
"name":"Training Engine",
"path":"23_MODEL_TRAINING_ENGINE",
"required":True
},

{
"name":"Prediction Intelligence",
"path":"24_PREDICTION_INTELLIGENCE_LAYER",
"required":True
},

{
"name":"Backtest Engine",
"path":"25_BACKTEST_ENGINE",
"required":True
},

{
"name":"Automation Layer",
"path":"26_AUTOMATION_LAYER",
"required":True
}

]


results=[]

failed=0


for item in checks:

    full=os.path.join(BASE,item["path"])

    if os.path.exists(full):

        status="PASS"

    else:

        if item["required"]:
            status="FAILED"
            failed+=1
        else:
            status="SKIPPED"


    results.append({

        "name":item["name"],
        "path":item["path"],
        "status":status

    })


report={

"system":

"Football AI OS",

"version":

"V2.0",

"validation":

"Release Validation",

"status":

"PASS" if failed==0 else "FAILED",

"total_checks":

len(checks),

"failed":

failed,

"checks":

results,

"time":

str(datetime.datetime.now())

}


out=os.path.join(

BASE,

"FINAL_RELEASE_REPORT",

"AI_OS_V2.0_RELEASE_VALIDATION_REPORT.json"

)


with open(

out,

"w",

encoding="utf-8"

) as f:

    json.dump(

        report,

        f,

        indent=4,

        ensure_ascii=False

    )


print(json.dumps(report,indent=4,ensure_ascii=False))

