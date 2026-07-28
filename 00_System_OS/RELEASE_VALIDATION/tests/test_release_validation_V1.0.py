
# -*- coding:utf-8 -*-

import os
import json
from datetime import datetime


def test():

    tests=[]

    files=[
    "E:\\football_v\\00_SYSTEM_OS\\RELEASE_VALIDATION\\release_validation_engine\\release_validation_engine_V1.0.py",
    "E:\\football_v\\00_SYSTEM_OS\\RELEASE_VALIDATION\\module_scanner\\module_scanner_V1.0.py",
    "E:\\football_v\\00_SYSTEM_OS\\RELEASE_VALIDATION\\dependency_checker\\dependency_checker_V1.0.py",
    "E:\\football_v\\00_SYSTEM_OS\\RELEASE_VALIDATION\\integrity_checker\\integrity_checker_V1.0.py"
    ]


    for f in files:

        tests.append(
        {
        "file":f,
        "status":"PASS" if os.path.exists(f) else "FAIL"
        }
        )


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


    os.makedirs(
    "reports",
    exist_ok=True
    )


    with open(
    "reports/release_validation_test_report.json",
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



if __name__=="__main__":
    test()
