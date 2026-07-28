

# -*- coding:utf-8 -*-


class EvolutionMemoryIndex:



    def __init__(self):

        self.memory=[]




    def add_record(self,data):


        self.memory.append(data)


        return True




    def search(self,key):


        result=[]


        for item in self.memory:


            if key in str(item):


                result.append(item)



        return result



