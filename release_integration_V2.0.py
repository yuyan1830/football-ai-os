# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\football_v"


release_dir=os.path.join(

BASE,

"RELEASE_CANDIDATE"

)


os.makedirs(

release_dir,

exist_ok=True

)


components=[

"00_SYSTEM_OS",

"01_DATA_LAYER",

"16_DATABASE_GOVERNANCE_LAYER",

"17_MODEL_STORE_LAYER",

"18_MODEL_EXECUTION_ENGINE",

"19_API_LAYER",

"20_DASHBOARD_LAYER",

"21_PRODUCT_PACKAGE",

"22_AI_FEATURE_STORE_LAYER",

"23_MODEL_TRAINING_ENGINE",

"24_PREDICTION_INTELLIGENCE_LAYER",

"25_BACKTEST_ENGINE",

"26_AUTOMATION_LAYER"

]


results=[]

failed=0


for c in components:

    path=os.path.join(BASE,c)

    status="PASS" if os.path.exists(path) else "FAILED"

    if status=="FAILED":

        failed+=1

    results.append({

        "component":c,

        "status":status

    })


release_report={

"system":

"Football AI OS",

"version":

"V2.0",

"release":

"RELEASE_CANDIDATE",

"status":

"READY" if failed==0 else "FAILED",

"components":

results,

"failed":

failed,

"time":

str(datetime.datetime.now())

}



out=os.path.join(

BASE,

"FINAL_RELEASE_REPORT",

"AI_OS_V2.0_FINAL_RELEASE_REPORT.json"

)


with open(

out,

"w",

encoding="utf-8"

) as f:

    json.dump(

        release_report,

        f,

        indent=4,

        ensure_ascii=False

    )


print(json.dumps(release_report,indent=4,ensure_ascii=False))

