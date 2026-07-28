# -*- coding:utf-8 -*-

import os
import json
import py_compile
from datetime import datetime


BASE=r"E:\football_v\00_SYSTEM_OS\ARCHITECTURE_CLEANUP"


FILES=[

r"architecture_scanner\architecture_scanner_V1.0.py",

r"architecture_classifier\architecture_classifier_V1.0.py",

r"registry_manager\registry_manager_V1.1.py",

r"config\architecture_rules.json"

]


tests=[]


for f in FILES:

    path=os.path.join(BASE,f)

    status="PASS"

    try:

        py_compile.compile(
        path,
        doraise=True
        )

    except:

        status="FAIL"


    tests.append({

    "file":path,

    "status":status

    })


failed=len(
[
x for x in tests
if x["status"]=="FAIL"
]
)


report={

"status":"PASS" if failed==0 else "FAILED",

"total_tests":len(tests),

"failed":failed,

"tests":tests,

"time":str(datetime.now())

}


REPORT=r"E:\football_v\00_SYSTEM_OS\ARCHITECTURE_CLEANUP\reports\architecture_cleanup_test_report.json"


os.makedirs(
os.path.dirname(REPORT),
exist_ok=True
)


with open(
REPORT,
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

