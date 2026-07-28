# -*- coding: utf-8 -*-

import importlib.util
import os


BASE=r"E:\football_v\18_MODEL_EXECUTION_ENGINE"


fusion_file=os.path.join(
    BASE,
    "fusion_engine",
    "fusion_engine_V1.0.py"
)


spec=importlib.util.spec_from_file_location(
    "fusion_core",
    fusion_file
)

module=importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)


fusion=module.fusion



def predict():


    # 当前接入 V3.2 模型输出接口
    # 后续由 model_loader 自动替换

    elo={

        "home":0.45,
        "draw":0.30,
        "away":0.25

    }


    dixon={

        "home":0.42,
        "draw":0.28,
        "away":0.30

    }


    poisson={

        "home":0.40,
        "draw":0.32,
        "away":0.28

    }


    xgb={

        "home":0.43,
        "draw":0.27,
        "away":0.30

    }



    result=fusion(
        elo,
        dixon,
        poisson,
        xgb
    )


    print(
    {
        "module":
        "Prediction Pipeline",

        "status":
        "COMPLETED",

        "prediction":
        result
    }
    )


    return result



if __name__=="__main__":

    predict()
