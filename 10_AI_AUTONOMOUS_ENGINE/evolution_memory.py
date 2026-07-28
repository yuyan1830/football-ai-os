

# -*- coding:utf-8 -*-



class EvolutionMemory:



    def __init__(self):


        self.memory=[]




    def store(

        self,

        event

    ):


        self.memory.append(event)


        return {


            "stored":

            True



        }




    def query(self):


        return self.memory



