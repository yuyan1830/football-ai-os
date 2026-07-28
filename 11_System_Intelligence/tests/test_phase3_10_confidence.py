
from confidence_engine import ConfidenceEngine


def test_confidence():

    c=ConfidenceEngine()

    r=c.calculate(
        0.8
    )

    assert r["confidence"]==0.8
