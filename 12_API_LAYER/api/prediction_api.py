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



def prediction_api(match):


    return RuntimePredictionService().predict(
        match
    )



if __name__=="__main__":


    result = prediction_api(

        {
            "home":
            "Manchester City",

            "away":
            "Liverpool"

        }

    )


    print(result)

