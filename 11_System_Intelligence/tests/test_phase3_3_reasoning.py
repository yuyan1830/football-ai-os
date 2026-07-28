
from reasoning_engine import ReasoningEngine
from decision_reasoner import DecisionReasoner


def test_reasoning_engine():

    engine=ReasoningEngine()

    result=engine.reason(
        {
            "risk":0.2
        }
    )

    assert result["decision"]=="continue"



def test_decision_reasoner():

    d=DecisionReasoner()

    result=d.decide(
        {
            "risk":0.9
        }
    )

    assert result["decision"]=="avoid"
