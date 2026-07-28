
# -*- coding: utf-8 -*-

class MemoryAdapter:


    def adapt(
        self,
        prediction,
        result
    ):

        return {
            "prediction":prediction,
            "result":result,
            "updated":True
        }
