
# -*- coding: utf-8 -*-



class FusionEngine:



    def __init__(self):

        self.weights={


            "Elo":

            0.25,


            "Dixon-Coles":

            0.25,


            "Poisson":

            0.25,


            "XGBoost":

            0.25


        }



    def fuse(
        self,
        predictions
    ):


        home=0

        draw=0

        away=0



        for model,data in predictions.items():


            weight=self.weights.get(

                model,

                0

            )


            home += data["home_win"] * weight

            draw += data["draw"] * weight

            away += data["away_win"] * weight



        return {


            "home_win":

            round(home,4),


            "draw":

            round(draw,4),


            "away_win":

            round(away,4)


        }



