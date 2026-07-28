

# -*- coding:utf-8 -*-



class ChangeRiskAssessor:



    def assess(self,data):


        risk = (

            data.get(

                "model_change",

                0

            )

            +

            data.get(

                "feature_change",

                0

            )

        ) / 2



        level="LOW"



        if risk>=0.5:


            level="MEDIUM"



        if risk>=0.8:


            level="HIGH"



        return {


            "risk_score":

            risk,


            "level":

            level


        }



