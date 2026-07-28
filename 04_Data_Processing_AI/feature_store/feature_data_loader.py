
# -*- coding: utf-8 -*-


class FeatureDataLoader:


    def load(self, data):


        result=[]


        for item in data:


            result.append({

                "home_team":
                item.get(
                    "home_team"
                ),


                "away_team":
                item.get(
                    "away_team"
                ),


                "home_score":
                item.get(
                    "home_score"
                ),


                "away_score":
                item.get(
                    "away_score"
                )


            })


        return result


