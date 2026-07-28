
# -*- coding: utf-8 -*-



class FeatureTableMapper:


    def __init__(self):

        self.mapping = {

            "HomeTeam":
            "home_team",

            "AwayTeam":
            "away_team",

            "FTHG":
            "home_score",

            "FTAG":
            "away_score"

        }



    def convert(self, data):


        result={}


        for key,value in data.items():

            if key in self.mapping:

                result[
                    self.mapping[key]
                ] = value


        return result


