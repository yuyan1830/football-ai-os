# -*- coding: utf-8 -*-

import sys
import os


BASE = r"E:\football_v\00_System_OS\03_MODEL_LAYER"

sys.path.append(BASE)

sys.path.append(
    os.path.join(BASE,"Model_Pool","Elo")
)

sys.path.append(
    os.path.join(BASE,"Model_Pool","Dixon_Coles")
)

sys.path.append(
    os.path.join(BASE,"Model_Pool","Poisson")
)

sys.path.append(
    os.path.join(BASE,"Model_Pool","XGBoost")
)


print("="*70)
print("Football AI OS Omega V3.2")
print("MODEL IMPORT TEST")
print("="*70)


tests=[
    ("ELO","elo_engine"),
    ("DIXON_COLES","dixon_coles"),
    ("POISSON","poisson_engine"),
    ("XGBOOST","xgboost_engine"),
    ("XGBOOST_FUSION","xgboost_fusion_v2_engine")
]


for name,module in tests:

    try:
        __import__(module)
        print("[OK]", name)

    except Exception as e:
        print("[FAIL]", name, e)


print("="*70)
print("FINISHED")
