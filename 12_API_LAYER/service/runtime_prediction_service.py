import sys


sys.path.insert(
    0,
    r"E:\football_v"
)

sys.path.insert(
    0,
    r"E:\football_v\12_API_LAYER"
)

sys.path.insert(
    0,
    r"E:\football_v\13_OUTPUT_SERVICE_LAYER"
)


from adapter.ai_runtime_adapter import run_ai_runtime

from output_adapter import generate_output



class RuntimePredictionService:



    def predict(self, match):


        result = run_ai_runtime(
            match
        )


        prediction = result.get(
            "prediction",
            {}
        )


        api_result = {


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

                }

        }


        return generate_output(
            api_result
        )

