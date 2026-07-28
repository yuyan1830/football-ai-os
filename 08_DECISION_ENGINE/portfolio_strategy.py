
# -*- coding: utf-8 -*-



class PortfolioStrategy:



    def allocate(

        self,

        matches

    ):



        result=[]



        total=len(matches)



        if total==0:


            return result




        weight=1/total




        for match in matches:


            result.append(


                {


                "match":

                match,


                "weight":

                round(

                    weight,

                    4

                )


                }


            )



        return result




    def risk_adjust(

        self,

        portfolio,

        risk

    ):



        if risk=="HIGH":


            return [

                x

                for x in portfolio

                if x["weight"]<0.03

            ]



        return portfolio



