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



service = RuntimePredictionService()


result = service.predict(

    {
        "home":
        "Manchester City",

        "away":
        "Liverpool"

    }

)


print("==============================")
print("RUNTIME SERVICE TEST")
print("==============================")


print(result)

