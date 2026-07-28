# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime



BASE_PATH = r"E:\football_v\00_SYSTEM_OS"



MODULES = [

    "File_Manager",

    "Automation",

    "Monitor",

    "Recovery",

    "Bootstrap"

]



LOG_FILE = (
    BASE_PATH +
    r"\Bootstrap\bootstrap_log.json"
)



def create_structure():

    print(
        "Football AI OS Bootstrap V1.0"
    )


    log = {

        "System":
        "Football AI OS",

        "Start":
        datetime.now().isoformat(),

        "Modules":[]

    }



    for module in MODULES:


        path = os.path.join(
            BASE_PATH,
            module
        )


        if not os.path.exists(path):

            os.makedirs(path)


            status = "CREATED"

        else:

            status = "EXISTS"



        print(
            "[",
            status,
            "]",
            module
        )


        log["Modules"].append({

            "Name":
            module,

            "Status":
            status

        })



    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            log,
            f,
            indent=4,
            ensure_ascii=False
        )



    print("")
    print(
        "Bootstrap Finished"
    )



if __name__=="__main__":

    create_structure()