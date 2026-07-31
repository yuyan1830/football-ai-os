# -*- coding: utf-8 -*-

import os
from pathlib import Path


ROOT = Path(r"E:\football_v")


OUTPUT = ROOT / r"99_DOCUMENTATION\checkpoints\Phase14_4_Runtime_API_Output_Audit_Report.txt"


targets = [

    "AI_RUNTIME",

    "08_DECISION_LAYER",

    "12_API_LAYER",

    "13_OUTPUT_SERVICE_LAYER",

    "13_TEST_LAYER",

    "00_SYSTEM_TOOLS"

]


keywords = [

    "AI_RUNTIME",

    "run_prediction",

    "decision_service",

    "DecisionService",

    "DecisionEngine",

    "final_decision",

    "decision_layer",

    "generate_output",

    "prediction",

    "SourceFileLoader",

    "V3.2",

    "v32"

]


lines=[]


lines.append(
"Football AI OS Ω+ Phase14.4 Runtime API Output Audit\n"
)

lines.append(
"====================================================\n\n"
)


for target in targets:


    path = ROOT / target


    lines.append(
        "\n\n========== "
        + target
        + " ==========\n"
    )


    if not path.exists():

        lines.append(
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



        matches=[]


        for key in keywords:

            if key in text:

                matches.append(key)



        if matches:


            lines.append(
                "\nFILE:\n"
                + str(file.relative_to(ROOT))
                + "\n"
            )


            lines.append(
                "MATCH:\n"
                + ",".join(matches)
                + "\n"
            )


            for i,line in enumerate(
                text.splitlines(),
                1
            ):

                for key in matches:

                    if key in line:

                        lines.append(
                            f"{i}: {line.strip()}\n"
                        )



# tree summary

lines.append(
"\n\n========== DIRECTORY SUMMARY ==========\n"
)


for target in targets:


    path=ROOT / target


    lines.append(
        "\n[" + target + "]\n"
    )


    if path.exists():

        for item in path.rglob("*"):

            if item.is_file():

                lines.append(
                    str(item.relative_to(ROOT))
                    + "\n"
                )



OUTPUT.write_text(
    "".join(lines),
    encoding="utf-8"
)


print(
    "Audit completed:"
)

print(
    OUTPUT
)

