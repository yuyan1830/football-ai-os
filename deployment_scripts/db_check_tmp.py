import sqlite3

db=r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db"

conn=sqlite3.connect(db)
cur=conn.cursor()

rows=cur.execute(
    "select name from sqlite_master where type='table'"
).fetchall()

print("==============================")
print("DATABASE TABLE CHECK")
print("==============================")

for r in rows:
    print(r[0])

conn.close()
