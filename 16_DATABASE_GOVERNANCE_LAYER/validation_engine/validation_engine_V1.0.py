# -*- coding: utf-8 -*-

import os
import sqlite3
import json
from datetime import datetime


BASE = r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER\validation_engine"

DATABASE_PATH = r"E:\football_v\database"


def validate_database(db):

    path = os.path.join(
        DATABASE_PATH,
        db
    )

    result = {
        "database": db,
        "exists": os.path.exists(path),
        "integrity": "NOT_CHECKED"
    }

    if result["exists"]:

        try:

            conn = sqlite3.connect(path)

            cursor = conn.cursor()

            cursor.execute(
                "PRAGMA integrity_check;"
            )

            result["integrity"] = cursor.fetchone()[0]

            conn.close()

        except Exception as e:

            result["integrity"] = str(e)

    return result



def run():

    databases = [

        "match_data.db",

        "feature_store.db",

        "model_store.db"

    ]


    results=[]

    failed=0


    for db in databases:

        result = validate_database(db)

        results.append(result)

        if not result["exists"]:

            failed += 1



    report={

        "module":
        "Validation Engine",

        "version":
        "V1.0",

        "status":
        "PASS" if failed == 0 else "WAITING",

        "databases":
        len(results),

        "failed":
        failed,

        "results":
        results,

        "time":
        str(datetime.now())

    }


    report_path=os.path.join(

        BASE,

        "reports",

        "validation_report.json"

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


    print(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )
    )


if __name__=="__main__":

    run()

