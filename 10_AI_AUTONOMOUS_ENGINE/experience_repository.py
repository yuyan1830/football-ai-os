

# -*- coding:utf-8 -*-



class ExperienceRepository:



    def __init__(self):

        self.records=[]




    def save(self,experience):


        self.records.append(experience)


        return True




    def all(self):


        return self.records



