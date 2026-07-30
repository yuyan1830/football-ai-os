import sys


sys.path.insert(
    0,
    r"E:\football_v"
)

sys.path.insert(
    0,
    r"E:\football_v\12_API_LAYER"
)


from api.prediction_api import prediction_api



def call_system(task, message):


    if task == "MATCH_ANALYSIS":


        return prediction_api(

            {
                "home":
                "Manchester City",

                "away":
                "Liverpool"

            }

        )


    return {

        "task":
            task,

        "status":
            "NOT_IMPLEMENTED"

    }

