import os
import json
from datetime import datetime


PROJECT_ROOT = r"E:\football_v"

OUTPUT_FILE = "framework_migration_report.json"


SCAN_EXTENSIONS = {
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".sql"
}


KEYWORDS = [
    "utils",
    "helper",
    "common",
    "tool",
    "logger",
    "validator",
    "exception",
    "file",
]


def get_file_info(path):

    stat = os.stat(path)

    return {
        "file": path,
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(
            stat.st_mtime
        ).isoformat()
    }


def scan_project():

    result = {
        "project": PROJECT_ROOT,
        "scan_time": datetime.now().isoformat(),
        "files": [],
        "possible_common": []
    }


    for root, dirs, files in os.walk(PROJECT_ROOT):

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext not in SCAN_EXTENSIONS:
                continue


            full_path = os.path.join(
                root,
                file
            )


            info = get_file_info(
                full_path
            )


            result["files"].append(
                info
            )


            lower_name = file.lower()


            if any(
                key in lower_name
                for key in KEYWORDS
            ):

                result["possible_common"].append(
                    info
                )


    return result



def main():

    report = scan_project()


    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("======================")
    print("Football AI OS Scanner")
    print("======================")

    print(
        "Files:",
        len(report["files"])
    )

    print(
        "Possible Common Files:",
        len(report["possible_common"])
    )

    print(
        "Output:",
        OUTPUT_FILE
    )



if __name__ == "__main__":

    main()