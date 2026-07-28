# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime


TASK_PATH = (
    r"E:\football_v\00_System_OS"
    r"\Automation\task_manager"
    r"\task_registry.json"
)


HISTORY_PATH = (
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



def run_task(task):


    history = load_json(
        HISTORY_PATH
    )


    record = {

        "Task_ID":
            task["Task_ID"],


        "Name":
            task["Name"],


        "Workflow":
            task["Workflow"],


        "Start_Time":
            datetime.now().isoformat(),


        "Status":
            "RUNNING"

    }


    print(
        "[RUNNING TASK]",
        task["Name"]
    )


    # 后续连接 workflow_runner


    record["Status"] = (
        "SUCCESS"
    )


    record["End_Time"] = (
        datetime.now().isoformat()
    )


    history.append(
        record
    )


    save_json(
        HISTORY_PATH,
        history
    )


    print(
        "[TASK SUCCESS]",
        task["Name"]
    )



def main():


    data = load_json(
        TASK_PATH
    )


    tasks = data.get(
        "tasks",
        []
    )


    print(
        "Football AI OS Task Manager V1.0"
    )


    for task in tasks:


        if task["Enabled"]:


            run_task(
                task
            )



if __name__=="__main__":

    main()