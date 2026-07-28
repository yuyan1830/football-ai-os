
class AgentManager:


    def __init__(self):

        self.agents=[]


    def register(self,agent):

        self.agents.append(agent)


    def run(self,data):

        return [
            a.analyze(data)
            for a in self.agents
        ]
