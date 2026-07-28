import sys
import os

BASE = r"E:\football_v\00_System_OS\03_MODEL_LAYER"

sys.path.append(BASE)
sys.path.append(os.path.join(BASE,"Model_Pool"))

print("="*70)
print("Football AI OS Omega V3.2")
print("MODEL RUNTIME TEST")
print("="*70)


# ELO
print("\n[TEST] ELO RUNTIME")

try:
    from Model_Pool.Elo import elo_engine
    
    print("[OK] ELO MODULE LOAD")
    
except Exception as e:
    print("[FAIL] ELO",e)



# Dixon Coles
print("\n[TEST] DIXON_COLES RUNTIME")

try:
    from Model_Pool.Dixon_Coles import dixon_coles
    
    print("[OK] DIXON_COLES MODULE LOAD")

except Exception as e:
    print("[FAIL] DIXON_COLES",e)



# Poisson
print("\n[TEST] POISSON RUNTIME")

try:
    from Model_Pool.Poisson import poisson_engine
    
    print("[OK] POISSON MODULE LOAD")

except Exception as e:
    print("[FAIL] POISSON",e)



# XGBoost
print("\n[TEST] XGBOOST RUNTIME")

try:
    from Model_Pool.XGBoost import xgboost_engine
    
    print("[OK] XGBOOST MODULE LOAD")

except Exception as e:
    print("[FAIL] XGBOOST",e)



# Fusion
print("\n[TEST] FUSION RUNTIME")

try:
    from Model_Pool.XGBoost import xgboost_fusion_v2_engine
    
    print("[OK] FUSION MODULE LOAD")

except Exception as e:
    print("[FAIL] FUSION",e)


print("\n"+"="*70)
print("RUNTIME MODULE CHECK FINISHED")
