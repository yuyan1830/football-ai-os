

# -*- coding:utf-8 -*-



class LearningEffectTracker:



    def __init__(self):


        self.records=[]




    def track(

        self,

        before,

        after

    ):



        result={


            "accuracy_change":

            after.get(

                "accuracy",

                0

            )

            -

            before.get(

                "accuracy",

                0

            ),



            "roi_change":

            after.get(

                "roi",

                0

            )

            -

            before.get(

                "roi",

                0

            )



        }



        self.records.append(result)



        return result




    def history(self):


        return self.records



