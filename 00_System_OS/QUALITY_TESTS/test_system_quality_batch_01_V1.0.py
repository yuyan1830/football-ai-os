# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


BASE=r"E:\football_v\00_SYSTEM_OS"


FILES=[

r"DEPLOYMENT_QUALITY_CHECKER\deployment_quality_checker_V1.0.py",

r"SYSTEM_HEALTH_MONITOR\system_health_monitor_V1.0.py",

r"ENVIRONMENT_CHECKER\environment_checker_V1.0.py",

r"FINAL_RELEASE_GATE\final_release_gate_V1.0.py"

]


tests=[]

failed=0


for f in FILES:

    path=os.path.join(BASE,f)

    if os.path.exists(path):

        tests.append(
        {
        "file":f,
        "status":"PASS"
        })

    else:

        failed+=1

        tests.append(
        {
        "file":f,
        "status":"FAIL"
        })


result={

"status":"PASS" if failed==0 else "FAILED",

"total_tests":len(FILES),

"failed":failed,

"tests":tests,

"time":str(datetime.now())

}


os.makedirs(
os.path.join(BASE,"QUALITY_TESTS","reports"),
exist_ok=True
)


with open(
os.path.join(BASE,"QUALITY_TESTS","reports","system_quality_test_report.json"),
"w",
encoding="utf-8"
) as f:

    json.dump(result,f,indent=4)


print(result)

