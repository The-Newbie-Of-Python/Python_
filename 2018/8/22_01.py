#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/22
'''
递归函数
1、调用自身函数
2、有一个结束条件

可以递归的都可以用循环解决
多重递归递归效率低
'''

import time

def fact(n):
    if n==1 :
        return 1
    return n * fact(n-1)
print(fact(30))
#斐波那契数列
def fibo(n):
    before = 0
    after = 1

    for i in range(n-1):
        ret = before + after
        before = after
        after = ret
    return ret

print(30*"*")
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(fibo(40))
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(30*"*")
'''
******************************
2018-08-22 11:41:42
102334155
2018-08-22 11:41:42
******************************
'''

#递归斐波那契数列
def fibo_new(n):
    if n <= 1:
        return n
    return fibo_new(n-1)+fibo_new(n-2)

print(30*"#")
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(fibo_new(40))
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(30*"#")
'''
##############################
2018-08-22 11:41:42
102334155
2018-08-22 11:42:54
##############################
'''
