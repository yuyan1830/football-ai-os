# -*- coding: utf-8 -*-

import os


ROOT = r"E:\football_v"

OUTPUT = r"E:\football_v\99_DOCUMENTATION\checkpoints\Architecture_Cleanup_Audit_V1.0.txt"


KEYWORDS = [

    "decision",
    "prediction",
    "fusion",
    "engine",
    "service",
    "router",
    "executor",
    "report"

]


IGNORE = [

    ".git",
    "__pycache__",
    ".pytest_cache"

]


RESULT = []


def scan():

    for root, dirs, files in os.walk(ROOT):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]


        for file in files:

            if not file.endswith(
                (".py",".json",".yaml",".yml")
            ):
                continue


            path=os.path.join(
                root,
                file
            )


            name=file.lower()


            hit=[]


            for k in KEYWORDS:

                if k in name:

                    hit.append(k)


            if hit:

                RESULT.append(
                    {
                        "file":path,
                        "keyword":hit
                    }
                )


def write_report():

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:


        f.write(
"""
Football AI OS Ω+

Architecture Cleanup Audit V1.0


扫描目标:

E:\\football_v


关键词:

decision
prediction
fusion
engine
service
router
executor
report


==============================


"""
        )


        for item in RESULT:

            f.write(
                "\n"
                + item["file"]
                + "\n"
            )

            f.write(
                "关键词:"
                +
                ",".join(
                    item["keyword"]
                )
                +
                "\n"
            )



if __name__=="__main__":

    scan()

    write_report()


    print("==============================")
    print("Architecture Cleanup Audit")
    print("==============================")
    print("扫描文件:",len(RESULT))
    print("报告:")
    print(OUTPUT)

