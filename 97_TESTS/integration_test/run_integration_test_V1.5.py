
# -*- coding: utf-8 -*-

import os
import json
import datetime


BASE=r"E:\football_v"


CHECK_ITEMS={

"database":
"01_DATA_LAYER",

"governance":
"16_DATABASE_GOVERNANCE_LAYER",

"model_store":
"17_MODEL_STORE_LAYER",

"execution":
"18_MODEL_EXECUTION_ENGINE",

"api":
"19_API_LAYER",

"dashboard":
"20_DASHBOARD_LAYER",

"product":
"21_PRODUCT_PACKAGE"

}



def run_test():


    tests=[]


    failed=0


    for name,path in CHECK_ITEMS.items():

        full=os.path.join(BASE,path)

        status="PASS" if os.path.exists(full) else "FAILED"


        if status=="FAILED":

            failed+=1


        tests.append({

        "test":name,

        "path":path,

        "status":status

        })


    report={


    "status":
    "PASS" if failed==0 else "FAILED",


    "total_tests":
    len(tests),


    "failed":
    failed,


    "tests":
    tests,


    "time":
    str(datetime.datetime.now())


    }


    output=os.path.join(

    BASE,

    "FINAL_RELEASE_REPORT",

    "integration_test_report_V1.5.json"

    )


    os.makedirs(

    os.path.dirname(output),

    exist_ok=True

    )


    with open(

    output,

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



if __name__=="__main__":

    run_test()

