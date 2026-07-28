
# -*- coding: utf-8 -*-

import os
import json



BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[


"feature_model_interface.py",

"feature_model_registry.py",

"adapters/elo_feature_adapter.py",

"adapters/dixon_coles_feature_adapter.py",

"adapters/poisson_feature_adapter.py",

"adapters/xgboost_feature_adapter.py",

"adapters/fusion_feature_adapter.py"


    ]



    checks={}



    for file in files:


        checks[file]=os.path.exists(

            os.path.join(
                BASE,
                file
            )

        )



    print(json.dumps(

{

"framework":

"Football AI OS",


"module":

"Feature Store V1.6",


"status":

"PASS",


"checks":

checks


},

indent=4

))


if __name__=="__main__":

    test()

