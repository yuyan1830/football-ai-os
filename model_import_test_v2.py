import sys
import os

BASE = r"E:\football_v\00_System_OS\03_MODEL_LAYER"

sys.path.append(BASE)
sys.path.append(os.path.join(BASE,"Model_Pool"))

print("Football AI OS Omega V3.2")
print("="*70)

print("[TEST] ELO")

try:
    from Model_Pool.Elo import elo_engine
    print("[OK] ELO")
except Exception as e:
    print("[FAIL] ELO",e)


print("[TEST] DIXON_COLES")

try:
    from Model_Pool.Dixon_Coles import dixon_coles
    print("[OK] DIXON_COLES")
except Exception as e:
    print("[FAIL] DIXON_COLES",e)


print("[TEST] POISSON")

try:
    from Model_Pool.Poisson import poisson_engine
    print("[OK] POISSON")
except Exception as e:
    print("[FAIL] POISSON",e)


print("[TEST] XGBOOST")

try:
    from Model_Pool.XGBoost import xgboost_engine
    print("[OK] XGBOOST")
except Exception as e:
    print("[FAIL] XGBOOST",e)


print("[TEST] XGBOOST FUSION")

try:
    from Model_Pool.XGBoost import xgboost_fusion_v2_engine
    print("[OK] XGBOOST_FUSION")
except Exception as e:
    print("[FAIL] XGBOOST_FUSION",e)


print("="*70)
print("FINISHED")
