
# -*- coding: utf-8 -*-



class DataSourceRegistry:



    sources={


        "football_v_database":

        True,


        "legacy_project":

        False,


        "external_api":

        False


    }



    def get_sources(self):

        return self.sources



