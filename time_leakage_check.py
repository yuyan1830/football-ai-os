# -*- coding:utf-8 -*-

import sqlite3


DB = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


TEST_DATE = "2018-05-01"


tables = [
    "elo_history",
    "dixon_coles_history",
    "poisson_history",
    "team_form_history",
    "fatigue_history",
    "home_away_history"
]


print("="*70)
print("Football AI OS Ω+ V3.2")
print("TIME LEAKAGE CHECK")
print("="*70)

print("TEST DATE:", TEST_DATE)


conn = sqlite3.connect(DB)
cur = conn.cursor()


for t in tables:

    print("\nTABLE:", t)


    result = cur.execute(
        f"""
        SELECT 
        MAX(date)
        FROM {t}
        WHERE date <= ?
        """,
        (TEST_DATE,)
    ).fetchone()


    future = cur.execute(
        f"""
        SELECT 
        COUNT(*)
        FROM {t}
        WHERE date > ?
        """,
        (TEST_DATE,)
    ).fetchone()[0]


    print(
        "LATEST AVAILABLE:",
        result[0]
    )

    print(
        "FUTURE RECORDS:",
        future
    )


conn.close()

print("\nLEAKAGE CHECK FINISHED")
