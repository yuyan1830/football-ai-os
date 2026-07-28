# -*- coding: utf-8 -*-

import sqlite3
import os
import shutil
from datetime import datetime


SOURCE_DB = r"E:\football\Football_AI_System\data\football.db"

TARGET_DB = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"

BACKUP_DB = (
    r"E:\football_v\99_Documentation\checkpoints"
    r"\model_store_before_history_migration_"
    + datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".db"
)


HISTORY_TABLES = [

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


# ==========================
# backup
# ==========================

if os.path.exists(TARGET_DB):

    os.makedirs(
        os.path.dirname(BACKUP_DB),
        exist_ok=True
    )

    shutil.copy2(
        TARGET_DB,
        BACKUP_DB
    )

    print("[BACKUP]")
    print(BACKUP_DB)


# ==========================
# connect
# ==========================

source = sqlite3.connect(SOURCE_DB)

target = sqlite3.connect(TARGET_DB)


src = source.cursor()
dst = target.cursor()



# ==========================
# migrate tables
# ==========================

for table in HISTORY_TABLES:


    print("\nCHECK:", table)


    src.execute(
        f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
    )

    exists = src.fetchone()


    if not exists:

        print("[SKIP] SOURCE NOT FOUND")

        continue



    # get schema

    src.execute(
        f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table}'"
    )

    schema = src.fetchone()[0]


    dst.execute(
        f"""
        SELECT name FROM sqlite_master
        WHERE type='table'
        AND name='{table}'
        """
    )


    target_exists = dst.fetchone()



    if not target_exists:

        print("[CREATE]", table)

        dst.execute(schema)



    else:

        print("[EXISTS]", table)



    # clear old

    dst.execute(
        f"DELETE FROM {table}"
    )



    # copy data

    src.execute(
        f"SELECT * FROM {table}"
    )

    rows = src.fetchall()


    if rows:

        placeholders = ",".join(
            ["?"] * len(rows[0])
        )


        dst.executemany(
            f"INSERT INTO {table} VALUES ({placeholders})",
            rows
        )


    print(
        "[MIGRATED]",
        table,
        "ROWS:",
        len(rows)
    )



target.commit()


source.close()
target.close()


print("\n")
print("="*70)
print("MIGRATION FINISHED")
print("="*70)

