# -*- coding:utf-8 -*-

import sys


MODEL_PATH=r"E:\football_v\00_System_OS\03_MODEL_LAYER\Model_Pool"

sys.path.append(MODEL_PATH)



def load_models():

    models={}


    try:
        from Elo import elo_engine
        models["ELO"]=elo_engine
    except Exception as e:
        models["ELO_ERROR"]=str(e)


    try:
        from Dixon_Coles import dixon_coles
        models["DIXON_COLES"]=dixon_coles
    except Exception as e:
        models["DIXON_ERROR"]=str(e)


    try:
        from Poisson import poisson_engine
        models["POISSON"]=poisson_engine
    except Exception as e:
        models["POISSON_ERROR"]=str(e)


    try:
        from XGBoost import xgboost_engine
        models["XGBOOST"]=xgboost_engine
    except Exception as e:
        models["XGB_ERROR"]=str(e)


    try:
        from XGBoost import xgboost_fusion_v2_engine
        models["FUSION"]=xgboost_fusion_v2_engine
    except Exception as e:
        models["FUSION_ERROR"]=str(e)


    return models



if __name__=="__main__":

    result=load_models()

    for k,v in result.items():

        print(
            "[OK]",
            k,
            type(v)
        )
