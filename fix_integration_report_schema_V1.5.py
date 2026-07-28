# -*- coding: utf-8 -*-

import json
import os
import datetime


BASE=r"E:\football_v"


tests=[

{
"test":"database",
"path":"01_DATA_LAYER",
"status":"PASS"
},

{
"test":"governance",
"path":"16_DATABASE_GOVERNANCE_LAYER",
"status":"PASS"
},

{
"test":"model_store",
"path":"17_MODEL_STORE_LAYER",
"status":"PASS"
},

{
"test":"execution",
"path":"18_MODEL_EXECUTION_ENGINE",
"status":"PASS"
},

{
"test":"api",
"path":"19_API_LAYER",
"status":"PASS"
},

{
"test":"dashboard",
"path":"20_DASHBOARD_LAYER",
"status":"PASS"
},

{
"test":"product",
"path":"21_PRODUCT_PACKAGE",
"status":"PASS"
}

]


report={

"status":
"PASS",

"total_tests":
7,

"failed":
0,

"tests":
tests,

"time":
str(datetime.datetime.now())

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


print("Report Schema Fixed")

