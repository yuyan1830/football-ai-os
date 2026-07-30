# -*- coding:utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Probability Extraction Layer

统一模型概率输出
"""


class ProbabilityExtractor:


    def normalize(self,home,draw,away):

        total = home + draw + away

        if total == 0:

            return {
                "home":0,
                "draw":0,
                "away":0
            }


        return {

            "home":round(home/total,4),

            "draw":round(draw/total,4),

            "away":round(away/total,4)

        }



    def extract_elo(self,data):

        return self.normalize(

            data.get("home",0),

            data.get("draw",0),

            data.get("away",0)

        )



    def extract_dixon(self,data):

        return self.normalize(

            data.get("home",0),

            data.get("draw",0),

            data.get("away",0)

        )



    def extract_poisson(self,data):

        return self.normalize(

            data.get("home",0),

            data.get("draw",0),

            data.get("away",0)

        )



    def extract_xgboost(self,data):

        return self.normalize(

            data.get("home",0),

            data.get("draw",0),

            data.get("away",0)

        )



    def extract_all(
        self,
        elo,
        dixon,
        poisson,
        xgb
    ):


        return {


            "elo":
            self.extract_elo(elo),


            "dixon_coles":
            self.extract_dixon(dixon),


            "poisson":
            self.extract_poisson(poisson),


            "xgboost":
            self.extract_xgboost(xgb)


        }



if __name__=="__main__":


    extractor=ProbabilityExtractor()


    print(

        extractor.extract_all(

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
