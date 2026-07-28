
# -*- coding: utf-8 -*-



class DecisionEngine:



    def __init__(self):


        self.status="READY"




    def decide(

        self,

        prediction

    ):



        probability=max(

            prediction.values()

        )



        if probability >=0.75:


            decision="BET"



        elif probability >=0.60:


            decision="WATCH"



        else:


            decision="PASS"




        return {


            "decision":

            decision,


            "probability":

            probability



        }




    def health(self):


        return {


            "status":

            self.status


        }



