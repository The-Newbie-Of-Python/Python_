#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/25
'''
编码：str(unicode)  -->  bytes
解码：bytes --> str(unicode)
print内置str方法
'''
import  json
import sys

s = "吴楠"                 # unicode类型数据对应的str明文
print(type(s))
b1 = s.encode("utf8")        #编码
print(b1,type(b1))
print(b1.decode("utf8"))     #解码   b'\xe5\x90\xb4\xe6\xa5\xa0' <class 'bytes'>



b2 = s.encode("gbk")         #编码
print(b2,type(b2))
print(b2.decode("gbk"))      #解码
print(json.dumps(s))

b3 = bytes(s,"utf8")
print(b3,type(b3))
print(str(b3,"utf8"))

print(sys.getdefaultencoding())