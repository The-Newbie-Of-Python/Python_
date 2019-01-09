#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/7
'''

'''
import time

timestamp_10b = int(time.time())           #精确到秒
timestamp_13b = int((time.time())*1000)    #精确到毫秒

print("10位时间戳：",timestamp_10b)
print("13位时间戳：",timestamp_13b)

# ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(ROOT)
#
# print(sys.version_info)
#
# paramDict = {
#     "Action":"DescribeRegions",
#     "Version":"2017-03-12",
#     "SecretId":12344,
#     "Nonce":"123456",
#     "Timestamp":int(time.time())
# }
#
# print(paramDict.items())
# print(paramDict)

