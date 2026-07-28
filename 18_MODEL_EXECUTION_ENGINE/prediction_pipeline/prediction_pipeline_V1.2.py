# -*- coding:utf-8 -*-

import sys

sys.path.append(
r"E:\football_v\18_MODEL_EXECUTION_ENGINE"
)

sys.path.append(
r"E:\football_v\00_System_OS\03_MODEL_LAYER\Model_Pool"
)


from fusion_engine.fusion_engine_V1_2 import fusion_predict



def run_models():


    # 临时模型适配层
    #
    # 后续直接连接:
    # Model_Pool
    # Elo Engine
    # Dixon Coles Engine
    # Poisson Engine
    # XGBoost Engine


    elo={

        "home":0.40,
        "draw":0.30,
        "away":0.30

    }


    dixon={

        "home":0.45,
        "draw":0.25,
        "away":0.30

    }


    poisson={

        "home":0.50,
        "draw":0.25,
        "away":0.25

    }


    xgb={

        "home":0.35,
        "draw":0.35,
        "away":0.30

    }


    return (

        elo,
        dixon,
        poisson,
        xgb

    )




def predict():


    elo,dixon,poisson,xgb=run_models()


    result=fusion_predict(

        elo,
        dixon,
        poisson,
        xgb

    )


    output={


        "module":

        "Prediction Pipeline V1.2",


        "status":

        "COMPLETED",


        "prediction":

        result

    }


    print(output)


    return output




if __name__=="__main__":

    predict()

