# -*- coding:utf-8 -*-

import sqlite3


DB = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


tables = [
    "elo_history",
    "dixon_coles_history",
    "poisson_history",
    "team_form_history",
    "fatigue_history",
    "home_away_history",
    "xg_features_history"
]


print("="*70)
print("Football AI OS Ω+ V3.2")
print("MODEL STORE HISTORY VALIDATION")
print("="*70)


conn = sqlite3.connect(DB)
cur = conn.cursor()


for t in tables:

    print("\nTABLE:", t)

    result = cur.execute(
        """
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        AND name=?
        """,
        (t,)
    ).fetchone()


    if result:

        count = cur.execute(
            f"SELECT COUNT(*) FROM {t}"
        ).fetchone()[0]

        print("[FOUND]")
        print("ROWS:", count)


        columns = cur.execute(
            f"PRAGMA table_info({t})"
        ).fetchall()

        print("COLUMNS:")

        for c in columns:
            print("-", c[1], c[2])


    else:
        print("[MISSING]")


conn.close()


print("\nCHECK FINISHED")
