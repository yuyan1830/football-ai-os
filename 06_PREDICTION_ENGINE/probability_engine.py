
# -*- coding: utf-8 -*-



class ProbabilityEngine:



    def __init__(self):

        self.status="READY"



    def calculate(
        self,
        model_predictions
    ):


        home=0

        draw=0

        away=0



        count=len(

            model_predictions

        )



        if count == 0:

            return {


                "home_win":0,


                "draw":0,


                "away_win":0


            }



        for prediction in model_predictions:


            home += prediction.get(

                "home_win",

                0

            )


            draw += prediction.get(

                "draw",

                0

            )


            away += prediction.get(

                "away_win",

                0

            )



        return {


            "home_win":

            round(

                home/count,

                4

            ),


            "draw":

            round(

                draw/count,

                4

            ),


            "away_win":

            round(

                away/count,

                4

            )


        }



    def compare_market(
        self,
        model_probability,
        market_probability
    ):


        return {


            "home_value":

            round(

                model_probability["home_win"]

                -

                market_probability["home_win"],

                4

            ),



            "draw_value":

            round(

                model_probability["draw"]

                -

                market_probability["draw"],

                4

            ),



            "away_value":

            round(

                model_probability["away_win"]

                -

                market_probability["away_win"],

                4

            )


        }



