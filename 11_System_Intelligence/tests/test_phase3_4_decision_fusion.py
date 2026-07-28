

from decision_fusion import DecisionFusion


def test_decision_fusion():

    engine=DecisionFusion()

    result=engine.calculate({

        "model":0.6,
        "reasoning":0.7,
        "memory":0.8

    })


    assert result>0


