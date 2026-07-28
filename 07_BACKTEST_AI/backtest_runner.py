
# -*- coding: utf-8 -*-



class BacktestRunner:



    def __init__(
        self,
        engine
    ):

        self.engine=engine



    def execute(
        self,
        dataset
    ):


        return self.engine.run(

            dataset

        )



