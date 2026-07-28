
# -*- coding: utf-8 -*-



class FinalDecisionReport:



    def generate(

        self,

        match,

        decision,

        probability,

        risk,

        stake

    ):



        return {


            "match":

            match,


            "decision":

            decision,


            "probability":

            probability,


            "risk":

            risk,


            "stake":

            stake



        }




    def summary(

        self,

        report

    ):


        return {


            "status":

            "READY",


            "report":

            report



        }



