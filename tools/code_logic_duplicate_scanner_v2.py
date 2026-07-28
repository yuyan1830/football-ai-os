import os
import re
import json
import hashlib
from datetime import datetime
from collections import defaultdict


ROOT = r"E:\football_v"

OUTPUT = (
    r"E:\football_v\reports"
    r"\CODE_LOGIC_DUPLICATE_AUDIT_V2.0.json"
)


TARGET_DIRS = [

"03_MODEL_LAYER",
"04_Data_Processing_AI",
"07_BACKTEST_AI",
"11_SIMULATION_LAYER",
"12_API_LAYER",
"13_TEST_LAYER",
"14_OPERATION_LAYER",
"24_PREDICTION_INTELLIGENCE_LAYER",
"27_MODEL_FUSION_ENGINE",
"28_PROBABILITY_CALIBRATION_ENGINE",
"29_DECISION_ENGINE",
"30_MARKET_GAME_ENGINE",
"38_HANDICAP_VALUE_ENGINE",
"39_MARKET_SENTIMENT_ENGINE",
"40_MATCH_PREDICTION_ENGINE",
"44_PRODUCTION_PREDICTION_RUNTIME"

]


def get_files():

    result=[]

    for d in TARGET_DIRS:

        path=os.path.join(ROOT,d)

        if not os.path.exists(path):
            continue


        for root,dirs,files in os.walk(path):

            for f in files:

                if f.endswith(".py"):

                    result.append(
                        os.path.join(root,f)
                    )

    return result



def extract_functions(code):

    funcs=[]

    matches=re.findall(
        r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        code
    )

    for m in matches:

        funcs.append(m)

    return funcs



def extract_classes(code):

    return re.findall(
        r"class\s+([a-zA-Z_][a-zA-Z0-9_]*)",
        code
    )



def normalize_block(code):

    code=re.sub(
        r"\s+",
        " ",
        code
    )

    code=re.sub(
        r"#.*?",
        "",
        code
    )

    return code.strip()



def block_hash(code):

    return hashlib.md5(
        normalize_block(code)
        .encode(
            "utf-8",
            errors="ignore"
        )
    ).hexdigest()



def scan():

    files=get_files()


    function_map=defaultdict(list)

    class_map=defaultdict(list)

    code_map=defaultdict(list)


    for file in files:

        try:

            with open(
                file,
                encoding="utf-8",
                errors="ignore"
            ) as f:

                code=f.read()


            for fn in extract_functions(code):

                function_map[fn].append(file)


            for cls in extract_classes(code):

                class_map[cls].append(file)


            h=block_hash(code)

            code_map[h].append(file)


        except:
            pass



    function_duplicates=[]

    for k,v in function_map.items():

        if len(v)>1:

            function_duplicates.append(
            {
                "function":k,
                "files":v,
                "risk":"REVIEW"
            })



    class_duplicates=[]

    for k,v in class_map.items():

        if len(v)>1:

            class_duplicates.append(
            {
                "class":k,
                "files":v,
                "risk":"REVIEW"
            })


    report={

        "version":
        "CODE_LOGIC_DUPLICATE_AUDIT_V2.0",

        "time":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),


        "scan_files":
        len(files),


        "summary":
        {

        "function_duplicate_groups":
        len(function_duplicates),

        "class_duplicate_groups":
        len(class_duplicates)

        },


        "function_duplicates":
        function_duplicates,


        "class_duplicates":
        class_duplicates,


        "merge_candidates":[],

        "delete_candidates":[]

    }


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print("="*60)
    print("Football AI OS Code Logic Duplicate Scanner V2.0")
    print("="*60)
    print("扫描文件:",len(files))
    print("函数重复组:",
          len(function_duplicates))
    print("类重复组:",
          len(class_duplicates))
    print("报告:")
    print(OUTPUT)
    print("="*60)



if __name__=="__main__":
    scan()

