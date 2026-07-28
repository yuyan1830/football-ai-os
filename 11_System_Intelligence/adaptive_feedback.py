
class AdaptiveFeedback:


    def analyze(self,error):

        if error>0.5:

            return {

            "adjust":
            "increase historical analysis"

            }


        return {

        "adjust":
        "stable"

        }
