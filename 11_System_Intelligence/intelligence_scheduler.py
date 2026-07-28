
class IntelligenceScheduler:

    def __init__(self):
        self.tasks=[]

    def register(self,task):
        self.tasks.append(task)

    def run(self):
        return {
            "tasks":len(self.tasks),
            "status":"running"
        }
