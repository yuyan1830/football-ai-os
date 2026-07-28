import os
import json
from datetime import datetime


# 项目根目录
ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


# 初始化报告
REPORT = {
    "created": [],
    "skipped": [],
    "failed": [],
    "time": ""
}


# 需要创建的目录
DIRECTORIES = [

    "00_System_OS/01_DATA_LAYER/core",

    "00_System_OS/01_DATA_LAYER/core",

    "00_System_OS/01_DATA_LAYER/core/logger",

    "00_System_OS/01_DATA_LAYER/core/exception",

    "00_System_OS/01_DATA_LAYER/core/validator",

    "00_System_OS/01_DATA_LAYER/core/database",

    "00_System_OS/01_DATA_LAYER/core/file_service",

    "00_System_OS/01_DATA_LAYER/core/config_loader",

    "00_System_OS/01_DATA_LAYER/core/datetime_service",

    "00_System_OS/01_DATA_LAYER/core/hash_service",

    "97_TESTS/core",

    "99_DOCUMENTATION/reports"

]


# 需要创建的初始化文件
FILES = {

"00_System_OS/01_DATA_LAYER/core/__init__.py":
"# Common Services Package\n",

"00_System_OS/01_DATA_LAYER/core/logger/__init__.py":
"# Logger Service\n",

"00_System_OS/01_DATA_LAYER/core/exception/__init__.py":
"# Exception Service\n",

"00_System_OS/01_DATA_LAYER/core/validator/__init__.py":
"# Validator Service\n"

}



def create_directory(path):

    full_path = os.path.join(
        ROOT,
        path
    )


    if os.path.exists(full_path):

        print(
            "[跳过目录]",
            path
        )

        REPORT["skipped"].append(path)

        return


    os.makedirs(full_path)

    print(
        "[创建目录]",
        path
    )

    REPORT["created"].append(path)



def create_file(path, content):

    full_path = os.path.join(
        ROOT,
        path
    )


    if os.path.exists(full_path):

        print(
            "[跳过文件]",
            path
        )

        REPORT["skipped"].append(path)

        return


    with open(
        full_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


    print(
        "[创建文件]",
        path
    )

    REPORT["created"].append(path)



def save_report():

    REPORT["time"] = datetime.now().isoformat()


    report_path = os.path.join(
        ROOT,
        "99_DOCUMENTATION",
        "reports",
        "framework_init_report.json"
    )


    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            REPORT,
            f,
            indent=4,
            ensure_ascii=False
        )



def main():

    print("====================")
    print("Football AI OS Initializer")
    print("====================")


    for d in DIRECTORIES:

        create_directory(d)


    for file,content in FILES.items():

        create_file(
            file,
            content
        )


    save_report()


    print("====================")
    print("完成")
    print(REPORT)
    print("====================")



if __name__ == "__main__":

    main()
