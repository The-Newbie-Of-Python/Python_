#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/26
'''

'''
# import  gevent,greenlet
#
# def foo():
#     print("num 1")
#     r2.switch()
#     print("num 2")
#     r2.switch()
#
# def bar():
#     print("num3")
#     r1.switch()
#     print("num4")
#
# # if __name__ == "__main__":
# r1 = greenlet.greenlet(foo)
# r2 = greenlet.greenlet(bar)
#
# # foo()
# r1.switch()

import time

import gevent


def foo():
    print("i am num1",time.ctime())
    gevent.sleep(1)
    # time.sleep(1)
    print("i am num2",time.ctime())
    # gevent.sleep(0)

def bar():
    print("i am num3",time.ctime())
    gevent.sleep(2)
    print("i am num4",time.ctime())

gevent.joinall(
    [gevent.spawn(foo),
     gevent.spawn(bar)]
)
