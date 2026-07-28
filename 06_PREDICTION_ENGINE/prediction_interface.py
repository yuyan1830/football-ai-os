
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod



class PredictionInterface(ABC):



    @abstractmethod

    def predict(
        self,
        match
    ):

        pass



    @abstractmethod

    def generate_report(
        self,
        prediction
    ):

        pass



