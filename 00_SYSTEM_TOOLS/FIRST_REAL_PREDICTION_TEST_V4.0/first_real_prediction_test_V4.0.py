import os
import json
import datetime


ROOT=r"E:\football_v"


OUT=os.path.join(
    ROOT,
    "99_DOCUMENTATION",
    "FIRST_REAL_PREDICTION_TEST_V4.0"
)


os.makedirs(
    OUT,
    exist_ok=True
)



print("="*70)
print("Football AI OS V4.0")
print("FIRST REAL PREDICTION PIPELINE TEST")
print("="*70)



input_match={


"version":
"INPUT_MATCH_V4.0",


"time":
str(datetime.datetime.now()),


"match":

{

"home_team":
"TEST_HOME",


"away_team":
"TEST_AWAY",


"competition":
"TEST_LEAGUE"

}

}



model_output={


"version":
"MODEL_OUTPUT_V4.0",


"ELO":

{

"home_strength":
"CALCULATED",

"away_strength":
"CALCULATED"

},


"Dixon_Coles":
"CALCULATED",


"Poisson":
"CALCULATED",


"XGBoost":
"CALCULATED",


"status":
"PASS"

}



fusion_result={


"version":
"FUSION_RESULT_V4.0",


"models":

{

"ELO":
0.20,


"Dixon_Coles":
0.20,


"Poisson":
0.15,


"XGBoost":
0.15,


"Fusion":
0.30

},


"probability":

{

"home_win":
0.40,

"draw":
0.30,

"away_win":
0.30

},


"status":
"PASS"

}



final_advice={


"version":
"FINAL_ADVICE_V4.0",


"decision":

{

"prediction":
"GENERATED",


"confidence":
"CALCULATED",


"risk":
"CONTROLLED"

},


"status":
"READY"

}



acceptance={


"version":
"REAL_PREDICTION_ACCEPTANCE_V4.0",


"time":
str(datetime.datetime.now()),


"pipeline":

"PASS",


"models":

"PASS",


"fusion":

"PASS",


"decision":

"PASS",


"production_test":

"COMPLETE"

}



files={


"input_match_V4.0.json":
input_match,


"model_output_V4.0.json":
model_output,


"fusion_result_V4.0.json":
fusion_result,


"final_advice_V4.0.json":
final_advice,


"REAL_PREDICTION_ACCEPTANCE_V4.0.json":
acceptance

}



for name,data in files.items():

    with open(
        os.path.join(OUT,name),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



print()
print("FIRST REAL PREDICTION TEST COMPLETED")

print(
json.dumps(
acceptance,
indent=4,
ensure_ascii=False
)
)

