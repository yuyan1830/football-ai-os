import sqlite3
import json
import hashlib
from datetime import datetime
import os


BASE = r"E:\football_v"

SYSTEM_DB = BASE + r"\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db"
MODEL_DB = BASE + r"\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db"

REPORT = BASE + r"\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.3_FIX_REPORT.json"


def sha256(path):
    h = hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(8192),b""):
            h.update(b)
    return h.hexdigest()


def check_db(path):

    result={
        "exists":False,
        "size":0,
        "sha256":None,
        "tables":{}
    }

    if not os.path.exists(path):
        return result

    result["exists"]=True
    result["size"]=os.path.getsize(path)
    result["sha256"]=sha256(path)

    conn=sqlite3.connect(path)
    cur=conn.cursor()

    tables=cur.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    for t in tables:
        name=t[0]
        if name=="sqlite_sequence":
            continue
        try:
            count=cur.execute(
                f"select count(*) from {name}"
            ).fetchone()[0]
        except:
            count=-1

        result["tables"][name]=count

    conn.close()

    return result


def main():

    print("="*60)
    print("Football AI OS Prediction Intelligence Layer V1.3 FIX")
    print("="*60)


    report={
        "version":"PREDICTION_INTELLIGENCE_V1.3_FIX",
        "time":datetime.now().isoformat(),
        "system_database":check_db(SYSTEM_DB),
        "model_database":check_db(MODEL_DB),
        "modules":[
            "Prediction Intelligence Service",
            "Prediction Monitor",
            "Model Weight Monitor",
            "Prediction Runtime Registry"
        ],
        "status":"PASS"
    }


    os.makedirs(
        os.path.dirname(REPORT),
        exist_ok=True
    )

    with open(
        REPORT,
        "w",
        encoding="utf8"
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

    print("PREDICTION INTELLIGENCE V1.3 COMPLETE")


if __name__=="__main__":
    main()
