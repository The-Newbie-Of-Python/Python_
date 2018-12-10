#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/27
'''
基于yield实现的伪并发
'''

import time

def cosumer(name):
    print("%s 准备开始！" %name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了！" %(baozi,name))

def producer(name):
    c1 = cosumer("A")
    c2 = cosumer("B")
    next(c1)                        #c1.__next__()
    c2.__next__()                   #next(c2)
    print("%s开始做包子了" %name)
    for i in range(10):
        time.sleep(1)
        print("做了俩包子")
        c1.send(i)
        c2.send(i)

producer("wun")