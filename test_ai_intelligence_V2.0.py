# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\football_v"


modules=[

"22_AI_FEATURE_STORE_LAYER",
"23_MODEL_TRAINING_ENGINE",
"24_PREDICTION_INTELLIGENCE_LAYER",
"25_BACKTEST_ENGINE",
"26_AUTOMATION_LAYER"

]


results=[]

failed=0


for module in modules:

    path=os.path.join(BASE,module)

    if os.path.exists(path):

        status="PASS"

    else:

        status="FAILED"
        failed+=1


    results.append({

        "module":module,
        "path":module,
        "status":status

    })


report={

    "status":"PASS" if failed==0 else "FAILED",

    "total_tests":len(modules),

    "failed":failed,

    "tests":results,

    "time":str(datetime.datetime.now())

}


report_path=os.path.join(

BASE,

"FINAL_RELEASE_REPORT",

"AI_OS_V2.0_TEST_REPORT.json"

)


with open(

report_path,

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

