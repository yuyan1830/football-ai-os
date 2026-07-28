import sqlite3
import json
import os
import datetime


DB_PATH = r"E:\FOOTBALL_V\data\football.db"


result = {

    "version":
    "DATA_SCHEMA_VALIDATION_V4.0",

    "time":
    str(datetime.datetime.now()),

    "database":
    DB_PATH,

    "status":
    "CHECKING"

}


conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()


# 数据库表检查

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
)

tables = [
    x[0] for x in cursor.fetchall()
]


result["tables"] = tables


print("="*70)

print("Football AI OS V4.0")

print("DATABASE TABLE CHECK")

print("="*70)


print("Tables:")

for t in tables:

    print(t)



# matches_clean检查

if "matches_clean" in tables:


    cursor.execute(
        "PRAGMA table_info(matches_clean)"
    )


    columns=[]

    for row in cursor.fetchall():

        columns.append(row[1])


    result["matches_clean_columns"]=columns


    print()

    print("matches_clean columns:")

    for c in columns:

        print(c)



    cursor.execute(
        "SELECT COUNT(*) FROM matches_clean"
    )


    count=cursor.fetchone()[0]


    result["matches_clean_count"]=count


    print()

    print(
        "matches_clean count:",
        count
    )


    cursor.execute(
        "SELECT * FROM matches_clean LIMIT 1"
    )


    sample=cursor.fetchone()


    result["sample"]=sample


    print()

    print("Sample:")

    print(sample)



else:

    result["error"]="matches_clean not found"



conn.close()


result["status"]="COMPLETE"


out=r"E:\FOOTBALL_V\99_DOCUMENTATION\MODEL_DATA_SNAPSHOT_V4.0\DATA_SCHEMA_VALIDATION_V4.0.json"


with open(
    out,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False,
        default=str
    )


print()

print("="*70)

print("SCHEMA VALIDATION COMPLETE")

print(out)

print("="*70)

