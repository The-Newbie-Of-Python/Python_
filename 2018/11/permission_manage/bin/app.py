#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/11/19
'''

'''
import os
import sys

Basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Basedir)

from src import service


if __name__ == '__main__':
    service.execute()

