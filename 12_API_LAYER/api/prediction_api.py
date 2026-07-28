
from service.football_prediction_service import FootballPredictionService


def prediction_api(match):

    return FootballPredictionService().predict(match)



if __name__=="__main__":

    print(
    prediction_api(
    {
    "home":"Manchester City",
    "away":"Liverpool"
    }
    )
    )

