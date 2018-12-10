#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/28
'''
迭代器
生成器就是迭代器，但是迭代器不一定是生成器
迭代器满足的两个条件：1、有iter方法；2、有next方法
'''
from collections import Iterable,Iterator

l = [1,2,3,4,5]
print(type(l))
print(l)
d = iter(l)             #l.__iter__()
print(type(d))        #<class 'list_iterator'>
print(d)                #<list_iterator object at 0x00000112636F88D0>

print(next(d))
next(d)

print(isinstance(l,list))
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
print(isinstance(d,Iterator))

#######################################################################################################################
print("---------------------------华丽分割线----------------------------------")
with open("customer","r") as f:
    # for i in f.readlines():   #f.readlines()将内容按行取出存入列表中
    #     print(i)
    #     print(type(f.readlines()))

    for i in f:
        print(i)
        print(type(f))
    print(type(iter(f)))

print("---------------------------华丽分割线----------------------------------")
#######################################################################################################################
#选出文件中最长的行
print(max( len(x.strip()) for x in (open("customer","r"))))
