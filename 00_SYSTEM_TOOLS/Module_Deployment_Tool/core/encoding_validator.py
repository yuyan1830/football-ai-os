
# -*- coding: utf-8 -*-


class EncodingValidator:


    def check(self, file):

        try:

            with open(
                file,
                encoding="utf-8"
            ):

                return True


        except Exception:

            return False

