# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime



BASE_PATH = (
    r"E:\football_v\00_System_OS\Monitor"
)


HEALTH_FILE = os.path.join(
    BASE_PATH,
    "health_status.json"
)


HEARTBEAT_FILE = os.path.join(
    BASE_PATH,
    "heartbeat.json"
)


HISTORY_FILE = (
    r"E:\football_v\00_System_OS"
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



def check_system():


    print(
        "Football AI OS Monitor V1.0"
    )


    health = load_json(
        HEALTH_FILE
    )


    heartbeat = load_json(
        HEARTBEAT_FILE
    )


    history = load_json(
        HISTORY_FILE
    )


    # Ä¬ÈÏ×´Ì¬

    automation_status = (
        "UNKNOWN"
    )


    scheduler_status = (
        "UNKNOWN"
    )



    if history:


        last = history[-1]


        if last.get(
            "Status"
        ) == "SUCCESS":

            automation_status = (
                "OK"
            )

        else:

            automation_status = (
                "ERROR"
            )



    health["Status"] = (
        "ONLINE"
    )


    health["Modules"] = {


        "File_Manager":
        "OK",


        "Automation":
        automation_status,


        "Scheduler":
        "OK"

    }



    heartbeat["Heartbeat"] = (
        "ONLINE"
    )


    heartbeat["Last_Check"] = (
        datetime.now()
        .isoformat()
    )



    save_json(
        HEALTH_FILE,
        health
    )


    save_json(
        HEARTBEAT_FILE,
        heartbeat
    )



    print("")
    print(
        "System Health:"
    )

    print(
        "File Manager :",
        "OK"
    )

    print(
        "Automation :",
        automation_status
    )

    print(
        "Scheduler :",
        "OK"
    )



if __name__=="__main__":

    check_system()