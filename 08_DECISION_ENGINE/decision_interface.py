
# -*- coding: utf-8 -*-



from abc import ABC, abstractmethod




class DecisionInterface(ABC):



    @abstractmethod

    def decide(

        self,

        prediction

    ):

        pass




    @abstractmethod

    def report(

        self,

        decision

    ):

        pass



