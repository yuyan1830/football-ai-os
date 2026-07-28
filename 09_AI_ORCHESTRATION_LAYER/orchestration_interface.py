
# -*- coding: utf-8 -*-


from abc import ABC,abstractmethod



class OrchestrationInterface(ABC):


    @abstractmethod

    def execute(self,task):

        pass



    @abstractmethod

    def status(self):

        pass



