
# -*- coding: utf-8 -*-



from value_filter_engine import ValueFilterEngine

from risk_control_engine import RiskControlEngine




class BetSelectionEngine:



    def __init__(self):


        self.value_engine=ValueFilterEngine()


        self.risk_engine=RiskControlEngine()




    def select(

        self,

        model_probability,

        market_probability,

        confidence,

        risk_level

    ):



        value=self.value_engine.calculate_value(

            model_probability,

            market_probability

        )



        value_status=self.value_engine.check_value(

            value

        )



        risk_result=self.risk_engine.analyze(

            confidence,

            risk_level

        )




        if risk_result["action"]=="BLOCK":


            decision="PASS"



        elif value_status=="VALUE_FOUND":


            decision="BET"



        else:


            decision="WATCH"





        return {


            "decision":

            decision,


            "value":

            value,


            "risk":

            risk_result



        }



