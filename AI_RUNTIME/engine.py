from .model_connector import check_database
from .model_runtime_connector import model_runtime_check
from .prediction_executor import run_prediction



def execute(task, message):


    prediction={}


    if task=="MATCH_ANALYSIS":


        home=""
        away=""


        if ":" in message:

            parts=message.split(":")

            if len(parts)>=3:

                home=parts[1].strip()
                away=parts[2].strip()


        if home and away:

            prediction=run_prediction(
                home,
                away
            )

        else:

            prediction={
                "message":
                "等待比赛参数"
            }


    return {


        "task":task,


        "database_status":
            check_database(),


        "model_runtime":
            model_runtime_check(),


        "prediction":
            prediction,


        "status":
            "PREDICTION_ENGINE_READY"

    }

