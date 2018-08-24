#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/22
'''
闭包
条件一、内部函数
条件二、调用外部函数的变量
'''

def outer(x):
    pass
    def inner():
        print(x)
    return inner()

outer(20)