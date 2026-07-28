# -*- coding:utf-8 -*-

import sqlite3


DB = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


conn = sqlite3.connect(DB)
cur = conn.cursor()


print("="*70)
print("XG HISTORY DATE FIELD CHECK")
print("="*70)


columns = cur.execute(
    "PRAGMA table_info(xg_features_history)"
).fetchall()


for c in columns:
    print(c[1], c[2])


conn.close()
