
# -*- coding: utf-8 -*-



class ModelRuntime:



    def __init__(self):

        self.status="READY"



    def start(self):


        self.status="RUNNING"


        return self.status



    def stop(self):


        self.status="STOPPED"


        return self.status



