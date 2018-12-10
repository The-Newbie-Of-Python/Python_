#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/6
'''

'''


import os
import sys

BASCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASCE_DIR)
# print(sys.path)
# sys.path.append('C:\\Users\\38454\\Desktop\\Road_Of_Python-master\\2018\\9')
# print(sys.path)

# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# # BASCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # sys.path.append(BASCE_DIR)
# print(BASCE_DIR)
# print(sys.path)
print(__name__)

if __name__ == '__main__':
    print(__file__)
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    # BASCE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.append(BASCE_DIR)
    print(BASCE_DIR)
    print(sys.path)
    print(__name__)