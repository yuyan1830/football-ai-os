class PredictionPipeline:

    def run(self, match):

        result = {
            "match": match,
            "status": "processed"
        }

        return result