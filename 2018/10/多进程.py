#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/25
'''

'''
import time
from multiprocessing import Process


def f(name):
    time.sleep(1)
    print('hello',name,time.ctime())

if __name__ == "__main__":
    p_list = []
    for i in range(10):
        p = Process(target=f,args=('wun',))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()