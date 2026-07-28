
# -*- coding: utf-8 -*-



from goal_distribution import GoalDistribution

from correct_score_calculator import CorrectScoreCalculator




class ScorePredictionEngine:



    def __init__(self):


        self.goal_engine=GoalDistribution()


        self.score_calculator=CorrectScoreCalculator()



    def predict(
        self,
        home_xg,
        away_xg
    ):


        score_probability=(


            self.goal_engine.generate(

                home_xg,

                away_xg

            )

        )



        top_scores=(


            self.score_calculator.top_scores(

                score_probability

            )

        )



        return {


            "home_xg":

            home_xg,


            "away_xg":

            away_xg,


            "top_scores":

            top_scores,


            "all_scores":

            score_probability


        }



