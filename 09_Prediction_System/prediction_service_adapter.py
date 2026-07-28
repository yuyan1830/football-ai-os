class PredictionServiceAdapter:


    def execute(self, data):

        return {
            "prediction": data,
            "service":"connected"
        }