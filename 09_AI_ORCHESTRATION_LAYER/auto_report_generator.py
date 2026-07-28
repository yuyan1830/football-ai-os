
# -*- coding: utf-8 -*-

import json

import datetime




class AutoReportGenerator:



    def __init__(self):


        self.reports=[]





    def create_match_report(

        self,

        match,

        prediction,

        decision

    ):



        report={


            "type":

            "MATCH_REPORT",


            "time":

            str(

                datetime.datetime.now()

            ),


            "match":

            match,


            "prediction":

            prediction,


            "decision":

            decision



        }



        self.reports.append(

            report

        )



        return report






    def create_model_report(

        self,

        model_results

    ):



        report={


            "type":

            "MODEL_REPORT",


            "models":

            model_results



        }



        self.reports.append(

            report

        )



        return report






    def create_roi_report(

        self,

        roi_data

    ):



        report={


            "type":

            "ROI_REPORT",


            "roi":

            roi_data



        }



        self.reports.append(

            report

        )



        return report






    def export(

        self,

        path

    ):



        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                self.reports,

                f,

                indent=4,

                ensure_ascii=False

            )



        return {


            "status":

            "EXPORTED",


            "file":

            path



        }




    def summary(self):


        return {


            "total_reports":

            len(

                self.reports

            )


        }



