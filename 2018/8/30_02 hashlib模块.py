#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/30
'''
hashlib 模块
'''
import hashlib

m = hashlib.md5()
print(m)

m.update("123.com".encode("utf8") )
print(m.hexdigest())

m.update("wun".encode("utf8"))
print(m.hexdigest())

#m.update("123.comwun".encode("utf8"))
#print(m.hexdigest())

s = hashlib.sha256()
print(s)

s.update("123.com".encode("utf8"))
print(s.hexdigest())
