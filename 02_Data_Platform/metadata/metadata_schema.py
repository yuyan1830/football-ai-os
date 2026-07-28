# -*- coding: utf-8 -*-

"""
Football AI OS
Metadata Schema
V1.0
"""


class MetadataSchema:


    fields = [

        "name",
        "type",
        "version",
        "status"

    ]


    @staticmethod
    def validate(dataset):

        for field in MetadataSchema.fields:

            if field not in dataset:

                return False

        return True