

# -*- coding:utf-8 -*-



class StrategyEvolutionManager:



    def __init__(self):


        self.strategies=[]




    def evaluate(

        self,

        strategy,

        result

    ):



        item={


            "strategy":

            strategy,


            "result":

            result,


            "status":

            "ANALYZED"



        }


        self.strategies.append(item)


        return item




    def recommend(self):


        return {


            "recommendation":

            "KEEP_BEST_PERFORMER"



        }



