
# -*- coding: utf-8 -*-

from feature_validator import FeatureValidator
from feature_dataset_builder import FeatureDatasetBuilder



class FeaturePipeline:


    def __init__(self):

        self.builder=FeatureDatasetBuilder()

        self.validator=FeatureValidator()



    def run(self,matches):


        data=self.builder.build(matches)


        if self.validator.validate(data):

            return data


        return []



