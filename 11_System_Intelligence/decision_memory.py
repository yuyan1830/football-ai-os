
class DecisionMemory:

    def __init__(self):
        self.records=[]

    def save(self,data):
        self.records.append(data)

    def history(self):
        return self.records
