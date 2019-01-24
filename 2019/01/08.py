#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/8
'''
API初级使用
腾讯云V1版本API调用，地域信息
'''

#列出AK信息
secret_id = "AKIDMdjegcmoGYio****"
secret_key = "d5MRL4VoxyvlQvM****"


#列出所有参数，再根据必要参数筛选
'''
SecretId 	密钥Id 	AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
Timestamp 	当前时间戳 	1465185768
Nonce 	随机正整数 	11886
InstanceIds.0 	待查询的实例ID 	ins-09dx96dg
Offset 	偏移量 	0
Limit 	最大允许输出 	20
Action 	是 	String 	公共参数，本接口取值：DescribeRegions
Version 	是 	String 	公共参数，本接口取值：2017-03-12
'''

##########################################################生成签名串###############################
import time
#腾讯云API接口地址
uri = "cvm.tencentcloudapi.com"
#将参数写成字典
paramDict = {
    "Action":"DescribeRegions",
    "Version":"2017-03-12",
    "SecretId":secret_id,
    "Nonce":"123456",
    "Timestamp":int(time.time())
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


########################################请求#####################################################
import urllib.request
print(
    urllib.request.urlopen(url).read().decode("utf-8")
)

#输出json格式
import json
for eveData in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["Response"]["RegionSet"]:
    print(eveData)
