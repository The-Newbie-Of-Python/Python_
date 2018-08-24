#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/22
'''
迭代器
'''
from functools import reduce
# print(all("111 334"))
# all()


str = ["a","b","c","d"]

def func1(s):
    if s != "a":
        return s
ret1 = filter(func1,str)

print(ret1)                                 #<filter object at 0x0000019EBA906860> 过滤器对象，迭代器对象
print(list(ret1))

def func2(m):
    return m + "wunan"
ret2 = map(func2,str)

print(ret2)                     #<map object at 0x0000020488646940>
print(list(ret2))


def func3(x,y):
    return x + y
ret3 = reduce(func3,range(1,100))

print(ret3)                  #生成一个值，不是迭代器对象





