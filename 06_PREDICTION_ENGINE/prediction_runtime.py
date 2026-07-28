
# -*- coding: utf-8 -*-



class PredictionRuntime:



    def __init__(self):

        self.state="STOPPED"



    def start(self):


        self.state="RUNNING"


        return self.state



    def stop(self):


        self.state="STOPPED"


        return self.state



    def health_check(self):


        return {


            "status":

            self.state


        }



