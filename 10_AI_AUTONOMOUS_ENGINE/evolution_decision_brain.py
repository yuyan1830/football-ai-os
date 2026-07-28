

# -*- coding:utf-8 -*-


class EvolutionDecisionBrain:



    def decide(self,data):


        score=data.get(

            "optimization_value",

            0

        )


        risk=data.get(

            "risk",

            0

        )



        if score>0.8 and risk<0.3:

            return "EXECUTE"



        if risk<0.6:

            return "REVIEW"



        return "REJECT"



