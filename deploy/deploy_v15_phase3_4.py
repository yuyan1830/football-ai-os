import os
import json


ROOT = r"E:\football_v\11_System_Intelligence"


files = {

"decision_context.py":'''
class DecisionContext:

    def __init__(self):
        self.memory={}
        self.reasoning={}
        self.models={}

    def update(self,key,value):
        self.memory[key]=value

    def get(self,key):
        return self.memory.get(key)
''',


"decision_memory.py":'''
class DecisionMemory:

    def __init__(self):
        self.records=[]

    def save(self,data):
        self.records.append(data)

    def history(self):
        return self.records
''',


"intelligence_fusion_engine.py":'''
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
''',


"decision_fusion.py":'''
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
'''
}



for name,content in files.items():

    path=os.path.join(ROOT,name)

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)



test_dir=os.path.join(ROOT,"tests")


test_file=os.path.join(
    test_dir,
    "test_phase3_4_decision_fusion.py"
)


test='''

from decision_fusion import DecisionFusion


def test_decision_fusion():

    engine=DecisionFusion()

    result=engine.calculate({

        "model":0.6,
        "reasoning":0.7,
        "memory":0.8

    })


    assert result>0


'''


with open(test_file,"w",encoding="utf-8") as f:

    f.write(test)



report={
"phase":"3.4",
"module":"Decision Fusion",
"status":"deployed"
}


with open(
os.path.join(ROOT,"reports","phase3_4_decision_fusion_report.json"),
"w",
encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )


print(
"""
==================================
Phase3.4 Decision Fusion Deployment Complete
==================================
"""
)