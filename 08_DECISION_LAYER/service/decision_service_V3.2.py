# -*- coding: utf-8 -*-

"""
Football AI OS Ω+

Decision Service V3.2


职责:

连接:

Decision Engine

Consensus Engine

Risk Engine

"""


import sys

from importlib.machinery import SourceFileLoader


sys.path.insert(
    0,
    r"E:\football_v\08_DECISION_LAYER"
)


decision_module = SourceFileLoader(
    "decision_engine",
    r"E:\football_v\08_DECISION_LAYER\engine\decision_engine_V3.2.py"
).load_module()


DecisionEngineV32 = decision_module.DecisionEngineV32


from engine.consensus_engine import ConsensusEngine

from engine.risk_engine import RiskEngine



class DecisionServiceV32:


    def __init__(self):


        self.decision_engine = DecisionEngineV32()


        self.consensus_engine = ConsensusEngine()


        self.risk_engine = RiskEngine()



    def run(self, data):


        fusion = data.get(
            "fusion",
            {}
        )


        models = data.get(
            "models",
            {}
        )


        decision = self.decision_engine.evaluate(
            fusion
        )


        consensus = self.consensus_engine.analyze(
            models
        )


        risk = self.risk_engine.analyze(
            decision
        )


        return {


            "decision":
                decision,


            "consensus":
                consensus,


            "risk":
                risk,


            "status":
                "DECISION_SERVICE_V3.2_READY"

        }
