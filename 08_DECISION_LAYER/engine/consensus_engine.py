# -*- coding: utf-8 -*-

"""
Decision Consensus Engine V3.2

分析四模型一致性
"""


class ConsensusEngine:


    def analyze(self, models):


        result={

            "主胜":0,

            "平局":0,

            "客胜":0

        }


        mapping={

            "home":
            "主胜",

            "draw":
            "平局",

            "away":
            "客胜"

        }


        for model in models.values():

            value=max(
                model,
                key=model.get
            )


            result[
                mapping[value]
            ] += 1



        decision=max(
            result,
            key=result.get
        )


        return {

            "support":
                result,


            "consensus":
                decision,


            "status":
                "CONSENSUS_READY"

        }
