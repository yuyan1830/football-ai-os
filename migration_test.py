import sqlite3

dbs=[
r'E:\football_v\01_DATA_LAYER\database\match_data.db',
r'E:\football_v\02_FEATURE_LAYER\database\feature_store.db',
r'E:\football_v\03_MODEL_LAYER\database\model_store.db'
]

print("==============================")
print("Football AI OS Migration Test")
print("==============================")


for db in dbs:

    conn=sqlite3.connect(db)

    tables=conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    print("")
    print(db)
    print("STATUS: OK")
    print("TABLES:",len(tables))

    for t in tables:
        print(" -",t[0])

    conn.close()
