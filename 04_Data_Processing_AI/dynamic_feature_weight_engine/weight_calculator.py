
# -*- coding:utf-8 -*-


class WeightCalculator:


    def calculate_model_weight(self,model):


        default={

            "Elo":0.15,

            "Dixon-Coles":0.18,

            "Poisson":0.12,

            "XGBoost":0.25,

            "Fusion":0.30

        }


        return default.get(
            model,
            0
        )



if __name__=="__main__":

    print(
        WeightCalculator().calculate_model_weight(
            "Fusion"
        )
    )
