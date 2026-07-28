
# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime


BASE=r"E:\football_v\17_MODEL_STORE_LAYER"


MODELS=[

"Elo",

"Dixon-Coles",

"Poisson",

"XGBoost",

"V38.8.1 Handicap Model",

"Market Risk Model 2.0"

]


def run():

    registry={

        "module":
        "Model Registry",

        "version":
        "V1.0",

        "models":
        MODELS,

        "time":
        str(datetime.now())

    }


    path=os.path.join(

        BASE,

        "model_registry",

        "registry.json"

    )


    os.makedirs(

        os.path.dirname(path),

        exist_ok=True

    )


    with open(

        path,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            registry,

            f,

            indent=4,

            ensure_ascii=False

        )


    print(registry)



if __name__=="__main__":

    run()

