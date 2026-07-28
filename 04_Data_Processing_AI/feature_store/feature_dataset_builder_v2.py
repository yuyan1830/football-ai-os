
# -*- coding: utf-8 -*-


class FeatureDatasetBuilderV2:


    def build(self, matches):


        dataset=[]


        for match in matches:


            home_score = match.get(
                "home_score",
                0
            )


            away_score = match.get(
                "away_score",
                0
            )


            if home_score > away_score:

                result="HOME_WIN"

            elif home_score < away_score:

                result="AWAY_WIN"

            else:

                result="DRAW"



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
                home_score,

                "away_score":
                away_score,

                "result":
                result

            })


        return dataset


