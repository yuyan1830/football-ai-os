
# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod



class BaseModelInterface(ABC):


    @abstractmethod

    def train(
        self,
        data
    ):

        pass



    @abstractmethod

    def predict(
        self,
        features
    ):

        pass



    @abstractmethod

    def evaluate(
        self,
        result
    ):

        pass



    @abstractmethod

    def save(
        self,
        path
    ):

        pass



    @abstractmethod

    def load(
        self,
        path
    ):

        pass



