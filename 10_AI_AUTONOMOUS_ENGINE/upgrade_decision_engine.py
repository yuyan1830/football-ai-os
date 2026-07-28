

# -*- coding:utf-8 -*-



class UpgradeDecisionEngine:



    def decide(self,data):


        score=data.get(

            "evolution_score",

            0

        )



        risk=data.get(

            "risk_score",

            1

        )



        if score>0 and risk<0.3:


            return "KEEP"



        elif risk<0.6:


            return "REVIEW"



        else:


            return "ROLLBACK"



