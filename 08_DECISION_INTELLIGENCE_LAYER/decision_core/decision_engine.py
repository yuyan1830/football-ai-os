
# -*- coding: utf-8 -*-


class DecisionEngine:


    def decide(self, fusion_probability):

        if fusion_probability >= 0.55:

            return {
                "decision":"HOME_WIN",
                "confidence":"HIGH"
            }


        elif fusion_probability <= 0.45:

            return {
                "decision":"AWAY_WIN",
                "confidence":"HIGH"
            }


        else:

            return {
                "decision":"RISK_ZONE",
                "confidence":"MEDIUM"
            }

