# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:/football_v/06_PREDICTION_INTELLIGENCE_ENGINE"


REPORT = os.path.join(
    BASE,
    "reports",
    "prediction_test_report.json"
)


tests=[]


def add_test(name,status,message):

    tests.append({

        "test":name,

        "status":status,

        "message":message

    })



def load_module(name,path):

    spec=importlib.util.spec_from_file_location(
        name,
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module



# 1 Regular Time

try:

    m=load_module(
        "prediction_engine",
        BASE+"/regular_time_prediction/prediction_engine.py"
    )


    obj=m.RegularTimePrediction()


    result=obj.predict({})


    if result["period"]=="90_minutes":

        add_test(
            "regular_time_prediction",
            "PASS",
            "90 minutes model ready"
        )


except Exception as e:

    add_test(
        "regular_time_prediction",
        "FAIL",
        str(e)
    )



# 2 Probability Fusion

try:

    m=load_module(
        "probability_fusion",
        BASE+"/probability_engine/probability_fusion.py"
    )


    obj=m.ProbabilityFusion()


    result=obj.calculate(
        [
            "Elo",
            "Dixon-Coles",
            "Poisson",
            "XGBoost",
            "Fusion"
        ]
    )


    if result["status"]=="fusion_ready":

        add_test(
            "probability_engine",
            "PASS",
            "fusion interface ready"
        )


except Exception as e:

    add_test(
        "probability_engine",
        "FAIL",
        str(e)
    )



# 3 Score Prediction

try:

    m=load_module(
        "score_predictor",
        BASE+"/score_prediction/score_predictor.py"
    )


    obj=m.ScorePredictor()


    result=obj.predict()


    if "score" in result:

        add_test(
            "score_prediction",
            "PASS",
            "score interface ready"
        )


except Exception as e:

    add_test(
        "score_prediction",
        "FAIL",
        str(e)
    )



# 4 Confidence

try:

    m=load_module(
        "confidence",
        BASE+"/confidence_engine/confidence_manager.py"
    )


    obj=m.ConfidenceManager()


    obj.calculate()


    add_test(
        "confidence_engine",
        "PASS",
        "confidence interface ready"
    )


except Exception as e:

    add_test(
        "confidence_engine",
        "FAIL",
        str(e)
    )



# 5 Risk

try:

    m=load_module(
        "risk",
        BASE+"/risk_engine/risk_manager.py"
    )


    obj=m.RiskManager()


    obj.evaluate()


    add_test(
        "risk_engine",
        "PASS",
        "risk interface ready"
    )


except Exception as e:

    add_test(
        "risk_engine",
        "FAIL",
        str(e)
    )



# 6 Knockout

try:

    m=load_module(
        "knockout",
        BASE+"/knockout_extension/knockout_engine.py"
    )


    obj=m.KnockoutExtension()


    result=obj.calculate()


    if "extra_time" in result:

        add_test(
            "knockout_extension",
            "PASS",
            "extra time and penalty interface ready"
        )


except Exception as e:

    add_test(
        "knockout_extension",
        "FAIL",
        str(e)
    )



# 7 Model Connector

try:

    m=load_module(
        "connector",
        BASE+"/model_connector/model_connector.py"
    )


    obj=m.ModelConnector()


    models=obj.connect()


    if len(models)==5:

        add_test(
            "model_connector",
            "PASS",
            str(models)
        )


except Exception as e:

    add_test(
        "model_connector",
        "FAIL",
        str(e)
    )



failed=[

x for x in tests

if x["status"]=="FAIL"

]



report={


"framework":

"Football AI OS Ultimate Fusion Framework V1.5",


"layer":

"06_PREDICTION_INTELLIGENCE_ENGINE",


"service":

"prediction_intelligence_test",


"version":

"V1.0",


"status":

"PASS" if len(failed)==0 else "FAIL",


"total_tests":

len(tests),


"failed":

len(failed),


"tests":

tests,


"time":

str(datetime.now())

}



with open(

REPORT,

"w",

encoding="utf-8"

) as f:


    json.dump(

        report,

        f,

        indent=4,

        ensure_ascii=False

    )



print("="*60)

print(json.dumps(

report,

indent=4,

ensure_ascii=False

))

print("="*60)