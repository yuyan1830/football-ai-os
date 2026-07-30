# -*- coding: utf-8 -*-

"""
Football AI OS
Runtime Prediction Service V1.1


API Layer
    |
AI Runtime Adapter
    |
AI Runtime Engine

"""


import sys


sys.path.insert(
    0,
    r"E:\football_v"
)


sys.path.insert(
    0,
    r"E:\football_v\12_API_LAYER"
)


from adapter.ai_runtime_adapter import run_ai_runtime



class RuntimePredictionService:


    def predict(self, match):


        result = run_ai_runtime(
            match
        )


        prediction = result.get(
            "prediction",
            {}
        )


        return {


            "service":
                "RuntimePredictionService",


            "match":
                prediction.get(
                    "match",
                    match
                ),


            "model_result":
                prediction.get(
                    "model_result",
                    {}
                ),


            "decision":
                prediction.get(
                    "final_decision",
                    {}
                ),


            "runtime":
                {

                "database_status":
                    result.get(
                        "database_status",
                        {}
                    ),


                "model_runtime":
                    result.get(
                        "model_runtime",
                        {}
                    )

                },


            "status":
                "READY"

        }

