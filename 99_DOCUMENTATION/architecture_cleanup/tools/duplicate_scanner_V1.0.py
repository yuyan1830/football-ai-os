import os
import json
import ast
from collections import defaultdict


ROOT=os.getcwd()

BASE="99_DOCUMENTATION/architecture_cleanup/reports"


class Scanner:


    def __init__(self):

        self.files=[]
        self.classes=defaultdict(list)
        self.functions=defaultdict(list)


    def scan(self):

        for root,dirs,files in os.walk(ROOT):

            if "__pycache__" in root:
                continue


            for f in files:

                if f.endswith(".py"):

                    path=os.path.join(root,f)

                    self.files.append(path)


                    try:

                        tree=ast.parse(
                            open(
                                path,
                                encoding="utf8"
                            ).read()
                        )


                        for node in ast.walk(tree):

                            if isinstance(
                                node,
                                ast.ClassDef
                            ):
                                self.classes[node.name].append(path)


                            if isinstance(
                                node,
                                ast.FunctionDef
                            ):
                                self.functions[node.name].append(path)


                    except:
                        pass



    def report(self):

        data={

            "version":
            "ARCHITECTURE_DUPLICATE_SCAN_V1.0",


            "python_files":
            len(self.files),


            "duplicate_classes":
            {
            k:v
            for k,v in self.classes.items()
            if len(v)>1
            },


            "duplicate_functions":
            {
            k:v
            for k,v in self.functions.items()
            if len(v)>5
            }

        }


        os.makedirs(BASE,exist_ok=True)


        with open(
            BASE+"/ARCHITECTURE_DUPLICATE_SCAN_V1.0.json",
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        print(data)



if __name__=="__main__":

    s=Scanner()

    s.scan()

    s.report()
