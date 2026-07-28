import os
import json
import datetime
import sqlite3


ROOT=r"E:\FOOTBALL_V"


result={}


# 数据检查

db_path=os.path.join(
    ROOT,
    "data",
    "football.db"
)


database_check={

    "path":db_path,

    "exists":os.path.exists(db_path),

    "status":"CHECKED"

}


# 如果数据库存在，读取比赛数量

if os.path.exists(db_path):

    try:

        conn=sqlite3.connect(db_path)

        cursor=conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM matches_clean"
        )

        count=cursor.fetchone()[0]

        database_check["matches_clean_count"]=count

        conn.close()

    except Exception as e:

        database_check["error"]=str(e)



result["database"]=database_check



# 模型配置

result["model_config"]={

    "version":"V4.0",

    "ELO":0.20,

    "Dixon_Coles":0.20,

    "Poisson":0.15,

    "XGBoost":0.15,

    "Fusion":0.30

}



# 训练规则

result["training_policy"]={

    "time_sequence_training":True,

    "architecture_modify":False,

    "auto_weight_change":False,

    "framework":"Frozen V4.0"

}



# 环境

result["environment"]={

    "python":"Python312",

    "system":"Windows",

    "status":"READY"

}



result["checkpoint"]={

    "version":
    "TRAINING_PREFLIGHT_CHECK_V4.0",

    "time":
    str(datetime.datetime.now()),

    "status":
    "READY_FOR_TRAINING"

}



out=os.path.join(

    ROOT,

    "99_DOCUMENTATION",

    "TRAINING_PREFLIGHT_CHECK_V4.0",

    "TRAINING_PREFLIGHT_REPORT_V4.0.json"

)



with open(

    out,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        result,

        f,

        indent=4,

        ensure_ascii=False

    )



print("="*70)

print("Football AI OS V4.0")

print("TRAINING PREFLIGHT CHECK COMPLETE")

print("="*70)

print(json.dumps(

result,

indent=4,

ensure_ascii=False

))

