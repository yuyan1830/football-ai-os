# -*- coding: utf-8 -*-

import os
import json
import importlib.util
from datetime import datetime


BASE = r"E:/football_v/06_PREDICTION_INTELLIGENCE_ENGINE"

REPORT = os.path.join(
    BASE,
    "reports",
    "batch_test_report.json"
)


tests=[]


def add(name,status,message):

    tests.append({

        "test":name,

        "status":status,

        "message":message

    })


def load(name,path):

    spec=importlib.util.spec_from_file_location(
        name,
        path
    )

    module=importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module



# =========================
# Real Probability Fusion
# =========================

try:

    m=load(
        "fusion",
        BASE+"/real_probability_engine/fusion_calculator.py"
    )

    obj=m.FusionCalculator()

    result=obj.calculate(
        [
            "Elo",
            "Dixon-Coles",
            "Poisson",
            "XGBoost",
            "Fusion"
        ]
    )


    if "models" in result:

        add(
            "real_probability_engine",
            "PASS",
            "probability fusion ready"
        )


except Exception as e:

    add(
        "real_probability_engine",
        "FAIL",
        str(e)
    )



# =========================
# Advanced Connector
# =========================

try:

    m=load(
        "connector",
        BASE+"/advanced_model_connector/connector_manager.py"
    )


    obj=m.ConnectorManager()

    models=obj.list_models()


    if len(models)==5:

        add(
            "advanced_model_connector",
            "PASS",
            str(models)
        )


except Exception as e:

    add(
        "advanced_model_connector",
        "FAIL",
        str(e)
    )



# =========================
# Score Probability
# =========================

try:

    m=load(
        "score",
        BASE+"/score_probability_engine/score_distribution.py"
    )


    obj=m.ScoreDistribution()

    result=obj.calculate()


    if "1-0" in result:

        add(
            "score_probability_engine",
            "PASS",
            "score distribution ready"
        )


except Exception as e:

    add(
        "score_probability_engine",
        "FAIL",
        str(e)
    )



# =========================
# Confidence Calibration
# =========================

try:

    m=load(
        "confidence",
        BASE+"/confidence_calibration/calibration_engine.py"
    )


    obj=m.CalibrationEngine()

    obj.calibrate(0.8)


    add(
        "confidence_calibration",
        "PASS",
        "calibration ready"
    )


except Exception as e:

    add(
        "confidence_calibration",
        "FAIL",
        str(e)
    )



# =========================
# Risk Intelligence
# =========================

try:

    m=load(
        "risk",
        BASE+"/risk_intelligence_engine/upset_detector.py"
    )


    obj=m.UpsetDetector()

    obj.detect()


    add(
        "risk_intelligence_engine",
        "PASS",
        "risk detection ready"
    )


except Exception as e:

    add(
        "risk_intelligence_engine",
        "FAIL",
        str(e)
    )



# =========================
# Prediction API
# =========================

try:

    m=load(
        "api",
        BASE+"/prediction_api/api_service.py"
    )


    obj=m.PredictionAPI()

    obj.request()


    add(
        "prediction_api",
        "PASS",
        "API interface ready"
    )


except Exception as e:

    add(
        "prediction_api",
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

"prediction_engine_batch_test",


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