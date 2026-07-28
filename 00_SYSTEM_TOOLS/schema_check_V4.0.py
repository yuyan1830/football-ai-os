import sqlite3
import json
import os


DB=r"E:\FOOTBALL_V\data\football.db"


conn=sqlite3.connect(DB)

cursor=conn.cursor()


print("="*60)

print("DATABASE SCHEMA CHECK V4.0")

print("="*60)


cursor.execute(
"PRAGMA table_info(matches_clean)"
)


columns=[]

for row in cursor.fetchall():

    columns.append(row[1])


print("字段:")

for c in columns:

    print(c)



cursor.execute(
"SELECT COUNT(*) FROM matches_clean"
)


count=cursor.fetchone()[0]


print()

print("比赛数量:",count)



cursor.execute(
"SELECT * FROM matches_clean LIMIT 1"
)


row=cursor.fetchone()


print()

print("第一条数据:")

print(row)



conn.close()


result={

"table":
"matches_clean",

"count":
count,

"columns":
columns,

"sample":
row

}


with open(
"E:\FOOTBALL_V\99_DOCUMENTATION\MODEL_DATA_SNAPSHOT_V4.0\schema_check_V4.0.json",
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


