

# -*- coding:utf-8 -*-



class OptimizationPriorityEngine:



    def rank(self,tasks):


        return sorted(

            tasks,

            key=lambda x:x.get(

                "priority",

                0

            ),

            reverse=True

        )



