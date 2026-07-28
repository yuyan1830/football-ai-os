# -*- coding:utf-8 -*-

"""
Football AI OS
Data Source Integration Pipeline V1.2
"""


import json

from source_scanner import SourceScanner
from source_validator import SourceValidator



DOWNLOAD_PATH="../download"



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Integration Pipeline V1.2"
    )

    print("="*50)



    scanner=SourceScanner(
        DOWNLOAD_PATH
    )


    files=scanner.scan()



    validator=SourceValidator()


    result=validator.validate(
        files
    )



    report={

        "module":
        "01_DATA_SOURCE",

        "pipeline":
        "V1.2",

        "scan":

        result

    }



    print(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )
    )