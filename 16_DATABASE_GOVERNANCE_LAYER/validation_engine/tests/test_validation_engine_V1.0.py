# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


BASE = r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER\validation_engine"


def test():

    files=[

        r"validation_engine_V1.0.py",

        r"config\validation_config.json",

        r"registry\validation_registry.json"

    ]


    tests=[]

    failed=0


    for file in files:

        result=os.path.exists(

            os.path.join(
                BASE,
                file
            )

        )


        tests.append({

            "file":file,

            "status":
            "PASS" if result else "FAIL"

        })


        if not result:

            failed+=1



    report={

        "status":
        "PASS" if failed==0 else "FAIL",

        "total_tests":
        len(files),

        "failed":
        failed,

        "tests":
        tests,

        "time":
        str(datetime.now())

    }


    path=os.path.join(

        BASE,

        "reports",

        "validation_test_report.json"

    )


    os.makedirs(

        os.path.dirname(path),

        exist_ok=True

    )


    with open(

        path,

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

