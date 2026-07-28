
class IntelligenceFeedbackLoop:


    def __init__(self):

        self.history=[]


    def record(self,data):

        self.history.append(data)


    def size(self):

        return len(self.history)
