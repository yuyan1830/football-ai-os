import sqlite3
import os
import json
import hashlib
from datetime import datetime


BASE = r"E:\football_v"


DATABASES = {

    "football_ai_os":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "01_DATA_LAYER",
        "database",
        "football_ai_os.db"
    ),

    "match_data":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "01_DATA_LAYER",
        "database",
        "match_data.db"
    ),

    "feature_store":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "02_FEATURE_LAYER",
        "database",
        "feature_store.db"
    ),

    "model_store":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "03_MODEL_LAYER",
        "database",
        "model_store.db"
    )
}


REPORT = os.path.join(
    BASE,
    "99_Documentation",
    "reports",
    "DATABASE_SYSTEM_VALIDATION_V2.2.4_REPORT.json"
)


REQUIRED_SYSTEM_TABLES = [

    "system_registry",
    "database_registry",
    "model_registry",
    "runtime_registry",
    "task_registry"

]


def sha256(path):

    if not os.path.exists(path):
        return None

    h=hashlib.sha256()

    with open(path,"rb") as f:

        for chunk in iter(
            lambda:f.read(8192),
            b""
        ):
            h.update(chunk)

    return h.hexdigest()



def inspect_database(name,path):

    result={

        "name":name,
        "path":path,
        "exists":False,
        "size":0,
        "sha256":None,
        "tables":{},
        "status":"FAIL"

    }


    if not os.path.exists(path):
        return result


    result["exists"]=True
    result["size"]=os.path.getsize(path)
    result["sha256"]=sha256(path)


    conn=sqlite3.connect(path)

    cur=conn.cursor()


    tables=[]

    for row in cur.execute(
        "select name from sqlite_master where type='table'"
    ):
        tables.append(row[0])


    for t in tables:

        if t=="sqlite_sequence":
            continue

        try:

            count=cur.execute(
                f"select count(*) from '{t}'"
            ).fetchone()[0]

            result["tables"][t]=count

        except:

            result["tables"][t]="ERROR"


    conn.close()


    result["status"]="PASS"


    return result



def validate():


    print("="*60)

    print(
        "Football AI OS Database System Validation V2.2.4"
    )

    print("="*60)



    report={

        "version":
        "DATABASE_SYSTEM_VALIDATION_V2.2.4",

        "time":
        datetime.now().isoformat(),

        "databases":{}

    }


    for name,path in DATABASES.items():

        print("Checking:",name)

        report["databases"][name]=inspect_database(
            name,
            path
        )


    system=report["databases"]["football_ai_os"]


    missing=[]

    for t in REQUIRED_SYSTEM_TABLES:

        if t not in system["tables"]:
            missing.append(t)



    if missing:

        system["status"]="FAIL"

        system["missing_tables"]=missing


    else:

        system["status"]="PASS"


    os.makedirs(
        os.path.dirname(REPORT),
        exist_ok=True
    )


    with open(
        REPORT,
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

    validate()

    print()

    print(
        "DATABASE SYSTEM VALIDATION COMPLETE"
    )

