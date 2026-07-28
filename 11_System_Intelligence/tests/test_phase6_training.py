
from elo_trainer import EloTrainer


def test_training():

    e=EloTrainer()

    r=e.train([])

    assert r["trained"]==True
