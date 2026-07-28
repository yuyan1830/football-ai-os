# -*- coding: utf-8 -*-

import os
import subprocess
from datetime import datetime



BASE = r"E:\football_v\00_SYSTEM_OS"



CHECK_SCRIPT = (
    BASE +
    r"\Bootstrap\system_check.py"
)



LOG_FILE = (
    BASE +
    r"\Bootstrap\deployment_log.txt"
)



def write_log(text):

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(text+"\n")



def run():

    print("")
    print(
        "=============================="
    )

    print(
        "Football AI OS Deployment V1.2"
    )

    print(
        "=============================="
    )


    write_log(
        "Deployment Start "
        +
        datetime.now().isoformat()
    )


    modules = [

        "File_Manager",

        "Automation",

        "Monitor",

        "Recovery",

        "Bootstrap"

    ]


    print("")


    for m in modules:


        path = os.path.join(
            BASE,
            m
        )


        if os.path.exists(path):

            status="OK"

        else:

            os.makedirs(path)

            status="CREATED"



        print(
            "[{}] {}".format(
                status,
                m
            )
        )


        write_log(
            m+":"+status
        )



    print("")

    print(
        "[RUNNING] System Check"
    )


    subprocess.run(
        [
            "python",
            CHECK_SCRIPT
        ]
    )


    write_log(
        "Deployment Complete"
    )


    print("")

    print(
        "DEPLOYMENT COMPLETE"
    )



if __name__=="__main__":

    run()