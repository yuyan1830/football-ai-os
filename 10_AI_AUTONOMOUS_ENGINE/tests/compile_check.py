import os
import ast


BASE = r"E:\football_v\10_AI_AUTONOMOUS_ENGINE"


for f in os.listdir(BASE):

    if f.endswith(".py"):

        path = os.path.join(BASE,f)

        try:

            with open(
                path,
                encoding="utf-8"
            ) as source:

                ast.parse(
                    source.read()
                )


            print(
                "PASS:",
                f
            )


        except Exception as e:

            print(
                "\nERROR:",
                f
            )

            print(e)