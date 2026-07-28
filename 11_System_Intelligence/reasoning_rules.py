
class ReasoningRules:


    def evaluate(self,data):

        result={}


        if data.get("risk",0)>0.7:

            result["decision"]="avoid"


        else:

            result["decision"]="continue"


        return result
