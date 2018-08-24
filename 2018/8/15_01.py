#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/15
'''

'''
f = open("document","r",encoding="utf8")
f.readline()
f = list(f.read())
print(type(f))
print(f)



with open("document2","r",encoding="utf8") as f_read , open("document","w",encoding="utf8") as f_write:
    for line in f_read:
        f_write.write(line)










