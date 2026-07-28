
# -*- coding: utf-8 -*-

class FeedbackMemory:


    def __init__(self):

        self.records=[]


    def add(
        self,
        data
    ):

        self.records.append(data)

        return True


    def count(self):

        return len(self.records)
