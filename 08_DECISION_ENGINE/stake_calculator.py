
# -*- coding: utf-8 -*-



class StakeCalculator:



    def calculate(

        self,

        bankroll,

        confidence,

        risk_level

    ):



        base_rate=0.02




        if confidence=="A":


            base_rate=0.05



        elif confidence=="B":


            base_rate=0.03



        else:


            base_rate=0.01




        if risk_level=="HIGH":


            base_rate*=0.5




        stake=bankroll*base_rate




        return {


            "rate":

            round(

                base_rate,

                4

            ),


            "stake":

            round(

                stake,

                2

            )


        }



