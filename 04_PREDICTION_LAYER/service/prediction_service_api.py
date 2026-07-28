class PredictionService:

    def predict(self,home,away):

        return {

        "home":home,
        "away":away,
        "fusion_probability":0.45,
        "confidence":"HIGH"

        }

