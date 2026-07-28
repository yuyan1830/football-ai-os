

# -*- coding:utf-8 -*-



class RiskGate:



    def evaluate(

        self,

        error_rate,

        risk_level

    ):



        if error_rate > 0.4:


            return {


                "gate":

                "BLOCK",


                "reason":

                "HIGH_ERROR_RATE"



            }



        if risk_level=="HIGH":


            return {


                "gate":

                "REVIEW"



            }




        return {


            "gate":

            "PASS"



        }



