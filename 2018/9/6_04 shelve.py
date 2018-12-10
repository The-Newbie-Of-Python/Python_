#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/6
'''
shelve
'''

import shelve


# data = input("input information>>>")
# data = {'name':'wun','age':24}
# f = shelve.open(r'Shelve_text')
#
# f['info']= data
# f.close()


f = shelve.open(r'Shelve_text')
print(f.get('info')['name'])