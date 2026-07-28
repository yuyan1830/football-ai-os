
# -*- coding: utf-8 -*-

from feature_data_loader import FeatureDataLoader
from feature_dataset_exporter import FeatureDatasetExporter



class FeaturePipelineRunner:


    def __init__(self):

        self.loader = FeatureDataLoader()

        self.exporter = FeatureDatasetExporter()



    def run(
        self,
        data,
        output
    ):


        dataset = self.loader.load(
            data
        )


        self.exporter.export(
            dataset,
            output
        )


        return dataset


