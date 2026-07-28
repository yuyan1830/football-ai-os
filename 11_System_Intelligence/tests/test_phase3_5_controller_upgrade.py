

from intelligence_scheduler import IntelligenceScheduler
from intelligence_router import IntelligenceRouter
from intelligence_weight_manager import IntelligenceWeightManager
from intelligence_feedback_loop import IntelligenceFeedbackLoop



def test_controller_upgrade():

    s=IntelligenceScheduler()

    s.register("decision")

    assert s.run()["tasks"]==1



def test_router():

    r=IntelligenceRouter()

    assert r.route({})=="normal_reasoning"



def test_weight():

    w=IntelligenceWeightManager()

    w.update("memory",0.5)

    assert w.get()["memory"]==0.5



def test_feedback():

    f=IntelligenceFeedbackLoop()

    f.record({"result":"win"})

    assert f.size()==1

