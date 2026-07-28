# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime



BASE_PATH = (
    r"E:\football_v\00_SYSTEM_OS\Recovery"
)


POLICY_FILE = os.path.join(
    BASE_PATH,
    "recovery_policy.json"
)


LOG_FILE = os.path.join(
    BASE_PATH,
    "recovery_log.json"
)


TASK_HISTORY = (
    r"E:\football_v\00_SYSTEM_OS"
    r"\Automation\task_manager"
    r"\task_history.json"
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



def recovery_check():


    print(
        "Football AI OS Recovery V1.0"
    )


    history = load_json(
        TASK_HISTORY
    )


    logs = load_json(
        LOG_FILE
    )


    if not history:


        print(
            "No task history"
        )

        return



    last = history[-1]


    record = {

        "Time":
        datetime.now().isoformat(),

        "Target":
        last.get(
            "Name"
        ),

        "Status":
        last.get(
            "Status"
        )

    }



    if last.get(
        "Status"
    ) == "SUCCESS":


        record["Action"] = (
            "NONE"
        )


        print(
            "[OK] No Recovery Needed"
        )


    else:


        record["Action"] = (
            "RETRY_REQUIRED"
        )


        print(
            "[RECOVERY]",
            "Retry Task"
        )



    logs.append(
        record
    )


    save_json(
        LOG_FILE,
        logs
    )



if __name__=="__main__":

    recovery_check()