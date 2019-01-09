#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/9
'''
V1_版本API
'''
import json
import urllib.request

import TencentCloudApi as f

# print(urllib.request.urlopen(url).read().decode("utf-8"))
for eveData in json.loads(urllib.request.urlopen(f.url).read().decode("utf-8"))["Response"]["ZoneSet"]:
    print(eveData)


