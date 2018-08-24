#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/16
'''
保留字
'''
from keyword import kwlist
#print(kwlist)
Blword = []
#False = "12133"
v = 0
for i in kwlist:
    v += 1
    Blword.append(i)
print(v)
print(Blword)
