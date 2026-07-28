

# -*- coding:utf-8 -*-



class LearningCycleManager:



    def __init__(self):


        self.cycles=[]




    def create_cycle(

        self,

        cycle_type

    ):


        item={


            "cycle":

            cycle_type,


            "status":

            "RUNNING"



        }


        self.cycles.append(item)


        return item




    def history(self):


        return self.cycles



