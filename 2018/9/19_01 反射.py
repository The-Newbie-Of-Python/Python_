#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/19
'''
反射
'''
import time

class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return "%s-%s"%(self.name,self.age)

    def f1(self):
        return 'main page'

    def f2(self):
        return 'news'

    def f3(self):
        return 'stories'

obj = Foo('wun',18)
while True:
    T = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print(T)
    inp = input('>>>>')
    try:
        inp in ['name','age']
    except Exception as e:
        print('error input')
    r = getattr(obj,inp)
    if r:
        print(r)

