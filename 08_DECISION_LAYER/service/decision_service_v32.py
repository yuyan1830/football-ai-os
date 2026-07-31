
# -*- coding: utf-8 -*-


from engine.decision_engine_v32 import DecisionEngineV32

from engine.consensus_engine import ConsensusEngine

from engine.risk_engine import RiskEngine



class DecisionServiceV32:


    def __init__(self):

        self.decision_engine = DecisionEngineV32()

        self.consensus_engine = ConsensusEngine()

        self.risk_engine = RiskEngine()



    def run(self,data):


        fusion=data.get(
            "fusion",
            {}
        )


        models=data.get(
            "models",
            {}
        )


        decision=self.decision_engine.evaluate(
            fusion
        )


        consensus=self.consensus_engine.analyze(
            models
        )


        risk=self.risk_engine.analyze(
            decision
        )


        return {

            "decision":decision,

            "consensus":consensus,

            "risk":risk,

            "status":
            "DECISION_SERVICE_V32_READY"

        }
