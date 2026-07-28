

# -*- coding:utf-8 -*-



class EvolutionPatternAnalyzer:



    def analyze(self,records):


        success=0


        fail=0



        for r in records:


            if r.get(

                "result"

            )=="SUCCESS":


                success+=1


            else:


                fail+=1




        return {


            "success_count":

            success,


            "fail_count":

            fail,


            "success_rate":

            (

                success /

                max(

                    success+fail,

                    1

                )

            )

        }



