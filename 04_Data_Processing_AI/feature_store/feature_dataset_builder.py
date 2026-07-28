
# -*- coding: utf-8 -*-


class FeatureDatasetBuilder:


    def build(self, matches):


        dataset=[]


        for item in matches:


            dataset.append({

                "home_team":
                item.get("home_team"),


                "away_team":
                item.get("away_team"),


                "feature_version":
                "V1.1"

            })


        return dataset


