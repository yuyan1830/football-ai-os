import os
import json
import datetime
import sqlite3


ROOT=r"E:\FOOTBALL_V"


DB_PATH=os.path.join(
    ROOT,
    "data",
    "football.db"
)


snapshot={

    "version":
    "MODEL_DATA_SNAPSHOT_V4.0",

    "time":
    str(datetime.datetime.now()),

    "database":

    {
        "path":
        DB_PATH,

        "exists":
        os.path.exists(DB_PATH)

    },

    "tables":
    {},

    "training_mode":
    "TIME_SEQUENCE",

    "status":
    "READY"

}



if os.path.exists(DB_PATH):

    try:

        conn=sqlite3.connect(DB_PATH)

        cursor=conn.cursor()


        cursor.execute(
            "SELECT COUNT(*) FROM matches_clean"
        )

        snapshot["tables"]["matches_clean"]=cursor.fetchone()[0]


        cursor.execute(
            "PRAGMA table_info(matches_clean)"
        )


        columns=[]

        for row in cursor.fetchall():

            columns.append(row[1])


        snapshot["training_features_reference"]=columns


        conn.close()


    except Exception as e:

        snapshot["error"]=str(e)



out=os.path.join(

    ROOT,

    "99_DOCUMENTATION",

    "MODEL_DATA_SNAPSHOT_V4.0",

    "MODEL_DATA_SNAPSHOT_V4.0.json"

)



with open(

    out,

    "w",

    encoding="utf-8"

) as f:


    json.dump(

        snapshot,

        f,

        indent=4,

        ensure_ascii=False

    )


print("="*70)

print("Football AI OS V4.0")

print("MODEL DATA SNAPSHOT COMPLETE")

print("="*70)

print(json.dumps(

snapshot,

indent=4,

ensure_ascii=False

))

