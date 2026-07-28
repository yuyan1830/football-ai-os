
# -*- coding: utf-8 -*-



class FeatureGenerator:



    def generate(
        self,
        matches
    ):


        dataset=[]



        for match in matches:


            dataset.append({

                "home_team":
                match.get(
                    "home_team"
                ),


                "away_team":
                match.get(
                    "away_team"
                ),


                "home_score":
                match.get(
                    "home_score"
                ),


                "away_score":
                match.get(
                    "away_score"
                )

            })


        return dataset


