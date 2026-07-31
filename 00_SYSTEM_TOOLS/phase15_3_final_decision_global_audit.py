from pathlib import Path


ROOT = Path(r"E:\football_v")

OUT = ROOT / r"99_DOCUMENTATION\checkpoints\Phase15_3_Final_Decision_Global_Audit.txt"


targets = [
    "AI_RUNTIME",
    "08_DECISION_LAYER",
    "12_API_LAYER",
    "13_TEST_LAYER",
    "00_SYSTEM_TOOLS",
    "deployment_scripts",
    "08_DECISION_ENGINE",
    "85_FINAL_DECISION_ENGINE"
]


keywords = [
    "final_decision",
    "DecisionEngine",
    "DecisionService",
    "decision_engine",
    "decision_service",
    "fallback",
    "run_decision",
    "DecisionEngineV32",
    "DecisionServiceV32"
]


report=[]

report.append(
"""
Football AI OS Ω+

Phase15.3 Final Decision Global Audit

Purpose:

Confirm single decision brain

==================================================

"""
)


for target in targets:

    path=ROOT/target

    report.append(
        "\n========== "
        + target
        + " ==========\n"
    )

    if not path.exists():

        report.append("NOT FOUND\n")
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
                +
                str(file.relative_to(ROOT))
                +
                "\n"
            )

            report.append(
                "KEYWORDS:"
                +
                ",".join(found)
                +
                "\n"
            )


            for i,line in enumerate(
                text.splitlines(),
                1
            ):

                if any(
                    k in line
                    for k in found
                ):

                    report.append(
                        f"{i}: {line.strip()}\n"
                    )


report.append(
"""

==================================================

Judgement Rules:


Allowed:

final_decision output field


Forbidden:

AI_RUNTIME independent decision calculation


Target:

AI_RUNTIME



DecisionServiceV32



DecisionEngineV32


==================================================

"""
)


OUT.write_text(
    "".join(report),
    encoding="utf-8"
)


print(OUT)

