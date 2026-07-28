import sqlite3
import os


dbs = [

r"E:\football_v\01_DATA_LAYER\database\match_data.db",

r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"

]


print("="*60)
print("Football AI OS Ω+ V3.2")
print("DATABASE CONNECTION TEST")
print("="*60)


for db in dbs:

    print()
    print("DATABASE:")
    print(db)


    if not os.path.exists(db):

        print("[NOT FOUND]")

        continue


    try:

        conn=sqlite3.connect(db)

        cur=conn.cursor()


        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )


        tables=cur.fetchall()


        print("[OK] CONNECT")

        print("TABLE COUNT:",len(tables))


        for t in tables[:20]:

            print(" -",t[0])


        conn.close()


    except Exception as e:

        print("[FAIL]")
        print(e)


print()
print("="*60)

