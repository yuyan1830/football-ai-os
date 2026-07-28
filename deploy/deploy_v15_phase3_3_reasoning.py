import os
import json


BASE = r"E:\football_v\11_System_Intelligence"


files = {


"reasoning_context.py":'''
class ReasoningContext:

    def __init__(self):
        self.memory={}
        self.knowledge={}
        self.history=[]


    def update(self,key,value):
        self.memory[key]=value


    def add_history(self,item):
        self.history.append(item)


    def snapshot(self):

        return {
            "memory":self.memory,
            "knowledge":self.knowledge,
            "history":self.history
        }
''',


"reasoning_memory.py":'''
class ReasoningMemory:


    def __init__(self):

        self.records=[]


    def store(self,data):

        self.records.append(data)


    def query(self):

        return self.records


    def latest(self):

        if self.records:
            return self.records[-1]

        return None
''',


"reasoning_rules.py":'''
class ReasoningRules:


    def evaluate(self,data):

        result={}


        if data.get("risk",0)>0.7:

            result["decision"]="avoid"


        else:

            result["decision"]="continue"


        return result
''',


"reasoning_engine.py":'''
from reasoning_rules import ReasoningRules


class ReasoningEngine:


    def __init__(self):

        self.rules=ReasoningRules()



    def reason(self,context):

        result=self.rules.evaluate(context)

        return result
''',



"decision_reasoner.py":'''
from reasoning_engine import ReasoningEngine


class DecisionReasoner:


    def __init__(self):

        self.engine=ReasoningEngine()



    def decide(self,data):

        return self.engine.reason(data)
''',



"intelligence_report.py":'''
import json
import os


class IntelligenceReport:


    def generate(self,data,path):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
''',



"tests/test_phase3_3_reasoning.py":'''
from reasoning_engine import ReasoningEngine
from decision_reasoner import DecisionReasoner


def test_reasoning_engine():

    engine=ReasoningEngine()

    result=engine.reason(
        {
            "risk":0.2
        }
    )

    assert result["decision"]=="continue"



def test_decision_reasoner():

    d=DecisionReasoner()

    result=d.decide(
        {
            "risk":0.9
        }
    )

    assert result["decision"]=="avoid"
'''
}



for path,content in files.items():


    full=os.path.join(BASE,path)


    if "/" in path:

        os.makedirs(
            os.path.dirname(full),
            exist_ok=True
        )


    else:

        os.makedirs(
            BASE,
            exist_ok=True
        )


    with open(
        full,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)



report={

"phase":"3.3",

"module":"Reasoning Intelligence",

"status":"deployed"

}



with open(
os.path.join(
BASE,
"reports",
"phase3_3_reasoning_report.json"
),
"w",
encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )



print(
"Phase3.3 Reasoning Deployment Complete"
)