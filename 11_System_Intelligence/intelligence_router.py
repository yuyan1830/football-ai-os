
class IntelligenceRouter:


    def route(self,context):

        if context.get("risk"):
            return "risk_reasoning"

        return "normal_reasoning"
