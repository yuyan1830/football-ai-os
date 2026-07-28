import os
import json
import ast
from datetime import datetime


ROOT = r"E:\football_v"

REPORT_DIR = (
    r"E:\football_v\99_DOCUMENTATION"
    r"\architecture_cleanup\reports"
)


SCAN_EXT = (
    ".py",
    ".ps1",
    ".json",
    ".yaml",
    ".yml"
)


KEEP_PATH = [
    "archive",
    "registry",
    "config",
    "manifest",
    "FINAL_RELEASE_REPORT"
]


def collect_files():

    result=[]

    for root,dirs,files in os.walk(ROOT):

        for f in files:

            if f.endswith(SCAN_EXT):

                result.append(
                    os.path.join(root,f)
                )

    return result



def python_symbol_scan(file):

    symbols=[]

    try:

        with open(
            file,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            tree=ast.parse(
                f.read()
            )


        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                symbols.append(
                    {
                        "type":"function",
                        "name":node.name
                    }
                )


            if isinstance(
                node,
                ast.ClassDef
            ):

                symbols.append(
                    {
                        "type":"class",
                        "name":node.name
                    }
                )


            if isinstance(
                node,
                ast.Import
            ):

                for n in node.names:

                    symbols.append(
                        {
                            "type":"import",
                            "name":n.name
                        }
                    )


            if isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    symbols.append(
                        {
                            "type":"from_import",
                            "name":node.module
                        }
                    )


    except Exception:

        pass


    return symbols



def text_reference_scan(
        files,
        symbols
):

    refs=[]


    for file in files:


        try:

            with open(
                file,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                text=f.read()


        except:

            continue



        for symbol in symbols:


            name=symbol["name"]


            if len(name)<4:

                continue


            if name in text:


                refs.append(
                    {
                        "source":file,
                        "target":name,
                        "type":symbol["type"]
                    }
                )


    return refs



def build_dependency_graph(files):

    nodes=[]

    edges=[]


    for file in files:

        nodes.append(file)


        if file.endswith(".py"):

            symbols=python_symbol_scan(file)


            for s in symbols:

                if s["type"] in (
                    "import",
                    "from_import"
                ):

                    edges.append(
                        {
                            "from":file,
                            "target":s["name"]
                        }
                    )


    return {
        "nodes":nodes,
        "edges":edges
    }



def cleanup_review(files,refs):


    candidates=[]


    for file in files:


        count=0


        for r in refs:

            if r["source"]==file:

                count+=1



        risk="LOW"


        decision="DELETE_REVIEW"



        lower=file.lower()



        for k in KEEP_PATH:

            if k.lower() in lower:

                risk="HIGH"

                decision="KEEP"


        if count>0:

            decision="KEEP_OR_MIGRATE"


        candidates.append(
            {
                "file":file,
                "references":count,
                "risk":risk,
                "decision":decision
            }
        )


    return candidates



def save(name,data):

    path=os.path.join(
        REPORT_DIR,
        name
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



def main():

    files=collect_files()


    all_symbols=[]


    for f in files:

        if f.endswith(".py"):

            all_symbols.extend(
                python_symbol_scan(f)
            )


    refs=text_reference_scan(
        files,
        all_symbols
    )


    graph=build_dependency_graph(
        files
    )


    cleanup=cleanup_review(
        files,
        refs
    )


    scan_report={

        "version":
        "CODE_REFERENCE_IMPACT_SCAN_V1.1",

        "time":
        str(datetime.now()),

        "root":
        ROOT,

        "files":
        len(files),

        "references":
        len(refs)

    }


    save(
        "CODE_REFERENCE_IMPACT_SCAN_V1.1.json",
        scan_report
    )


    save(
        "DEPENDENCY_GRAPH_V1.0.json",
        graph
    )


    save(
        "DELETE_CANDIDATE_REVIEW_V1.0.json",
        cleanup
    )


    print("==============================")
    print("CODE REFERENCE IMPACT SCAN V1.1")
    print("==============================")
    print("Files:",len(files))
    print("References:",len(refs))
    print("Completed")


if __name__=="__main__":

    main()
