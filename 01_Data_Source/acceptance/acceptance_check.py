# -*- coding:utf-8 -*-

"""
Football AI OS
Data Source Final Acceptance V1.2
"""


import os
import json
import datetime



BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


REPORT = os.path.join(
    BASE_DIR,
    "reports",
    "data_source_acceptance_report.json"
)



CHECK_FILES = [

    "download/data_downloader.py",

    "download/download_history.json",

    "monitor/source_monitor.py",

    "registry/source_registry.py",

    "registry/source_registry.json",

    "pipeline/source_scanner.py",

    "pipeline/source_validator.py",

    "pipeline/pipeline_runner.py"

]



def check_files():

    result=[]


    for file in CHECK_FILES:


        path=os.path.join(
            BASE_DIR,
            file
        )


        result.append(
            {
                "file":file,
                "exists":
                os.path.exists(path)
            }
        )


    return result




def generate_report():

    checks=check_files()


    passed=all(
        x["exists"]
        for x in checks
    )


    report={

        "framework":
        "Football AI OS",

        "module":
        "01_DATA_SOURCE",

        "version":
        "V1.2",


        "time":
        str(datetime.datetime.now()),


        "status":
        "PASS"
        if passed
        else
        "FAILED",


        "checks":
        checks

    }


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


    return report



if __name__=="__main__":


    print("="*60)

    print(
        "Football AI OS"
    )

    print(
        "Data Source Final Acceptance V1.2"
    )

    print("="*60)



    result=generate_report()


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )


    print()

    print(
        "Report:"
    )

    print(
        REPORT
    )