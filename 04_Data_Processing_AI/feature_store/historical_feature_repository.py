
# -*- coding: utf-8 -*-



class HistoricalFeatureRepository:



    def save_feature(
        self,
        feature
    ):


        return {


            "saved":

            True,


            "feature":

            feature


        }



    def load_feature(
        self,
        query
    ):


        return {



            "query":

            query


        }



