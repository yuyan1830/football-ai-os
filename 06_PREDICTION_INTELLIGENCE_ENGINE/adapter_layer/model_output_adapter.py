# -*- coding: utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Model Output Adapter

统一模型概率输出格式
"""


class ModelOutputAdapter:



    def normalize(
        self,
        result
    ):


        return {


            "home":

            round(
                result.get("home",0),
                4
            ),


            "draw":

            round(
                result.get("draw",0),
                4
            ),


            "away":

            round(
                result.get("away",0),
                4
            )


        }



    def build_output(
        self,
        elo,
        dixon,
        poisson,
        xgb
    ):


        return {


            "elo":

            self.normalize(elo),


            "dixon_coles":

            self.normalize(dixon),


            "poisson":

            self.normalize(poisson),


            "xgboost":

            self.normalize(xgb)


        }



if __name__=="__main__":


    adapter=ModelOutputAdapter()


    print(

        adapter.build_output(

            {
            "home":0.4,
            "draw":0.3,
            "away":0.3
            },

            {
            "home":0.45,
            "draw":0.25,
            "away":0.3
            },

            {
            "home":0.5,
            "draw":0.25,
            "away":0.25
            },

            {
            "home":0.35,
            "draw":0.35,
            "away":0.3
            }

        )

    )

