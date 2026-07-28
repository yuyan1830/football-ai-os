
class IntelligenceWeightManager:


    def __init__(self):

        self.weights={
            "reasoning":0.4,
            "memory":0.3,
            "knowledge":0.3
        }


    def update(self,key,value):

        self.weights[key]=value


    def get(self):

        return self.weights
