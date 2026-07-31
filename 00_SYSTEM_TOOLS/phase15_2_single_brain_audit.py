# -*- coding: utf-8 -*-

from pathlib import Path


ROOT = Path(r"E:\football_v")

OUT = ROOT / r"99_DOCUMENTATION\checkpoints\Phase15_2_Single_Brain_Cleanup_Audit_Report.txt"


scan_paths = [

    "AI_RUNTIME",

    "06_PREDICTION_ENGINE",

    "06_PREDICTION_INTELLIGENCE_ENGINE",

    "08_DECISION_LAYER",

    "09_Prediction_System",

    "12_API_LAYER",

    "13_OUTPUT_SERVICE_LAYER",

    "00_SYSTEM_TOOLS",

    "deployment_scripts"

]


keywords = [

    "final_decision",

    "DecisionEngine",

    "DecisionService",

    "decision_engine",

    "prediction_engine",

    "prediction_service",

    "run_prediction",

    "run_ai_runtime",

    "SourceFileLoader",

    "decision_service_V3.2",

    "decision_engine_V3.2",

    "decision_service_v32",

    "decision_engine_v32"

]


report=[]


report.append(
"""
Football AI OS Ω+

Phase15.2 Single Brain Architecture Cleanup Audit

Purpose:

Remove duplicate decision brain
Remove duplicate prediction path
Confirm single production architecture

==================================================

"""
)


for path_name in scan_paths:


    path = ROOT / path_name


    report.append(
        "\n\n========== "
        + path_name
        + " ==========\n"
    )


    if not path.exists():

        report.append(
            "NOT FOUND\n"
        )

        continue


    for file in path.rglob("*.py"):


        try:

            text=file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        except:

            continue


        matched=[]


        for key in keywords:

            if key in text:

                matched.append(key)


        if matched:


            report.append(
                "\nFILE:\n"
            )

            report.append(
                str(file.relative_to(ROOT))
                +
                "\n"
            )


            report.append(
                "MATCH:\n"
            )

            report.append(
                ",".join(matched)
                +
                "\n"
            )


            for index,line in enumerate(
                text.splitlines(),
                1
            ):


                if any(
                    k in line
                    for k in matched
                ):

                    report.append(
                        f"{index}: {line.strip()}\n"
                    )


report.append(
"""

==================================================

Architecture Judgment Target:

ONLY ONE DECISION BRAIN:


AI_RUNTIME



decision_service_bridge.py



08_DECISION_LAYER/service/decision_service_v32.py



08_DECISION_LAYER/engine/decision_engine_v32.py


ONLY ONE PREDICTION ENTRY:


API



AI_RUNTIME



MODEL OUTPUTS



MODEL FUSION



DECISION


==================================================

"""
)


OUT.write_text(
    "".join(report),
    encoding="utf-8"
)


print("Generated:")
print(OUT)

