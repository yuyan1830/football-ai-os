# -*- coding: utf-8 -*-

from .model_runtime_connector import model_runtime_check
from .model_outputs import run_models
from .model_fusion import fusion_predict
from .final_decision import final_decision
from .ai_report import generate_report


def run_prediction(home, away):

    models = run_models(
        home,
        away
    )

    fusion = fusion_predict(
        models["elo"],
        models["dixon"],
        models["poisson"],
        models["xgb"]
    )

    decision = final_decision(
        fusion
    )

    prediction = {

        "match":{
            "home":home,
            "away":away
        },

        "models":models,

        "fusion":fusion,

        "runtime":model_runtime_check(),

        "prediction_status":
            "PREDICTION_COMPLETED"

    }


    return generate_report(
        prediction,
        decision
    )
