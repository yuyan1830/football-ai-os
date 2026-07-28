

# -*- coding:utf-8 -*-



class StrategySelectionEngine:



    def select(self,strategies):


        if not strategies:

            return None



        return max(

            strategies,

            key=lambda x:x.get(

                "score",

                0

            )

        )



