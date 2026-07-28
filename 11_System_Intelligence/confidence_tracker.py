
class ConfidenceTracker:


    def __init__(self):

        self.history=[]


    def add(self,value):

        self.history.append(value)

        return True
