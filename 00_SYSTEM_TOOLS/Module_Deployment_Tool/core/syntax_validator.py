
# -*- coding: utf-8 -*-

import ast


class SyntaxValidator:


    def check(self, file):

        try:

            with open(
                file,
                encoding="utf-8"
            ) as f:

                ast.parse(
                    f.read()
                )

            return True


        except Exception:

            return False

