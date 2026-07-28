class ModelResultAdapter:


    def adapt(self, model_result):

        return {
            "model_result": model_result,
            "status": "adapted"
        }