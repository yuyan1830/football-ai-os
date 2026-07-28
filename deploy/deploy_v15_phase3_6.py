import os
import json


BASE = r"E:\football_v\11_System_Intelligence"


def write_file(path, content):

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)



# ==============================
# Self Learning Engine
# ==============================

write_file(

os.path.join(BASE,"self_learning_engine.py"),

r'''
class SelfLearningEngine:


    def __init__(self):

        self.history=[]


    def learn(self,prediction,result):

        error = abs(
            prediction-result
        )

        record={

            "prediction":
            prediction,

            "result":
            result,

            "error":
            error
        }


        self.history.append(record)

        return record



    def score(self):

        if not self.history:
            return 0


        total=0

        for item in self.history:

            total+=item["error"]


        return round(
            1-total/len(self.history),
            4
        )
'''
)



# ==============================
# Learning Memory
# ==============================


write_file(

os.path.join(BASE,"learning_memory.py"),

r'''
class LearningMemory:


    def __init__(self):

        self.memory=[]



    def save(self,data):

        self.memory.append(data)



    def recall(self):

        return self.memory
'''
)



# ==============================
# Model Optimizer
# ==============================


write_file(

os.path.join(BASE,"model_optimizer.py"),

r'''
class ModelOptimizer:


    def __init__(self):

        self.weights={

            "elo":0.25,

            "poisson":0.25,

            "dixon_coles":0.25,

            "xgboost":0.25

        }



    def optimize(self,score):


        if score>0.7:

            self.weights["xgboost"]+=0.03


        elif score<0.5:

            self.weights["xgboost"]-=0.03



        total=sum(
            self.weights.values()
        )


        for k in self.weights:

            self.weights[k]=round(
                self.weights[k]/total,
                4
            )


        return self.weights
'''
)



# ==============================
# Adaptive Feedback
# ==============================


write_file(

os.path.join(BASE,"adaptive_feedback.py"),

r'''
class AdaptiveFeedback:


    def analyze(self,error):

        if error>0.5:

            return {

            "adjust":
            "increase historical analysis"

            }


        return {

        "adjust":
        "stable"

        }
'''
)



# ==============================
# Learning Scheduler
# ==============================


write_file(

os.path.join(BASE,"learning_scheduler.py"),

r'''
class LearningScheduler:


    def __init__(self):

        self.tasks=[]



    def add(self,task):

        self.tasks.append(task)



    def run(self):

        return len(self.tasks)
'''
)



# ==============================
# Test
# ==============================


test_code=r'''
from self_learning_engine import SelfLearningEngine
from model_optimizer import ModelOptimizer


def test_self_learning():

    engine=SelfLearningEngine()


    result=engine.learn(
        0.8,
        1
    )


    assert result["error"]==0.2



def test_optimizer():

    opt=ModelOptimizer()


    result=opt.optimize(
        0.8
    )


    assert "xgboost" in result
'''



write_file(

os.path.join(
BASE,
"tests",
"test_phase3_6_self_learning.py"
),

test_code

)



# ==============================
# Report
# ==============================


report={

"phase":

"Phase3.6 Self Learning",


"status":

"completed",


"modules":[

"self_learning_engine.py",

"learning_memory.py",

"model_optimizer.py",

"adaptive_feedback.py",

"learning_scheduler.py"

]

}



write_file(

os.path.join(
BASE,
"reports",
"phase3_6_self_learning_report.json"
),

json.dumps(
report,
indent=4,
ensure_ascii=False
)

)



print(
"Phase3.6 Self Learning Deployment Complete"
)