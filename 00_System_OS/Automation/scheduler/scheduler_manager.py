# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime



CONFIG_PATH = (
    r"E:\football_v\00_System_OS"
    r"\Automation\scheduler"
    r"\scheduler_config.json"
)



LOG_PATH = (
    r"E:\football_v\00_System_OS"
    r"\Automation\logs"
    r"\scheduler_log.json"
)



def load_config():

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def write_log(data):

    if not os.path.exists(
        os.path.dirname(LOG_PATH)
    ):

        os.makedirs(
            os.path.dirname(LOG_PATH)
        )


    with open(
        LOG_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def run():

    config = load_config()


    print(
        "Football AI OS Scheduler V1.0"
    )


    log = {

        "Module":
        "Scheduler",

        "Version":
        "1.0",

        "Start":
        datetime.now().isoformat(),

        "Tasks":[]

    }



    for task in config["tasks"]:


        if task["Enabled"]:


            print(
                "[REGISTERED]",
                task["Name"]
            )


            log["Tasks"].append({

                "Name":
                task["Name"],

                "Time":
                task["Time"],

                "Script":
                task["Script"],

                "Status":
                "READY"

            })


    write_log(log)


    print(
        "Scheduler configuration loaded"
    )



if __name__=="__main__":

    run()