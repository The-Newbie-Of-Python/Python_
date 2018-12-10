#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/28
'''
time
'''
import datetime
import time

#
# print(time.time())
# print(time.clock())
# print(time.localtime())
# t = time.localtime()
# print(type(t))
# struct_time = time.localtime()
# T = time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(T)
#print(help(time))
print(time.gmtime())
#time.strptime()
print(time.localtime())
print(time.ctime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(time.time())
print(time.mktime(time.localtime()))


print(datetime.datetime.now())