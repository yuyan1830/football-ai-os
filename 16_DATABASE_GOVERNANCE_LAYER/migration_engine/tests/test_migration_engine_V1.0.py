# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


BASE = r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER\migration_engine"


def test():

    files = [

        r"migration_engine_V1.0.py",

        r"config\migration_config.json",

        r"registry\migration_registry.json"

    ]


    tests = []

    failed = 0


    for file in files:

        exists = os.path.exists(
            os.path.join(BASE, file)
        )


        tests.append(
            {
                "file": file,
                "status": "PASS" if exists else "FAIL"
            }
        )


        if not exists:

            failed += 1


    report = {

        "status":
        "PASS" if failed == 0 else "FAIL",

        "total_tests":
        len(files),

        "failed":
        failed,

        "tests":
        tests,

        "time":
        str(datetime.now())

    }


    report_path = os.path.join(
        BASE,
        "reports",
        "migration_test_report.json"
    )


    os.makedirs(
        os.path.dirname(report_path),
        exist_ok=True
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


    print(report)


if __name__ == "__main__":

    test()

