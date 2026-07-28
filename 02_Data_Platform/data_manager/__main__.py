# -*- coding: utf-8 -*-

"""
Football AI OS
Data Manager Module Entry
"""


import sys
import os


CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

sys.path.append(CURRENT_DIR)


from data_manager import DataManager



if __name__ == "__main__":

    print("="*50)
    print("Football AI OS Data Manager V1.0")
    print("="*50)


    manager = DataManager()


    print(
        manager.status()
    )