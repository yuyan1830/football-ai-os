
class RuleOptimizer:


    def optimize(self,error):

        if error>0.5:

            return {
                "action":"increase_learning"
            }

        return {
            "action":"keep"
        }
