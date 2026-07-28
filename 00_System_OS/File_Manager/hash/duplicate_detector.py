import json
import csv
from collections import defaultdict


REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry.json"
)

REPORT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\reports\duplicate_report.csv"
)



def load_registry():

    with open(
        REGISTRY_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def detect_duplicates(records):

    hash_map = defaultdict(list)


    for item in records:

        sha = item.get("SHA256")

        if sha:

            hash_map[sha].append(item)



    duplicates = []


    for sha, files in hash_map.items():

        if len(files) > 1:

            for file in files:

                duplicates.append({

                    "SHA256": sha,

                    "File_Name":
                        file["File_Name"],

                    "Full_Path":
                        file["Full_Path"],

                    "Category":
                        file["Category"],

                    "Status":
                        "DUPLICATE_CANDIDATE"

                })


    return duplicates



def save_report(data):

    if not data:

        print(
            "No duplicate files found"
        )

        return


    with open(
        REPORT_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:


        writer = csv.DictWriter(
            f,
            fieldnames=data[0].keys()
        )

        writer.writeheader()

        writer.writerows(data)



if __name__ == "__main__":


    print(
        "Football AI OS Duplicate Detector V1.0"
    )


    records = load_registry()


    duplicates = detect_duplicates(
        records
    )


    save_report(
        duplicates
    )


    print(
        "Duplicate scan finished:"
        ,
        len(duplicates),
        "files"
    )