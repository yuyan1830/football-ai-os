
# -*- coding:utf-8 -*-


import os
import json



BASE_PATH=r"E:\football_v\10_AI_AUTONOMOUS_ENGINE"



def check(file):

    return os.path.exists(

        os.path.join(

            BASE_PATH,

            file

        )

    )



result={


"framework":

"Football AI OS",


"module":

"AI Autonomous Evolution Engine HIL V1.2",


"status":

"PASS",


"checks":{


"human_approval_manager.py":

check(

"human_approval_manager.py"

),


"approval_workflow.py":

check(

"approval_workflow.py"

),


"decision_logger.py":

check(

"decision_logger.py"

),


"config/human_approval_config.json":

check(

"config/human_approval_config.json"

)


}


}



for v in result["checks"].values():

    if not v:

        result["status"]="FAIL"



print(

json.dumps(

result,

indent=4,

ensure_ascii=False

)

)

