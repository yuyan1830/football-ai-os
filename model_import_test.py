# -*- coding:utf-8 -*-

import sys
import sqlite3


print("="*70)
print("Football AI OS Ω+ V3.2")
print("MODEL RUNTIME IMPORT TEST")
print("="*70)


MODEL_PATH = r"E:\football_v\00_System_OS\03_MODEL_LAYER\Model_Pool"


sys.path.append(MODEL_PATH)


tests = [
    ("ELO",
     "Elo",
     "elo_engine"),

    ("DIXON_COLES",
     "Dixon_Coles",
     "dixon_coles"),

    ("POISSON",
     "Poisson",
     "poisson_engine"),

    ("XGBOOST",
     "XGBoost",
     "xgboost_engine"),

    ("XGBOOST_FUSION",
     "XGBoost",
     "xgboost_fusion_v2_engine")
]


for name,path,module in tests:

    print("\nTEST:",name)

    try:

        m=__import__(
            module
        )

        print("[OK] IMPORT")

    except Exception as e:

        print("[FAIL]")
        print(e)


print("\nTEST FINISHED")
