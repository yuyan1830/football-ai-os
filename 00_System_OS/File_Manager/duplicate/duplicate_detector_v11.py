import json
import os
from datetime import datetime


REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry_v11.json"
)


REPORT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\duplicate\duplicate_report_v11.json"
)



def load_json(path):

    if not os.path.exists(path):
        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_json(path,data):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )



def compare_assets(a,b):


    same_hash = (
        a.get("SHA256")
        ==
        b.get("SHA256")
    )


    same_source = (
        a.get("Source")
        ==
        b.get("Source")
    )


    same_period = (
        a.get("Data_Period")
        ==
        b.get("Data_Period")
    )


    same_version = (
        a.get("Version")
        ==
        b.get("Version")
    )


    if (
        same_hash
        and same_source
        and same_period
        and same_version
    ):

        return "EXACT_DUPLICATE"



    if (
        same_source
        and not same_hash
    ):

        return "VERSION_DIFFERENCE"



    if (
        not same_source
    ):

        return "SOURCE_VARIATION"



    if (
        not same_period
    ):

        return "PERIOD_VARIATION"



    return "UNKNOWN"



def run():


    assets = load_json(
        REGISTRY_PATH
    )


    report=[]


    checked=set()


    for i,a in enumerate(assets):

        for j,b in enumerate(assets):

            if i>=j:
                continue


            key=f"{i}-{j}"


            if key in checked:
                continue


            checked.add(key)


            result = compare_assets(
                a,b
            )


            if result!="UNKNOWN":


                report.append({

                    "Asset_A":
                        a.get("Asset_ID"),


                    "Asset_B":
                        b.get("Asset_ID"),


                    "Result":
                        result,


                    "Time":
                        datetime.now().isoformat()

                })


    save_json(
        REPORT_PATH,
        report
    )


    print(
        "Duplicate Detector V1.1 completed:",
        len(report),
        "relations"
    )



if __name__=="__main__":

    print(
        "Football AI OS Duplicate Detector V1.1"
    )

    run()