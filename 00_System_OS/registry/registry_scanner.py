# -*- coding: utf-8 -*-

"""
Football AI OS Registry Scanner V1.1
"""

import os
import json
from datetime import datetime



SYSTEM_ROOT = (
    r"E:\football_v\00_SYSTEM_OS"
)



REGISTRY_FILE = (
    SYSTEM_ROOT +
    r"\Registry\registry.json"
)



LOG_FILE = (
    SYSTEM_ROOT +
    r"\Registry\registry_log.json"
)



IGNORE = [

    "Registry"

]



def load(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



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



def scan():


    print(
        "Football AI OS Registry Scanner V1.1"
    )


    registry = load(
        REGISTRY_FILE
    )


    modules=[]


    for item in os.listdir(
        SYSTEM_ROOT
    ):


        path=os.path.join(
            SYSTEM_ROOT,
            item
        )


        if os.path.isdir(path):


            if item not in IGNORE:


                module={

                    "ID":
                    item.upper()
                    +"_001",


                    "Name":
                    item,


                    "Version":
                    "UNKNOWN",


                    "Status":
                    "DISCOVERED",


                    "Detected":
                    datetime.now()
                    .isoformat()

                }


                modules.append(
                    module
                )


                print(
                    "[FOUND]",
                    item
                )



    registry["Modules"]=modules


    save(
        REGISTRY_FILE,
        registry
    )



    log={

        "Time":
        datetime.now().isoformat(),

        "Action":
        "AUTO_DISCOVERY",

        "Modules":
        len(modules)

    }



    save(
        LOG_FILE,
        [log]
    )


    print("")
    print(
        "Registry Discovery Complete"
    )



if __name__=="__main__":

    scan()