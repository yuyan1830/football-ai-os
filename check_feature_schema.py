import sqlite3

db=r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db"

conn=sqlite3.connect(db)

cur=conn.cursor()

for t in [
"elo_history",
"dixon_coles_history",
"poisson_history",
"xg_features_history"
]:

    print("\nTABLE:",t)

    print(
        cur.execute(
        f"PRAGMA table_info({t})"
        ).fetchall()
    )

conn.close()
