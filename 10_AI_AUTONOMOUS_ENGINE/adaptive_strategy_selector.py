
# -*- coding:utf-8 -*-


class AdaptiveStrategySelector:


    def select(self,risk):

        if risk == "HIGH":

            return "CONSERVATIVE"


        return "BALANCED"

