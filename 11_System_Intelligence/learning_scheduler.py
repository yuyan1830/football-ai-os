
class LearningScheduler:


    def __init__(self):

        self.tasks=[]



    def add(self,task):

        self.tasks.append(task)



    def run(self):

        return len(self.tasks)
