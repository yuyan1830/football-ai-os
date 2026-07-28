
from probability_fusion_engine import ProbabilityFusionEngine


def test_probability():

    e=ProbabilityFusionEngine()

    r=e.fuse(
        {
            "elo":50,
            "poisson":30,
            "xgboost":20
        }
    )

    assert r["home"]>0
