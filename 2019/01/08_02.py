#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/8
'''
创建CVM
'''
#列出AK信息
# secret_id = "AKIDMdjegcmoGYiolXbk5E*****"
# secret_key = "d5MRL4VoxyvlQvMchaU*****"


#列出所有参数，再根据必要参数筛选
'''
SecretId 	密钥Id 	AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
Timestamp 	当前时间戳 	1465185768
Nonce 	随机正整数 	11886
InstanceIds.0 	待查询的实例ID 	ins-09dx96dg
Offset 	偏移量 	0
Limit 	最大允许输出 	20
Action 	是 	String 	公共参数，本接口取值：RunInstances
Version 	是 	String 	公共参数，本接口取值：2017-03-12
Region 	是 	String 	公共参数，详见产品支持的地域列表。
Placement 	是 	Placement 	实例所在的位置。通过该参数可以指定实例所属可用区，所属项目，所属宿主机（在专用宿主机上创建子机时指定）等属性。
ImageId 	是 	String 	指定有效的镜像ID，格式形如img-xxx。
'''

##########################################################生成签名串###############################
import time
#腾讯云API接口地址
uri = "cvm.tencentcloudapi.com"
#将参数写成字典
paramDict = {
    "Action":"RunInstances",
    "Version":"2017-03-12",
    "SecretId":secret_id,
    "Nonce":"123456",
    "Timestamp":int(time.time()),
    "Region":"ap-chengdu",
    "Placement.Zone":"ap-chengdu-1",
    "ImageId":"img-oikl1tzv",
    "InstanceChargeType":"POSTPAID_BY_HOUR",
    "InstanceType":"SA1.SMALL1",
    "SystemDisk.DiskType":"CLOUD_PREMIUM"
}
####################################对参数排序
tempList = []
tempDict = {}
for eveKey,eveValue in paramDict.items():
    tempLowerData = eveKey.lower()
    tempList.append(tempLowerData)
    tempDict[tempLowerData] = eveKey
tempList.sort()

###############################拼接请求字符串
resultList = []
for eveData in tempList:
    tempStr = str(tempDict[eveData]) + "=" + str(paramDict[tempDict[eveData]])
    resultList.append(tempStr)
sourceStr = "&".join(resultList)
###############################拼接签名原文字符串
requestStr = "%s%s%s%s%s"%("GET",uri,"/","?",sourceStr)
#print(requestStr)   #GETcvm.tencentcloudapi.com/?Action=DescribeRegions&Nonce=123456&SecretId=AKIDMdjegcmoGYiolXbk5EC3jEYhiYFo9WdE&Timestamp=1546929993&Version=2017-03-12

##############################生成签名串
import sys
#判断运行环境，如果是python3.x版本需要对requestStr和key进行utf8编码
if sys.version_info[0] > 2:
    signStr = requestStr.encode("utf-8")
    secret_key = secret_key.encode("utf-8")
# print(signStr)
# print(secret_key)

#sha1加密签名
import hashlib
digestmod = hashlib.sha1

import hmac
hashed = hmac.new(secret_key,signStr,digestmod)

#base64编码
import binascii
base64Data = binascii.b2a_base64(hashed.digest())[:-1]

#############################################签名串编码#########################################################
if sys.version_info[0] > 2:
    base64Data = base64Data.decode()

import urllib.parse
base64Data = urllib.parse.quote(base64Data)

url = "https://" + uri + "/" + "?" + sourceStr + "&Signature=" + base64Data
print(url)

import urllib.request
print(
    urllib.request.urlopen(url).read().decode("utf-8")
)

# import json
# for eveData in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["Response"]["RegionSet"]:
#     print(eveData)
