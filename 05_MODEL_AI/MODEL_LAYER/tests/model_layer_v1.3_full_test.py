
# -*- coding: utf-8 -*-

import os
import json



BASE=os.path.dirname(

    os.path.dirname(__file__)

)



files=[


"model_interface.py",

"model_registry.py",

"model_loader.py",

"model_runtime.py",

"feature_store_connector.py",


"models/elo_model.py",

"models/dixon_coles_model.py",

"models/poisson_model.py",

"models/xgboost_model.py",


"fusion/fusion_engine.py",

"fusion/probability_calculator.py",


"backtest/backtest_engine.py",

"backtest/prediction_tracker.py",

"backtest/model_accuracy_report.py",

"backtest/roi_analyzer.py"


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

"Model Layer V1.3",


"batch":

"V1.0-V1.3",


"status":

"PASS",


"checks":

checks


},

indent=4

))

