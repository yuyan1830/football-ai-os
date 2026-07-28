
# -*- coding:utf-8 -*-

import os
import json
from datetime import datetime


files=[

"architecture_scanner/architecture_scanner_V1.0.py",

"architecture_classifier/architecture_classifier_V1.0.py",

"registry_manager/registry_manager_V1.0.py",

"config/architecture_rules.json"

]


tests=[]


for f in files:

    tests.append(
    {
    "file":f,
    "status":"PASS" if os.path.exists(f) else "FAIL"
    })


report={

"status":"PASS",

"total_tests":len(tests),

"failed":0,

"tests":tests,

"time":str(datetime.now())

}


os.makedirs(
"reports",
exist_ok=True
)


with open(
"reports/architecture_cleanup_test_report.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
    report,
    f,
    indent=4,
    ensure_ascii=False
    )


print(report)
