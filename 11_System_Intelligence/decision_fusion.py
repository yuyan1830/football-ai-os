
from intelligence_fusion_engine import IntelligenceFusionEngine


class DecisionFusion:


    def __init__(self):

        self.engine=IntelligenceFusionEngine()


    def calculate(self,data):

        return self.engine.fuse(
            data["model"],
            data["reasoning"],
            data["memory"]
        )
