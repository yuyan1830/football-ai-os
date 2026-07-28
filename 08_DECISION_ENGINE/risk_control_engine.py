
# -*- coding: utf-8 -*-



class RiskControlEngine:



    def analyze(

        self,

        confidence,

        risk_level

    ):



        if risk_level=="HIGH":


            return {


                "action":

                "BLOCK",


                "reason":

                "HIGH_RISK"


            }




        if confidence=="C":


            return {


                "action":

                "WATCH",


                "reason":

                "LOW_CONFIDENCE"


            }




        return {


            "action":

            "ALLOW",


            "reason":

            "NORMAL"


        }



