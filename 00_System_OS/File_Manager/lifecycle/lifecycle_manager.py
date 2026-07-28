import json
import csv
from datetime import datetime


REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry.json"
)

REPORT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\reports\lifecycle_report.csv"
)


STATUS_RULES = {

    "REGISTERED": "File registered in system",

    "VALIDATED": "Hash validation completed",

    "ACTIVE": "File available for system usage",

    "ARCHIVED": "Historical version stored",

    "DEPRECATED": "No longer recommended",

    "DELETED": "Removed after approval"

}



def load_registry():

    with open(
        REGISTRY_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def update_lifecycle(records):

    result = []

    current_time = datetime.now().isoformat()


    for item in records:


        lifecycle_record = {


            "Asset_ID":
                item.get("Asset_ID"),


            "File_Name":
                item.get("File_Name"),


            "Full_Path":
                item.get("Full_Path"),


            "Current_Status":
                "REGISTERED",


            "Last_Check_Time":
                current_time,


            "Lifecycle_Note":
                STATUS_RULES["REGISTERED"]

        }


        result.append(
            lifecycle_record
        )


    return result



def save_report(records):


    with open(
        REPORT_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:


        writer = csv.DictWriter(

            f,

            fieldnames=records[0].keys()

        )


        writer.writeheader()

        writer.writerows(records)



if __name__ == "__main__":


    print(
        "Football AI OS Lifecycle Manager V1.0"
    )


    registry = load_registry()


    lifecycle = update_lifecycle(
        registry
    )


    save_report(
        lifecycle
    )


    print(
        "Lifecycle update completed:",
        len(lifecycle),
        "files"
    )