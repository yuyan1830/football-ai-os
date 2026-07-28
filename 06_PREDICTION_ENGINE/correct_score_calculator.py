
# -*- coding: utf-8 -*-



class CorrectScoreCalculator:



    def rank(
        self,
        score_probability
    ):


        return sorted(

            score_probability.items(),

            key=lambda x:x[1],

            reverse=True

        )



    def top_scores(
        self,
        score_probability,
        limit=5
    ):


        ranking=self.rank(

            score_probability

        )



        return ranking[:limit]



