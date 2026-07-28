
class ModelOptimizer:


    def __init__(self):

        self.weights={

            "elo":0.25,

            "poisson":0.25,

            "dixon_coles":0.25,

            "xgboost":0.25

        }



    def optimize(self,score):


        if score>0.7:

            self.weights["xgboost"]+=0.03


        elif score<0.5:

            self.weights["xgboost"]-=0.03



        total=sum(
            self.weights.values()
        )


        for k in self.weights:

            self.weights[k]=round(
                self.weights[k]/total,
                4
            )


        return self.weights
