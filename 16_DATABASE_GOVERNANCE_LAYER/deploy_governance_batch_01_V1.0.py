# -*- coding: utf-8 -*-

import os
import json
import subprocess
from datetime import datetime


BASE = r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER"


MODULES = [

    "create_database_initializer.py",

    "create_backup_engine.py",

    "create_restore_engine.py",

    "create_version_control_engine.py"

]


def run():


    results=[]


    for module in MODULES:

        path=os.path.join(

            BASE,

            "batch_modules",

            module

        )


        if os.path.exists(path):

            result=subprocess.run(

                [

                    "python",

                    path

                ],

                capture_output=True,

                text=True

            )


            results.append({

                "module":module,

                "status":
                "PASS"
                if result.returncode==0
                else "FAIL",

                "output":
                result.stdout[-300:]

            })


        else:

            results.append({

                "module":module,

                "status":"MISSING"

            })



    report={

        "module":
        "Database Governance Batch Deployment",

        "version":
        "V1.0",

        "status":
        "DEPLOYED",

        "modules":
        len(MODULES),

        "results":
        results,

        "time":
        str(datetime.now())

    }



    report_path=os.path.join(

        BASE,

        "reports",

        "governance_batch_01_deployment_report.json"

    )


    os.makedirs(

        os.path.dirname(report_path),

        exist_ok=True

    )


    with open(

        report_path,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            report,

            f,

            indent=4,

            ensure_ascii=False

        )


    print(json.dumps(

        report,

        indent=4,

        ensure_ascii=False

    ))



if __name__=="__main__":

    run()

