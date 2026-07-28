# -*- coding: utf-8 -*-

"""
Football AI OS Registry API V1.3
"""

import json
import os



BASE_PATH = (
    r"E:\football_v\00_SYSTEM_OS\Registry"
)



MODULE_FILE = os.path.join(
    BASE_PATH,
    "modules.json"
)



def load_modules():

    with open(
        MODULE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def get_module(name):


    modules = load_modules()


    for module in modules:


        if module["Name"] == name:


            return module



    return {

        "Status":
        "NOT_FOUND"

    }



def list_modules():


    modules = load_modules()


    return modules



if __name__=="__main__":


    print(
        "Football AI OS Registry API V1.3"
    )


    print("")


    print(
        get_module(
            "Monitor"
        )
    )