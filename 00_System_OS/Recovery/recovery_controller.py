# -*- coding: utf-8 -*-

import json
import os
import subprocess
from datetime import datetime



HEALTH_FILE = (
    r"E:\football_v\00_SYSTEM_OS"
    r"\Monitor\health_status.json"
)


TASK_MANAGER = (
    r"E:\football_v\00_SYSTEM_OS"
    r"\Automation\task_manager"
    r"\task_manager.py"
)


LOG_FILE = (
    r"E:\football_v\00_SYSTEM_OS"
    r"\Recovery\recovery_log.json"
)



def load_json(path):

    if not os.path.exists(path):

        return {}

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
            indent=4,
            ensure_ascii=False
        )



def main():


    print(
        "Football AI OS Recovery Controller V1.0"
    )


    health = load_json(
        HEALTH_FILE
    )


    logs = load_json(
        LOG_FILE
    )


    status = health.get(
        "Modules",
        {}
    ).get(
        "Automation",
        "UNKNOWN"
    )


    record = {

        "Time":
        datetime.now().isoformat(),

        "Before":
        status

    }



    if status == "ERROR":


        print(
            "[RECOVERY REQUIRED]"
        )


        subprocess.run(
            [
                "python",
                TASK_MANAGER
            ]
        )


        record["Action"] = (
            "TASK_RESTART"
        )


        record["Result"] = (
            "EXECUTED"
        )


    else:


        print(
            "[SYSTEM NORMAL]"
        )


        record["Action"] = (
            "NONE"
        )


        record["Result"] = (
            "SKIPPED"
        )



    logs.append(
        record
    )


    save_json(
        LOG_FILE,
        logs
    )



if __name__ == "__main__":

    main()