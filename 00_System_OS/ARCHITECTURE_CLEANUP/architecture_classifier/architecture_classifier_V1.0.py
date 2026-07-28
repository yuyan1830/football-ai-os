
# -*- coding:utf-8 -*-

import os
import json


BASE=r"E:\football_v"


ACTIVE=[
"00_SYSTEM_OS",
"01_DATA_LAYER",
"02_FEATURE_LAYER",
"03_MODEL_LAYER",
"16_DATABASE_GOVERNANCE_LAYER",
"17_MODEL_STORE_LAYER",
"18_MODEL_EXECUTION_ENGINE",
"19_API_LAYER",
"20_DASHBOARD_LAYER",
"21_PRODUCT_PACKAGE"
]


def classify():


    result={

    "ACTIVE":[],
    "LEGACY":[],
    "MIGRATION_REQUIRED":[],
    "DEPRECATED":[]

    }


    for x in os.listdir(BASE):

        path=os.path.join(BASE,x)

        if not os.path.isdir(path):
            continue


        if x in ACTIVE:
            result["ACTIVE"].append(x)

        elif x[:2].isdigit():
            result["LEGACY"].append(x)


    print(json.dumps(
    result,
    indent=4,
    ensure_ascii=False
    ))


if __name__=="__main__":
    classify()
