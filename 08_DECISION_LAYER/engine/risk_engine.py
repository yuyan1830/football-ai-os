# -*- coding: utf-8 -*-

"""
Decision Risk Engine V3.2

风险分析
"""


class RiskEngine:


    def analyze(self, decision):


        confidence = decision.get(
            "confidence",
            0
        )


        if confidence >= 0.55:

            level="LOW"


        elif confidence >= 0.45:

            level="MEDIUM"


        else:

            level="HIGH"



        return {


            "risk_level":
                level,


            "confidence":
                confidence,


            "status":
                "RISK_READY"

        }
