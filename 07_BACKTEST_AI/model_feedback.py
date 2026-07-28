
# -*- coding: utf-8 -*-



class ModelFeedback:



    def analyze_error(
        self,
        predictions,
        results
    ):


        errors=[]



        for prediction,result in zip(

            predictions,

            results

        ):


            if prediction != result:


                errors.append(


                    {


                    "prediction":

                    prediction,


                    "actual":

                    result,


                    "type":

                    "MODEL_ERROR"


                    }


                )



        return {


            "errors":

            errors,


            "count":

            len(errors)



        }



    def generate_feedback(
        self,
        errors
    ):


        return {


            "model_adjustment":

            True,


            "error_samples":

            len(errors)



        }



