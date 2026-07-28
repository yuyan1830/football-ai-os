# -*- coding: utf-8 -*-

import sqlite3
import os


TARGETS = {

    "MODEL_STORE":
    r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db",

    "FEATURE_STORE":
    r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"

}


CHECK_TABLES = {

    "MODEL_STORE":[
        "elo_history",
        "dixon_coles_history",
        "poisson_history",
        "model_weight_history",
        "prediction_history"
    ],

    "FEATURE_STORE":[
        "team_form_history",
        "fatigue_history",
        "home_away_history",
        "xg_features_history"
    ]

}


print("="*70)
print("Football AI OS Ω+ V3.2")
print("TARGET HISTORY STRUCTURE CHECK")
print("="*70)


for name, db in TARGETS.items():

    print("\n")
    print("="*50)
    print(name)

    print(db)


    if not os.path.exists(db):

        print("[NOT FOUND]")
        continue


    conn = sqlite3.connect(db)

    cur = conn.cursor()


    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )

    tables=[
        x[0]
        for x in cur.fetchall()
    ]


    print("\nEXIST TABLES:")

    for t in tables:
        print("-",t)


    print("\nHISTORY CHECK:")


    for t in CHECK_TABLES[name]:

        if t in tables:

            cur.execute(
                f"SELECT COUNT(*) FROM {t}"
            )

            count=cur.fetchone()[0]

            print(
                "[FOUND]",
                t,
                "ROWS:",
                count
            )

        else:

            print(
                "[MISSING]",
                t
            )


    conn.close()


print("\nCHECK FINISHED")