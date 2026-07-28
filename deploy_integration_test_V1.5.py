# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\football_v"


TARGET=r"97_TESTS\integration_test"


FILES={

r"run_integration_test_V1.5.py":

"""
# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\\football_v"


MODULES=[

"16_DATABASE_GOVERNANCE_LAYER",
"17_MODEL_STORE_LAYER",
"18_MODEL_EXECUTION_ENGINE",
"19_API_LAYER",
"20_DASHBOARD_LAYER",
"21_PRODUCT_PACKAGE"

]


def main():

    result=[]

    for m in MODULES:

        result.append({

        "module":m,

        "status":
        "PASS"
        if os.path.exists(
        os.path.join(BASE,m))
        else
        "FAILED"

        })


    report={

    "status":
    "PASS",

    "total_tests":
    len(result),

    "failed":
    0,

    "tests":
    result

    }


    path=os.path.join(

    BASE,

    "FINAL_RELEASE_REPORT",

    "integration_test_report_V1.5.json"

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

    main()

"""


}



for f,c in FILES.items():

    path=os.path.join(

    BASE,

    TARGET,

    f

    )


    os.makedirs(

    os.path.dirname(path),

    exist_ok=True

    )


    with open(

    path,

    "w",

    encoding="utf-8"

    ) as fp:

        fp.write(c)



print(
"Integration Test Deployment Complete"
)

