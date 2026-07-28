
# -*- coding: utf-8 -*-


class FeatureSelector:


    def select(self,model):


        return {

            "model":
            model,

            "features":
            "selected"

        }



if __name__=="__main__":

    print(
        FeatureSelector().select("XGBoost")
    )
