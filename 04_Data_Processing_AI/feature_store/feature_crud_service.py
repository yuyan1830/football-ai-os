
# -*- coding: utf-8 -*-



class FeatureCRUDService:



    def create(
        self,
        feature
    ):


        return {


            "created":

            True,


            "feature":

            feature


        }



    def read(
        self,
        feature_id
    ):


        return {


            "feature_id":

            feature_id


        }



    def update(
        self,
        feature
    ):


        return {


            "updated":

            True


        }



    def delete(
        self,
        feature_id
    ):


        return {


            "deleted":

            True


        }



