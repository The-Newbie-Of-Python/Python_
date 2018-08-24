#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/9
'''
进度条
'''

import sys
import time



for i in range(30):
    sys.stdout.write("---")
    sys.stdout.flush()
    time.sleep(0.1)
print(sys.stdout.isatty(),end="\t")
print("lalala",end="")

for i in range(30):
    print("***",end="",flush=True)
    time.sleep(0.1)