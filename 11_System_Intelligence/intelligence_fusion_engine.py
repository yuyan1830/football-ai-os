
class IntelligenceFusionEngine:


    def fuse(self,
             model_probability,
             reasoning_score,
             memory_score):

        result = (
            model_probability*0.5+
            reasoning_score*0.3+
            memory_score*0.2
        )

        return round(result,4)
