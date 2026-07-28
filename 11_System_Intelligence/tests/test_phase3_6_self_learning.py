
from self_learning_engine import SelfLearningEngine
from model_optimizer import ModelOptimizer


def test_self_learning():

    engine=SelfLearningEngine()


    result=engine.learn(
        0.8,
        1
    )


    assert result["error"]==0.2



def test_optimizer():

    opt=ModelOptimizer()


    result=opt.optimize(
        0.8
    )


    assert "xgboost" in result
