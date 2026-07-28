
# -*- coding: utf-8 -*-



class FeatureDatabaseSession:



    def __init__(self):

        self.database="PostgreSQL"



    def connect(self):

        return {


            "database":

            self.database,


            "status":

            "READY"


        }



