
# -*- coding: utf-8 -*-



class DatabaseConnector:



    def __init__(self):

        self.database="PostgreSQL"



    def connect(self):

        return {


            "database":

            self.database,


            "status":

            "CONNECTED"


        }



    def close(self):

        return {

            "status":

            "CLOSED"

        }



