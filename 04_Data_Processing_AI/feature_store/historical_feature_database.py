
# -*- coding: utf-8 -*-


class HistoricalFeatureDatabase:


    def __init__(self):

        self.database_type = "PostgreSQL"



    def connect(self):

        return {

            "database":

            "historical_feature_db",


            "status":

            "CONNECTED"

        }



