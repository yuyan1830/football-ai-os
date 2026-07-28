import sqlite3

db=r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"

conn=sqlite3.connect(db)

cur=conn.cursor()

print("MODEL STORE TABLES")

for row in cur.execute("select name from sqlite_master where type='table'"):
    print(row[0])

conn.close()
