
from risk_engine import RiskEngine


def test_risk():

    r=RiskEngine()

    x=r.calculate({})

    assert x["score"]==80
