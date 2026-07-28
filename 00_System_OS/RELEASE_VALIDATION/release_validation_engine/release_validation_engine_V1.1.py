# -*- coding:utf-8 -*-

import os
import json
from datetime import datetime


BASE=r"E:\football_v"


def scan_modules():

    result={}

    for item in os.listdir(BASE):

        path=os.path.join(BASE,item)

        if os.path.isdir(path):

            if item[:2].isdigit():

                result[item]=True


    return result



def run():

    modules=scan_modules()


    report={

    "module":"Release Validation Engine",

    "version":"V1.1",

    "status":"READY",

    "discovered_modules":modules,

    "module_count":len(modules),

    "time":str(datetime.now())

    }


    report_path=r"E:\football_v\00_SYSTEM_OS\RELEASE_VALIDATION\reports\release_validation_report.json"


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


    print(json.dumps(report,indent=4,ensure_ascii=False))



if __name__=="__main__":
    run()

