
from service.football_prediction_service import FootballPredictionService


def decision_api(match):

    result=FootballPredictionService().predict(match)

    return result["decision"]


if __name__=="__main__":

    print(
    decision_api(
    {
    "home":"Manchester City",
    "away":"Liverpool"
    }
    )
    )

