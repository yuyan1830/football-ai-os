
class ReasoningContext:

    def __init__(self):
        self.memory={}
        self.knowledge={}
        self.history=[]


    def update(self,key,value):
        self.memory[key]=value


    def add_history(self,item):
        self.history.append(item)


    def snapshot(self):

        return {
            "memory":self.memory,
            "knowledge":self.knowledge,
            "history":self.history
        }
