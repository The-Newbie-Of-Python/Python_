#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/23
'''
装饰器
#封闭开放原则
#对修改封闭，对扩展开放
'''
import time

def show_time(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print("spend %s s"%(end-start))
    return inner

@show_time    #等价于foo = show_time(foo)  装饰器“@函数名等价于功能函数（函数名）”
def foo():
    print("this is a foo...")
    time.sleep(3)

def bar():
    print("this is a bar...")
    time.sleep(2)

def showtime(func):
    start_time=time.time()
    func()
    end_time=time.time()
    spend_time=end_time-start_time
    print("this is spend time:%s s"%spend_time)

showtime(bar)
showtime(foo)

foo()


##装饰器参数



