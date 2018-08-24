#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "Auther"
# Date: 2018/7/20

a = ["1","2","3","4","5","6"]

print(a)
print(a[0::])
print(a[1::2])
print(a[-1::])
print(a[-2::-1])
print(a[2::-1])
a.append("7")
print(a)
a.insert(1,"8")
print(a)
a.remove(a[0])
print(a)