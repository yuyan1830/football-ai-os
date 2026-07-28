
# -*- coding: utf-8 -*-

import os


class PathValidator:


    def check(self, path):

        return os.path.exists(path)

