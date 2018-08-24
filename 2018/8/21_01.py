#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/21
'''
集合
'''
a = {11,11,22,3,4,6,9,2,33,4}
b = {2,23,343,56,5787,79,665434567,8765}
#集合，无序，去重，不重复的元素集合
print(a,b)

print(a | b)
print(a.union(b))      #a 并 b  ,并集

print(a.difference(b))  #in a but not in b
print(b.difference(a))

print(a.symmetric_difference(b))  #反向差集
print(a ^ b)

print(a.intersection(b))  #交集

