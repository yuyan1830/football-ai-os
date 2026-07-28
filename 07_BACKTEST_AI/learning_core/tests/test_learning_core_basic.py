import sys
import os


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


from learning_decision import LearningDecision
from feature_feedback_engine import FeatureFeedbackEngine



def test_learning_decision():


    engine=LearningDecision()


    result=engine.evaluate({

        "accuracy_drop":True

    })


    assert result["learning_required"] is True



def test_feature_feedback():


    engine=FeatureFeedbackEngine()


    result=engine.analyze([

        {

            "feature":
            "home_advantage"

        }

    ])


    assert result["count"]==1
