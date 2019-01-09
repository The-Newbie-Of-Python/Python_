#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/8
'''
退还CVM
'''
#列出AK信息
secret_id = "AKIDMdjegcmoGYiol*********"
secret_key = "d5MRL4VoxyvlQvMc*********"


#列出所有参数，再根据必要参数筛选
'''
SecretId 	密钥Id 	AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
Timestamp 	当前时间戳 	1465185768
Nonce 	随机正整数 	11886

Action 	是 	String 	公共参数，本接口取值：TerminateInstances
Version 	是 	String 	公共参数，本接口取值：2017-03-12
Region 	是 	String 	公共参数，详见产品支持的地域列表。
InstanceIds.N 	是 	Array of String 	一个或多个待操作的实例ID。可通过DescribeInstances接口返回值中的InstanceId获取。每次请求批量实例的上限为100。
'''

##########################################################生成签名串###############################
import time
#腾讯云API接口地址
uri = "cvm.tencentcloudapi.com"
#将参数写成字典
paramDict = {
    "Action":"TerminateInstances",
    "Version":"2017-03-12",
    "SecretId":secret_id,
    "Nonce":"123456",
    "Timestamp":int(time.time()),
    "Region":"ap-chengdu",
    "InstanceIds.0":"ins-d74yz4h1"
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
