
class PredictionAgent:


    def analyze(self,data):

        return {

            "agent":"prediction",

            "result":
                data.get(
                    "prediction",
                    None
                )

        }
