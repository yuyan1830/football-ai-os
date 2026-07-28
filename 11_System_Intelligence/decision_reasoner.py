
from reasoning_engine import ReasoningEngine


class DecisionReasoner:


    def __init__(self):

        self.engine=ReasoningEngine()



    def decide(self,data):

        return self.engine.reason(data)
