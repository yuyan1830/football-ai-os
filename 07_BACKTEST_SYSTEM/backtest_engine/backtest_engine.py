
# -*- coding: utf-8 -*-

class BacktestEngine:

    def run(self, prediction, result):

        return {
            "prediction": prediction,
            "actual": result,
            "status": "completed"
        }
