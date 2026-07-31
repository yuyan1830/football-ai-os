
# -*- coding: utf-8 -*-


class DecisionEngineV32:


    def evaluate(self,fusion):


        probabilities={

            "主胜":
            fusion.get("home_win_probability",0),

            "平局":
            fusion.get("draw_probability",0),

            "客胜":
            fusion.get("away_win_probability",0)

        }


        decision=max(
            probabilities,
            key=probabilities.get
        )


        return {

            "decision":decision,

            "confidence":
            round(
                probabilities[decision],
                4
            ),

            "probabilities":
            probabilities,

            "status":
            "DECISION_V32_READY"

        }
