
class SelfLearningEngine:


    def __init__(self):

        self.history=[]


    def learn(self,prediction,result):

        error = round(abs(prediction-result),4)

        record={

            "prediction":
            prediction,

            "result":
            result,

            "error":
            error
        }


        self.history.append(record)

        return record



    def score(self):

        if not self.history:
            return 0


        total=0

        for item in self.history:

            total+=item["error"]


        return round(
            1-total/len(self.history),
            4
        )

