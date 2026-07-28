import os
import json
import ast
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(r"E:\football_v")

REPORT_PATH = (
    PROJECT_ROOT
    / "99_DOCUMENTATION"
    / "reports"
    / "PHASE5_RUNTIME_DEPENDENCY_AUDIT_V1.0.json"
)


SCAN_MODULES = [
    "04_Data_Processing_AI",
    "05_MODEL_AI",
    "06_PREDICTION_ENGINE",
    "07_BACKTEST_AI",
    "08_DECISION_ENGINE",
    "17_MODEL_STORE_LAYER",
    "18_MODEL_EXECUTION_ENGINE",
]


KEYWORDS = [
    "fusion",
    "registry",
    "model_loader",
    "prediction_pipeline",
    "feedback",
    "optimization",
    "elo",
    "dixon",
    "poisson",
    "xgboost",
]


def scan_python_imports(file_path):

    result = []

    try:
        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(content)

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for item in node.names:
                    result.append(item.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    result.append(node.module)

    except Exception:
        pass

    return result



def scan_modules():

    result = {}

    for module in SCAN_MODULES:

        module_path = PROJECT_ROOT / module

        result[module] = {

            "exists": module_path.exists(),

            "python_files": 0,

            "imports": [],

            "keyword_hits": []

        }

        if not module_path.exists():
            continue


        for file in module_path.rglob("*.py"):

            result[module]["python_files"] += 1


            imports = scan_python_imports(file)

            result[module]["imports"].extend(
                imports
            )


            text = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )


            for key in KEYWORDS:

                if key.lower() in text.lower():

                    result[module]["keyword_hits"].append(
                        {
                            "file": str(file.relative_to(PROJECT_ROOT)),
                            "keyword": key
                        }
                    )


    return result



def check_runtime_paths():

    paths = {

        "fusion_engine":

        [
            r"05_MODEL_AI\MODEL_LAYER\fusion",
            r"18_MODEL_EXECUTION_ENGINE\fusion_engine"
        ],


        "model_registry":

        [
            r"05_MODEL_AI\MODEL_LAYER\model_registry.py",
            r"17_MODEL_STORE_LAYER\model_registry"
        ],


        "prediction_pipeline":

        [
            r"18_MODEL_EXECUTION_ENGINE\prediction_pipeline"
        ],


        "feedback":

        [
            r"07_BACKTEST_AI\model_feedback.py",
            r"07_BACKTEST_AI\optimization_scheduler.py"
        ]

    }


    result={}


    for name, items in paths.items():

        result[name]=[]

        for item in items:

            p = PROJECT_ROOT / item

            result[name].append(
                {
                    "path":item,
                    "exists":p.exists()
                }
            )

    return result



def main():

    report={

        "project":
            "Football AI OS",

        "architecture":
            "Omega V3.2",

        "phase":
            "PHASE5 Runtime Dependency Audit",

        "time":
            datetime.now().isoformat(),

        "modules":
            scan_modules(),

        "runtime_paths":
            check_runtime_paths()

    }


    REPORT_PATH.parent.mkdir(
        exist_ok=True
    )


    REPORT_PATH.write_text(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    print(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False
        )
    )


    print(
        "\nREPORT:"
    )

    print(
        REPORT_PATH
    )


if __name__ == "__main__":

    main()