import sys


sys.path.insert(
    0,
    r"E:\football_v"
)

sys.path.insert(
    0,
    r"E:\football_v\12_API_LAYER"
)


from service.runtime_prediction_service import RuntimePredictionService



def decision_api(match):


    result = RuntimePredictionService().predict(
        match
    )


    return result["decision"]



if __name__=="__main__":


    print(

        decision_api(

            {
                "home":
                "Manchester City",

                "away":
                "Liverpool"

            }

        )

    )
