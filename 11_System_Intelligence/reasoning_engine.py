
from reasoning_rules import ReasoningRules


class ReasoningEngine:


    def __init__(self):

        self.rules=ReasoningRules()



    def reason(self,context):

        result=self.rules.evaluate(context)

        return result
