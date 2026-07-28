import json
from datetime import datetime


files=[
r"E:\football_v\31_SELF_LEARNING_ENGINE\feedback_engine.py",
r"E:\football_v\31_SELF_LEARNING_ENGINE\model_update_engine.py"
]


result={

"version":
"FOOTBALL_AI_OS_V4.0_SELF_LEARNING_ENGINE_AUDIT",

"time":
str(datetime.now()),

"files":{}

}


for file in files:

    data={

    "exists":False,
    "classes":[],
    "functions":[],
    "database_reference":False,
    "model_update_reference":False

    }


    try:

        with open(file,"r",encoding="utf-8") as f:

            text=f.read()


        data["exists"]=True


        for line in text.splitlines():

            line=line.strip()


            if line.startswith("class "):

                data["classes"].append(line)


            if line.startswith("def "):

                data["functions"].append(line)


            if "sqlite" in line.lower():

                data["database_reference"]=True


            if "update" in line.lower() or "model" in line.lower():

                data["model_update_reference"]=True


    except Exception as e:

        data["error"]=str(e)


    result["files"][file]=data


print(
json.dumps(
result,
ensure_ascii=False,
indent=4
)
)


out=r"E:\football_v\reports\V4_SELF_LEARNING_ENGINE_AUDIT.json"


with open(out,"w",encoding="utf-8") as f:

    json.dump(
    result,
    f,
    ensure_ascii=False,
    indent=4
    )

