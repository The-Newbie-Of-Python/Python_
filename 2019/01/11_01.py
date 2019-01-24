#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/11
'''

'''
import json

obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
encodedjson = json.dumps(obj)
print (repr(obj))
print (encodedjson)

decodejson = json.loads(encodedjson)
print (type(decodejson))
print (decodejson[4]['key1'])
print (decodejson)

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
print(test_dict)
print(type(test_dict))
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

with open("record.json","w") as f:
     json.dump(json_str,f)
     print("加载入文件完成...")

with open("record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
    print(type(load_dict))