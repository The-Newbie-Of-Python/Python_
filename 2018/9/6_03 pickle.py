#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/6
'''
pickle
只适用于python
序列化函数
'''
import pickle

def haha():
    print("ok")

data = pickle.dumps(haha)

f = open('PICKLE_TEXT','wb')
f.write(data)