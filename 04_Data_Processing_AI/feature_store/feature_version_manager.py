
# -*- coding: utf-8 -*-


class FeatureVersionManager:


    def __init__(self):

        self.version="V2.4"



    def get_version(self):

        return self.version



    def register_feature(
        self,
        feature
    ):

        return {

            "feature":

            feature,


            "version":

            self.version

        }


