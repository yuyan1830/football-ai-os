import sqlite3
import json
from datetime import datetime


DB=r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

conn=sqlite3.connect(DB)

cursor=conn.cursor()


cursor.execute(
    "select name from sqlite_master where type='table'"
)

tables=[x[0] for x in cursor.fetchall()]


result={

    "version":
    "FOOTBALL_AI_OS_V4.0_LEARNING_DATABASE_SCHEMA_AUDIT",

    "time":
    str(datetime.now()),

    "database":
    DB,

    "tables":{}

}


for table in tables:

    cursor.execute(
        f"pragma table_info({table})"
    )

    columns=[]

    for row in cursor.fetchall():

        columns.append(
            {
                "name":row[1],
                "type":row[2]
            }
        )

    result["tables"][table]=columns


conn.close()


print(
    json.dumps(
        result,
        ensure_ascii=False,
        indent=4
    )
)

out=r"E:\football_v\reports\V4_LEARNING_DATABASE_SCHEMA_AUDIT.json"

with open(out,"w",encoding="utf-8") as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=4
    )

