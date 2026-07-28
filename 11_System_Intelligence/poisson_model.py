
import math


class PoissonModel:


    def probability(self, attack, defense):

        lam = attack*defense


        return {

            "goal_rate":
                round(lam,4)

        }
