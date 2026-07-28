
from model_adjustment_engine import ModelAdjustmentEngine


def test_adjust():

    m=ModelAdjustmentEngine()

    assert m.adjust({})["updated"]==True
