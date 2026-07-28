
# -*- coding: utf-8 -*-



class SystemHealthMonitor:



    def __init__(self):


        self.modules={}




    def register(

        self,

        name,

        status

    ):


        self.modules[name]=status




    def check(self):


        result={}



        for module,status in self.modules.items():


            result[module]={


                "status":

                status,


                "health":

                "OK"

                if status=="RUNNING"

                else "READY"


            }




        return result




    def overall_status(self):


        for status in self.modules.values():


            if status not in [

                "RUNNING",

                "READY"

            ]:


                return "WARNING"




        return "HEALTHY"



