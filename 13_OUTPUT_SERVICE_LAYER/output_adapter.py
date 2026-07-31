# -*- coding: utf-8 -*-

"""
Football AI OS
Output Adapter V1.0
"""


import sys


sys.path.insert(
    0,
    r"E:\football_v\13_OUTPUT_SERVICE_LAYER"
)


from report_service import ReportService



def generate_output(data):


    service = ReportService()


    return service.generate(
        data
    )

