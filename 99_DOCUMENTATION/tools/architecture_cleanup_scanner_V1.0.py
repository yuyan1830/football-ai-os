import os
import json
import ast
from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[2]

REPORT_DIR = ROOT / "99_DOCUMENTATION" / "reports"


python_files = []
modules = []
functions = []
imports = []


IGNORE = {
    "__pycache__",
    ".git",
    "venv",
    "env"
}


def scan_python():

    for path in ROOT.rglob("*.py"):

        if any(x in path.parts for x in IGNORE):
            continue

        python_files.append(str(path))

        try:

            tree = ast.parse(
                path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )

            module_name = path.stem

            modules.append(
                {
                    "file":str(path),
                    "module":module_name
                }
            )


            for node in ast.walk(tree):

                if isinstance(node,ast.FunctionDef):

                    functions.append(
                        {
                            "module":module_name,
                            "function":node.name,
                            "file":str(path)
                        }
                    )


                if isinstance(node,ast.Import):

                    for item in node.names:

                        imports.append(
                            {
                                "file":str(path),
                                "import":item.name
                            }
                        )


                if isinstance(node,ast.ImportFrom):

                    if node.module:

                        imports.append(
                            {
                                "file":str(path),
                                "import":node.module
                            }
                        )


        except Exception:
            pass



def duplicate_scan():

    keywords=[
        "prediction",
        "predict",
        "forecast",
        "runtime",
        "engine",
        "fusion",
        "feature",
        "market",
        "decision",
        "report",
        "validator"
    ]

    result=[]


    for key in keywords:

        group=[]

        for m in modules:

            name=m["module"].lower()

            if key in name:

                group.append(
                    m["file"]
                )


        if len(group)>1:

            result.append(
                {
                    "keyword":key,
                    "count":len(group),
                    "files":group,
                    "recommendation":
                    "review_merge"
                }
            )


    return result



def save():

    cleanup={
        "generated":
            datetime.now().isoformat(),

        "total_python_files":
            len(python_files),

        "total_modules":
            len(modules),

        "total_functions":
            len(functions),

        "duplicate_candidates":
            duplicate_scan()
    }


    module_map={
        "modules":modules,
        "imports":imports
    }


    dup={
        "duplicates":
            duplicate_scan()
    }


    (REPORT_DIR /
     "Architecture_Cleanup_Report_V1.0.json"
    ).write_text(
        json.dumps(
            cleanup,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    (REPORT_DIR /
     "Architecture_Module_Map_V1.0.json"
    ).write_text(
        json.dumps(
            module_map,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


    (REPORT_DIR /
     "Architecture_Duplicate_Report_V1.0.json"
    ).write_text(
        json.dumps(
            dup,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


if __name__=="__main__":

    scan_python()
    save()

    print("==============================")
    print("Architecture Cleanup Scanner")
    print("==============================")
    print(
        "Python Files:",
        len(python_files)
    )
    print(
        "Modules:",
        len(modules)
    )
    print(
        "Functions:",
        len(functions)
    )
    print("==============================")
    print("Reports Generated")
