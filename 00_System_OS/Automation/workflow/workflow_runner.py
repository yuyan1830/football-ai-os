import json
import os
from datetime import datetime


# ==============================
# Football AI OS
# Workflow Runner V1.1
# ==============================


WORKFLOW_PATH = (
    r"E:\football_v\00_System_OS"
    r"\Automation\workflow\workflow.json"
)


LOG_DIR = (
    r"E:\football_v\00_System_OS"
    r"\Automation\logs"
)


LOG_PATH = os.path.join(
    LOG_DIR,
    "workflow_run_log.json"
)



# ==============================
# JSON 操作
# ==============================


def load_json(path):

    if not os.path.exists(path):

        raise FileNotFoundError(
            f"File not found: {path}"
        )


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_json(path,data):

    folder = os.path.dirname(path)

    if not os.path.exists(folder):

        os.makedirs(folder)


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



# ==============================
# 日志记录
# ==============================


def create_log():

    return {

        "System":
            "Football AI OS",

        "Module":
            "Workflow Runner",

        "Version":
            "1.1",

        "Start_Time":
            datetime.now().isoformat(),

        "Status":
            "RUNNING",

        "Steps":[]

    }



# ==============================
# 执行 Workflow
# ==============================


def run_workflow(
        workflow_name
):


    workflow_data = load_json(
        WORKFLOW_PATH
    )


    workflow = (
        workflow_data
        ["workflows"]
        [workflow_name]
    )


    log = create_log()


    print(
        "\n=============================="
    )

    print(
        "Football AI OS Workflow Runner V1.1"
    )

    print(
        "Workflow:",
        workflow_name
    )

    print(
        "==============================\n"
    )



    # 核心优化：
    # 强制按照 order 执行

    steps = sorted(
        workflow["steps"],
        key=lambda x:x["order"]
    )



    try:


        for step in steps:


            step_log={


                "Order":
                    step["order"],


                "Name":
                    step["name"],


                "Command":
                    step["command"],


                "Start":
                    datetime.now().isoformat(),


                "Status":
                    "RUNNING"

            }



            print(

                "[RUNNING]",
                step["order"],
                step["name"]

            )



            # =================================
            # 后续这里接真实模块调用
            #
            # scanner.py
            # duplicate_detector_v11.py
            # lifecycle_engine.py
            # version_manager.py
            # archive_manager_v11.py
            #
            # =================================



            step_log["Status"] = (
                "SUCCESS"
            )


            step_log["End"] = (
                datetime.now()
                .isoformat()
            )


            log["Steps"].append(
                step_log
            )



            print(

                "[DONE]",
                step["name"]

            )



        log["Status"] = (
            "COMPLETED"
        )



    except Exception as e:


        log["Status"] = (
            "FAILED"
        )


        log["Error"] = str(e)



    log["End_Time"] = (
        datetime.now()
        .isoformat()
    )


    save_json(
        LOG_PATH,
        log
    )



    print(
        "\nWorkflow Finished"
    )


    print(
        "Log:",
        LOG_PATH
    )



# ==============================
# Main
# ==============================


if __name__=="__main__":


    run_workflow(
        "asset_maintenance"
    )