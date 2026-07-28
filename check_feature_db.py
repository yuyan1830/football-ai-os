import sqlite3

db=r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"

conn=sqlite3.connect(db)

cur=conn.cursor()

print("FEATURE STORE TABLES")

for row in cur.execute("select name from sqlite_master where type='table'"):
    print(row[0])

conn.close()
