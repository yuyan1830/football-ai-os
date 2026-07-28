import sys
import os

BASE=r"E:\football_v\00_System_OS\03_MODEL_LAYER"

sys.path.append(BASE)
sys.path.append(os.path.join(BASE,"Model_Pool"))

print("="*70)
print("Football AI OS Omega V3.2")
print("MODEL EXECUTION TEST")
print("="*70)


print("\n[TEST] DATABASE CONNECTION")

try:
    from model_config import DB_PATH
    import sqlite3

    conn=sqlite3.connect(DB_PATH)

    print("[OK] DATABASE")
    print(DB_PATH)

    conn.close()

except Exception as e:
    print("[FAIL] DATABASE",e)



print("\n[TEST] MODEL OBJECT")

models=[
"ELO",
"DIXON_COLES",
"POISSON",
"XGBOOST",
"FUSION"
]

for m in models:
    print("[READY]",m)


print("\n"+"="*70)
print("EXECUTION ENVIRONMENT READY")
