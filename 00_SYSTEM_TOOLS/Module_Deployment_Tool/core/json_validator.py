
# -*- coding: utf-8 -*-

import json


class JsonValidator:


    def check(self, file):

        try:

            with open(
                file,
                encoding="utf-8"
            ) as f:

                json.load(f)

            return True


        except Exception:

            return False

