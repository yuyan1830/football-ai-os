
class EvolutionMemory:

    def __init__(self):
        self.records=[]


    def store(self,data):

        self.records.append(data)

        return {
            "stored":True,
            "count":len(self.records)
        }


    def latest(self):

        if not self.records:
            return None

        return self.records[-1]
