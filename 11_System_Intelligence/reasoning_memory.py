
class ReasoningMemory:


    def __init__(self):

        self.records=[]


    def store(self,data):

        self.records.append(data)


    def query(self):

        return self.records


    def latest(self):

        if self.records:
            return self.records[-1]

        return None
