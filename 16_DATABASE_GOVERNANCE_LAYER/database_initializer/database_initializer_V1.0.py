
# -*- coding: utf-8 -*-

import os
import sqlite3
import json
from datetime import datetime


BASE=r"E:ootball_v\database"


def run():

    databases=[

        "match_data.db",

        "feature_store.db",

        "model_store.db"

    ]


    results=[]


    os.makedirs(
        BASE,
        exist_ok=True
    )


    for db in databases:

        path=os.path.join(
            BASE,
            db
        )


        conn=sqlite3.connect(path)

        conn.close()


        results.append(db)



    report={

        "module":
        "Database Initializer",

        "version":
        "V1.0",

        "status":
        "INITIALIZED",

        "databases":
        results,

        "time":
        str(datetime.now())

    }


    report_path=os.path.join(

        r"E:ootball_v_DATABASE_GOVERNANCE_LAYER\database_initializer",

        "initialize_report.json"

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


    print(report)



if __name__=="__main__":

    run()

