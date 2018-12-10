#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/17
'''

'''
f = open('test.txt','a+b')

f.write(b'hello')
f.write(b'hello')
f.write(b'hello')
# f = open('test.txt','U',encoding='utf8')
print(f.read())