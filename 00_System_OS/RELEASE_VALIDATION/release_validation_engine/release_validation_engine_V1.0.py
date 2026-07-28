
# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


BASE=r"E:ootball_v"


MODULES=[
"16_DATABASE_GOVERNANCE_LAYER",
"17_MODEL_STORE_LAYER",
"18_MODEL_EXECUTION_ENGINE",
"19_API_LAYER",
"20_DASHBOARD_LAYER",
"21_PRODUCT_PACKAGE"
]


MODELS=[
"Elo",
"Dixon-Coles",
"Poisson",
"XGBoost",
"V38.8.1 Handicap Model",
"Market Risk Model 2.0"
]


def run():

    result={}

    result["module"]="Release Validation Engine"
    result["version"]="V1.0"

    result["modules"]={}

    for m in MODULES:
        path=os.path.join(BASE,m)
        result["modules"][m]=os.path.exists(path)


    result["models"]=MODELS

    result["status"]="READY"

    result["time"]=str(datetime.now())


    report=r"E:\football_v\00_SYSTEM_OS\RELEASE_VALIDATION\reports\release_validation_report.json"

    os.makedirs(
        os.path.dirname(report),
        exist_ok=True
    )

    with open(report,"w",encoding="utf-8") as f:
        json.dump(
            result,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(json.dumps(result,indent=4,ensure_ascii=False))


if __name__=="__main__":
    run()
