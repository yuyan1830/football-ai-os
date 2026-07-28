import sqlite3


dbs=[
r"E:\football_v\01_DATA_LAYER\database\match_data.db",
r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db",
r"E:\football_v\03_MODEL_LAYER\database\model_store.db"
]


for db in dbs:

    print("\n================================")
    print(db)
    print("================================")

    conn=sqlite3.connect(db)

    tables=conn.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    for t in tables:
        print(t[0])

    conn.close()

