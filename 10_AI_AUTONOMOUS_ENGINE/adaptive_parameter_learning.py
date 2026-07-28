

# -*- coding:utf-8 -*-



class AdaptiveParameterLearning:



    def generate_suggestion(

        self,

        model,

        weight,

        error_rate,

        roi

    ):



        suggestion_weight = weight



        if error_rate > 0.25:


            suggestion_weight = round(

                weight * 0.9,

                3

            )



        return {


            "model":

            model,


            "parameter":

            "model_weight",


            "old_weight":

            weight,


            "suggested_weight":

            suggestion_weight,


            "error_rate":

            error_rate,


            "roi":

            roi,


            "confidence":

            0.85,


            "status":

            "WAIT_HUMAN"



        }




