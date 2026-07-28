
# -*- coding: utf-8 -*-

BASE=r"E:\football_v"


class DatabaseGovernance:

    def status(self):

        return {
            "module":
            "DATABASE_GOVERNANCE",

            "status":
            "READY"
        }


if __name__=="__main__":

    print(DatabaseGovernance().status())

