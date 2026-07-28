
from elo_engine import EloEngine
from model_fusion_core import ModelFusionCore


def test_elo():

    e=EloEngine()

    r=e.calculate(
        1700,
        1600
    )

    assert r["home_win"]>0


def test_fusion():

    f=ModelFusionCore()

    r=f.fuse(
        [
            0.5,
            0.6
        ]
    )

    assert r["fusion_probability"]==0.55

