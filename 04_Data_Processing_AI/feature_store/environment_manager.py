
# -*- coding: utf-8 -*-



class EnvironmentManager:


    environments=[

        "development",

        "validation",

        "production"

    ]



    def list_environments(self):

        return self.environments



    def check_environment(
        self,
        env
    ):

        return env in self.environments


