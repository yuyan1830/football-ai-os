import os
import hashlib
import json
import csv
from datetime import datetime


ROOT_PATH = r"E:\football_v"

REGISTRY_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\registry\file_registry.json"
)

REPORT_PATH = (
    r"E:\football_v\00_System_OS\File_Manager"
    r"\reports\file_inventory.csv"
)


EXCLUDE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    "temp",
    "cache"
}


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:

            while True:

                data = f.read(1024 * 1024)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except Exception:

        return None



def classify_file(extension):

    data_types = [
        ".csv",
        ".json",
        ".xlsx",
        ".xls",
        ".xml"
    ]

    code_types = [
        ".py",
        ".ps1",
        ".bat"
    ]

    config_types = [
        ".yaml",
        ".yml",
        ".ini",
        ".conf"
    ]

    model_types = [
        ".pkl",
        ".pt",
        ".onnx"
    ]


    if extension in data_types:
        return "DATA"

    if extension in code_types:
        return "CODE"

    if extension in config_types:
        return "CONFIG"

    if extension in model_types:
        return "MODEL"

    return "UNKNOWN"



def scan_files():

    inventory = []

    asset_id = 1


    for root, dirs, files in os.walk(ROOT_PATH):

        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDE_DIRS
        ]


        for file in files:

            full_path = os.path.join(
                root,
                file
            )


            try:

                stat = os.stat(full_path)

                extension = (
                    os.path.splitext(file)[1]
                    .lower()
                )


                record = {

                    "Asset_ID":
                        f"FA-{asset_id:06d}",

                    "File_Name":
                        file,

                    "Full_Path":
                        full_path,

                    "Extension":
                        extension,

                    "Category":
                        classify_file(extension),

                    "Size":
                        stat.st_size,

                    "Create_Time":
                        datetime.fromtimestamp(
                            stat.st_ctime
                        ).isoformat(),

                    "Modify_Time":
                        datetime.fromtimestamp(
                            stat.st_mtime
                        ).isoformat(),

                    "SHA256":
                        calculate_hash(
                            full_path
                        ),

                    "Status":
                        "REGISTERED"

                }


                inventory.append(record)

                asset_id += 1


            except Exception:

                pass


    return inventory



def save_results(records):


    with open(
        REGISTRY_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            records,
            f,
            indent=4,
            ensure_ascii=False
        )



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
        "Football AI OS File Scanner V1.0"
    )


    result = scan_files()


    save_results(result)


    print(
        "Scan completed:"
        ,
        len(result),
        "files"
    )