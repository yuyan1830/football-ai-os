# -*- coding: utf-8 -*-

"""
CSV Loader V1.0
"""

import csv


def load_csv(path):

    rows=[]

    with open(
        path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        reader=csv.DictReader(f)

        for row in reader:

            rows.append(row)


    return rows