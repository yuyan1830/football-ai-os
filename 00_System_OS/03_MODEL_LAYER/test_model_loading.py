import sys

sys.path.append(
    r"E:\football_v\00_System_OS\03_MODEL_LAYER"
)


print("==============================")
print("Football AI OS Ω+ V3.2")
print("MODEL LOADING TEST")
print("==============================")


from model_config import DB_PATH

print("DATABASE:")
print(DB_PATH)


tests = []


try:
    from Model_Pool.Elo import elo_engine
    tests.append(("ELO", True, ""))
except Exception as e:
    tests.append(("ELO", False, str(e)))


try:
    from Model_Pool.Dixon_Coles import dixon_coles
    tests.append(("DIXON_COLES", True, ""))
except Exception as e:
    tests.append(("DIXON_COLES", False, str(e)))


try:
    from Model_Pool.Poisson import poisson_engine
    tests.append(("POISSON", True, ""))
except Exception as e:
    tests.append(("POISSON", False, str(e)))


try:
    from Model_Pool.XGBoost import xgboost_engine
    tests.append(("XGBOOST", True, ""))
except Exception as e:
    tests.append(("XGBOOST", False, str(e)))


try:
    from Model_Pool.XGBoost import xgboost_fusion_v2_engine
    tests.append(("XGBOOST_FUSION_V2", True, ""))
except Exception as e:
    tests.append(("XGBOOST_FUSION_V2", False, str(e)))


print()

for name,status,error in tests:
    if status:
        print("[OK]",name)
    else:
        print("[FAIL]",name)
        print(error)


print()
print("==============================")
print("TEST FINISHED")
print("==============================")

