
from dynamic_weight_engine import DynamicWeightEngine


def test_weight():

    w=DynamicWeightEngine()

    r=w.update({})

    assert r["elo"]==0.25
