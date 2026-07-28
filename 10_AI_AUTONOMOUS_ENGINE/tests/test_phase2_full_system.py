# -*- coding: utf-8 -*-


def test_phase2_chain():


    from autonomous_engine_v3 import AutonomousEngine

    from system_brain import SystemBrain



    engine = AutonomousEngine()

    brain = SystemBrain()



    engine_result = engine.run()

    brain_result = brain.run()



    assert engine_result["status"] == "running"

    assert brain_result["status"] == "PASS"
