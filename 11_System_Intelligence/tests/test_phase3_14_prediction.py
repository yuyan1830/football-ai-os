
from match_prediction_engine import MatchPredictionEngine


def test_prediction():

    e=MatchPredictionEngine()

    r=e.predict({})

    assert r["prediction"]=="home_win"
