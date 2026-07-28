# -*- coding:utf-8 -*-

import sqlite3
import shutil
import os


SOURCE = r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"

TARGET = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


TABLES = [
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
print("MODEL HISTORY MIGRATION")
print("="*70)


src = sqlite3.connect(SOURCE)
dst = sqlite3.connect(TARGET)


for table in TABLES:

    print("\nMIGRATE:", table)


    sql = """
    SELECT sql 
    FROM sqlite_master
    WHERE type='table'
    AND name=?
    """

    schema = src.execute(sql,(table,)).fetchone()


    if not schema:
        print("SOURCE MISSING")
        continue


    dst.execute(schema[0])


    rows = src.execute(
        f"SELECT * FROM {table}"
    ).fetchall()


    if rows:

        placeholders=",".join(["?"]*len(rows[0]))

        dst.executemany(
            f"INSERT INTO {table} VALUES ({placeholders})",
            rows
        )


    print("ROWS:",len(rows))


dst.commit()

src.close()
dst.close()


print("\nMIGRATION FINISHED")

