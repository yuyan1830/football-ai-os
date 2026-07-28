

# -*- coding:utf-8 -*-



class EvolutionController:



    def __init__(self):


        self.state="IDLE"




    def start_evolution(

        self,

        task

    ):


        self.state="RUNNING"


        return {


            "task":

            task,


            "state":

            self.state



        }




    def finish(

        self

    ):


        self.state="COMPLETED"


        return {


            "state":

            self.state



        }



