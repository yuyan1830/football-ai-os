# -*- coding: utf-8 -*-

"""
Football AI OS Ω+
Decision Engine V3.2

职责:

接收 Fusion 输出
生成基础决策结果
"""


class DecisionEngineV32:


    def evaluate(self, fusion):


        probabilities = {

            "主胜":
            fusion.get(
                "home_win_probability",
                0
            ),

            "平局":
            fusion.get(
                "draw_probability",
                0
            ),

            "客胜":
            fusion.get(
                "away_win_probability",
                0
            )

        }


        decision=max(
            probabilities,
            key=probabilities.get
        )


        confidence=probabilities[decision]


        return {

            "decision":
                decision,


            "confidence":
                round(
                    confidence,
                    4
                ),


            "probabilities":
                probabilities,


            "status":
                "DECISION_V3.2_READY"

        }
