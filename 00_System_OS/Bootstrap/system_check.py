# -*- coding: utf-8 -*-

import os
import sys
import json
import subprocess
from datetime import datetime



BASE = r"E:\football_v\00_SYSTEM_OS"



CHECK_LOG = (
    BASE +
    r"\Bootstrap\system_check_log.json"
)



def check_python():

    return {

        "Python":

        sys.version.split()[0]

    }



def check_path(name,path):

    return {

        name:

        "OK"
        if os.path.exists(path)
        else
        "MISSING"

    }



def check_scheduler():

    try:

        result = subprocess.check_output(
            [
                "powershell",
                "-command",
                "Get-ScheduledTask | findstr Football"
            ],
            text=True
        )


        if "Football" in result:

            return {
                "Scheduler":
                "OK"
            }


    except:

        pass


    return {

        "Scheduler":
        "UNKNOWN"

    }



def run_check():


    print(
        "Football AI OS System Check V1.1"
    )


    result = {

        "Time":
        datetime.now().isoformat(),

        "Checks":[]

    }



    checks = []


    checks.append(
        check_python()
    )


    checks.append(
        check_path(
            "File_Manager",
            BASE+r"\File_Manager"
        )
    )


    checks.append(
        check_path(
            "Automation",
            BASE+r"\Automation"
        )
    )


    checks.append(
        check_path(
            "Monitor",
            BASE+r"\Monitor"
        )
    )


    checks.append(
        check_path(
            "Recovery",
            BASE+r"\Recovery"
        )
    )


    checks.append(
        check_scheduler()
    )


    result["Checks"] = checks



    for item in checks:

        print(
            item
        )



    result["Status"]="READY"



    with open(
        CHECK_LOG,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            result,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("")
    print(
        "SYSTEM READY"
    )



if __name__=="__main__":

    run_check()