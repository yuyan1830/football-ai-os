import os

ROOT = r"E:\football_v"

EXCLUDE = {
    ".venv",
    "venv",
    "__pycache__",
    "site-packages",
    ".git",
    "node_modules"
}

KEYWORDS = [
    "import ",
    "from ",
    "sqlite",
    "database",
    "db_path",
    "connect(",
    "load",
    "save",
    "registry",
    "pipeline",
    "execute"
]


OUTPUT = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Phase6_Dependency_Clean_Report_V1.0.txt"


with open(OUTPUT,"w",encoding="utf-8") as out:

    count = 0

    for root,dirs,files in os.walk(ROOT):

        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDE
        ]

        for file in files:

            if not file.endswith((".py",".json",".yaml",".yml",".md")):
                continue

            path=os.path.join(root,file)

            try:
                with open(path,"r",encoding="utf-8",errors="ignore") as f:
                    lines=f.readlines()

                for i,line in enumerate(lines,1):

                    for k in KEYWORDS:

                        if k.lower() in line.lower():

                            out.write(
                                f"{path}:{i}\n"
                            )
                            out.write(
                                line.strip()+"\n\n"
                            )

                            count+=1
                            break

            except:
                pass


    out.write("\n====================\n")
    out.write(
        f"TOTAL HITS:{count}\n"
    )

print("DONE")
print(OUTPUT)