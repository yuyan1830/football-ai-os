
class LearningMemory:


    def __init__(self):

        self.memory=[]



    def save(self,data):

        self.memory.append(data)



    def recall(self):

        return self.memory
