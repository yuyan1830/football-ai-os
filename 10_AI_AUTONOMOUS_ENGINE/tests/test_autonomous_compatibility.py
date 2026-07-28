
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(ROOT))


def test_autonomous_v2():

    from autonomous_engine_v3 import AutonomousEngine

    engine = AutonomousEngine()

    result = engine.run()

    assert result["status"]=="running"



def test_autonomous_v3():

    from autonomous_engine_v3 import AutonomousEngineV3

    engine = AutonomousEngineV3()

    result = engine.execute()

    assert result["status"]=="running"



def test_human():

    from human_approval_v1 import HumanApproval

    obj = HumanApproval()

    assert obj.check()["approved"]



def test_optimizer():

    from optimization_suggestion_v1 import OptimizationSuggestion

    obj = OptimizationSuggestion()

    assert obj.generate()["status"]=="ready"

