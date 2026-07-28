
# -*- coding: utf-8 -*-



class DatabaseConnectionPool:



    def __init__(self):

        self.pool_size=10



    def acquire(self):

        return {


            "connection":

            "AVAILABLE"


        }



    def release(self):

        return {


            "connection":

            "RELEASED"


        }



