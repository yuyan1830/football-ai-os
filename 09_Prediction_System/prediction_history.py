class PredictionHistory:

    def __init__(self):
        self.records=[]


    def save(self,data):
        self.records.append(data)