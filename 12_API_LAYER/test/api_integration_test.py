
import sqlite3
import json


db=r"E:\football_v\12_API_LAYER\runtime\api_runtime.db"


conn=sqlite3.connect(db)

cur=conn.cursor()


tables=[
x[0]
for x in
cur.execute(
"select name from sqlite_master where type='table'"
)
]


print("TABLES")

for t in tables:
    print(t)



print("DATABASE TEST PASS")


