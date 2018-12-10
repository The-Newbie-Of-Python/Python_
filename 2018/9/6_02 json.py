#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/6
'''
json
序列化
把内存中的对象转化成可存储的
'''

# dic = {'name':'wun','age':'24'}
# f =open('JSON_TEXT','w')

# data = json.dumps(dic)
# f.write(data)

# json.dump(dic,f)

# f.close()
#

#################################################################华丽的分割线#########################################

import json

f = open("JSON_TEXT","r")

# data = f.read()
# data = json.loads(data)
data = json.load(f)
print(data['name'])