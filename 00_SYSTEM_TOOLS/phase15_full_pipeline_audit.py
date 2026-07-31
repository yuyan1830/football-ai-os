# -*- coding: utf-8 -*-

from pathlib import Path


ROOT = Path(r"E:\football_v")


OUTPUT = ROOT / r"99_DOCUMENTATION\checkpoints\Phase15_Full_Prediction_Pipeline_Audit_Report.txt"


targets = [

    "AI_RUNTIME",

    "08_DECISION_LAYER",

    "12_API_LAYER",

    "13_OUTPUT_SERVICE_LAYER",

    "13_TEST_LAYER",

    "06_PREDICTION_ENGINE",

    "06_PREDICTION_INTELLIGENCE_ENGINE",

    "00_SYSTEM_TOOLS"

]


keywords = [

    "run_prediction",

    "run_models",

    "fusion_predict",

    "model_outputs",

    "DecisionService",

    "DecisionEngine",

    "decision_layer",

    "final_decision",

    "generate_output",

    "run_ai_runtime",

    "prediction",

    "router",

    "runtime",

    "API",

    "SourceFileLoader",

    "V3.2",

    "v32"

]


report=[]


report.append(
"Football AI OS Ω+ Phase15 Full Prediction Pipeline Audit\n"
)

report.append(
"====================================================\n\n"
)



for target in targets:


    path = ROOT / target


    report.append(
        "\n\n========== "
        + target
        + " ==========\n"
    )


    if not path.exists():

        report.append(
            "PATH NOT FOUND\n"
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



        found=[]


        for key in keywords:

            if key in text:

                found.append(key)



        if found:


            report.append(
                "\nFILE:\n"
            )

            report.append(
                str(file.relative_to(ROOT))
                +
                "\n"
            )


            report.append(
                "KEYWORDS:\n"
            )

            report.append(
                ",".join(found)
                +
                "\n"
            )


            for number,line in enumerate(
                text.splitlines(),
                1
            ):


                if any(
                    key in line
                    for key in found
                ):

                    report.append(
                        f"{number}: {line.strip()}\n"
                    )



report.append(
"\n\n========== DIRECTORY SUMMARY ==========\n"
)



for target in targets:


    path=ROOT / target


    report.append(
        "\n["+
        target+
        "]\n"
    )


    if path.exists():

        for item in path.rglob("*"):

            if item.is_file():

                report.append(
                    str(item.relative_to(ROOT))
                    +
                    "\n"
                )



OUTPUT.write_text(
    "".join(report),
    encoding="utf-8"
)


print(
    "Audit Generated:"
)

print(
    OUTPUT
)

