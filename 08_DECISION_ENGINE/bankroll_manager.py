
# -*- coding: utf-8 -*-



class BankrollManager:



    def __init__(

        self,

        bankroll=10000

    ):


        self.bankroll=bankroll




    def update(

        self,

        profit

    ):


        self.bankroll += profit



        return self.bankroll




    def balance(self):


        return {


            "bankroll":

            self.bankroll



        }




