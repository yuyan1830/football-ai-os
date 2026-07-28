# -*- coding: utf-8 -*-

"""
Football AI OS Registry Manager V1.0
"""

import json
import os
from datetime import datetime



BASE_PATH = (
    r"E:\football_v\00_SYSTEM_OS\Registry"
)



REGISTRY_FILE = os.path.join(
    BASE_PATH,
    "registry.json"
)



LOG_FILE = os.path.join(
    BASE_PATH,
    "registry_log.json"
)



MODULES = [

    {
        "ID":
        "FILE_MANAGER_001",

        "Name":
        "File Manager",

        "Version":
        "1.0",

        "Layer":
        "Core System",

        "Status":
        "ONLINE"
    },


    {
        "ID":
        "AUTOMATION_001",

        "Name":
        "Automation",

        "Version":
        "1.0",

        "Layer":
        "Automation",

        "Status":
        "ONLINE"
    },


    {
        "ID":
        "MONITOR_001",

        "Name":
        "Monitor",

        "Version":
        "1.0",

        "Layer":
        "System Control",

        "Status":
        "ONLINE"
    },


    {
        "ID":
        "RECOVERY_001",

        "Name":
        "Recovery",

        "Version":
        "1.0",

        "Layer":
        "Self Healing",

        "Status":
        "ONLINE"
    }

]



def save(path,data):

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



def load(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def register():


    print(
        "Football AI OS Registry V1.0"
    )


    registry = load(
        REGISTRY_FILE
    )


    registry["Modules"] = MODULES


    save(
        REGISTRY_FILE,
        registry
    )


    log = {

        "Time":
        datetime.now().isoformat(),

        "Action":
        "REGISTER_MODULES",

        "Count":
        len(MODULES)

    }


    save(
        LOG_FILE,
        [log]
    )


    for m in MODULES:

        print(
            "[REGISTERED]",
            m["Name"]
        )



    print("")
    print(
        "Registry Update Complete"
    )



if __name__=="__main__":

    register()