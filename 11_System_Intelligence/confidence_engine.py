
class ConfidenceEngine:


    def calculate(self,probability):

        return {

            "confidence":

                round(
                    probability,
                    4
                )

        }
