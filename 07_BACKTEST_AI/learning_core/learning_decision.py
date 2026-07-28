# -*- coding: utf-8 -*-

class LearningDecision:


    def __init__(self):

        self.version="V1.0"


    def evaluate(self, metrics):

        """
        判断是否需要进入学习流程
        """

        accuracy_drop = metrics.get(
            "accuracy_drop",
            False
        )

        roi_drop = metrics.get(
            "roi_drop",
            False
        )


        learning_required = (
            accuracy_drop
            or
            roi_drop
        )


        return {

            "learning_required":
                learning_required,

            "reason":
                "Performance degradation detected"
                if learning_required
                else
                "Performance stable",

            "version":
                self.version

        }
