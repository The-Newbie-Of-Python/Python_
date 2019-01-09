#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/9
'''

'''
import binascii
import hashlib
import hmac
import random
import sys
import time

'''1.列出AK信息'''
SecretId = "AKIDMdjegcmoGYiolXbk5EC3jEYhiYFo9WdE"
SecretKey = "d5MRL4VoxyvlQvMchaUHhx658A2lNq7D"

#参数
'''
===========================================公共参数========================================================
Action 	String 	是 	具体操作的指令接口名称，例如想要调用云服务器的查询实例列表接口，则 Action 参数即为 DescribeInstances 。
Region 	String 	是 	地域参数，用来标识希望操作哪个地域的数据。
Timestamp 	Integer 	是 	当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，如果与当前时间相差过大，会引起签名过期错误。
Nonce 	Integer 	是 	随机正整数，与 Timestamp 联合起来，用于防止重放攻击。
SecretId 	String 	是 	在云API密钥上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey ，而 SecretKey 会用来生成请求签名 Signature。
Signature 	String 	是 	请求签名，用来验证此次请求的合法性，需要用户根据实际的输入参数计算得出。具体计算方法参见接口鉴权文档。
Version 	String 	是 	API 的版本。例如 2017-03-12。

===========================================输入参数========================================================
Action 	是 	String 	公共参数，本接口取值：DescribeZones
Version 	是 	String 	公共参数，本接口取值：2017-03-12
Region 	是 	String 	公共参数，详见产品支持的地域列表。

===========================================最终所需参数====================================================
Timestamp 	Integer 	是 	当前 UNIX 时间戳，可记录发起 API 请求的时间。例如1529223702，如果与当前时间相差过大，会引起签名过期错误。
Nonce 	Integer 	是 	随机正整数，与 Timestamp 联合起来，用于防止重放攻击。
SecretId 	String 	是 	在云API密钥上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey ，而 SecretKey 会用来生成请求签名 Signature。
Signature 	String 	是 	请求签名，用来验证此次请求的合法性，需要用户根据实际的输入参数计算得出。具体计算方法参见接口鉴权文档。
Action 	是 	String 	公共参数，本接口取值：DescribeZones
Version 	是 	String 	公共参数，本接口取值：2017-03-12
Region 	是 	String 	公共参数，详见产品支持的地域列表。

'''

'''2.生成签名串'''
#需要调用的接口地址
uri = "cvm.tencentcloudapi.com"
#选择操作的action
Action = "DescribeKeyPairs"
#选择Region
Region = "ap-chengdu"

'''2.1参数排序'''

Nonce = random.randint(65535,999999999) #a到b的随机正整数
Timestamp = int(time.time())
paramDict = {
    "Timestamp":Timestamp,
    "Nonce":Nonce,
    "SecretId":SecretId,
    "Action":Action,
    "Version":'2017-03-12',
    "Region":Region,
    # "KeyName":"wun_keypair",
    # "ProjectId":1101069

}
tempList = []
tempDict = {}
for eveKey,eveValue in paramDict.items():
    tempLowerData = eveKey.lower()
    tempList.append(tempLowerData)
    tempDict[tempLowerData] = eveKey
tempList.sort()

'''2.2参数拼接'''
resultList = []
for eveData in tempList:
    tempStr = str(tempDict[eveData]) + "=" + str(paramDict[tempDict[eveData]])
    resultList.append(tempStr)
sourceStr = "&".join(resultList)

'''2.3拼接出需要签名的原文字符串'''
requestStr = "%s%s%s%s%s"%("GET",uri,"/","?",sourceStr)

'''2.4生成签名串'''

if sys.version_info[0] > 2 :
    signStr = requestStr.encode("utf-8")
    SecretKey = SecretKey.encode("utf-8")

digestmod = hashlib.sha1

hased = hmac.new(SecretKey,signStr,digestmod)

base64Data = binascii.b2a_base64(hased.digest())[:-1]

'''3.签名串URL编码'''

if sys.version_info[0] > 2 :
    base64Data = base64Data.decode()

import urllib.parse
base64Data = urllib.parse.quote(base64Data)

'''4.请求URL拼接'''
url = 'https://' + uri + '/' + '?' + sourceStr + '&Signature=' + base64Data


'''可能会用到的输出方法'''



if __name__ == '__main__':
    import urllib.request
    import json
    print(urllib.request.urlopen(url).read().decode("utf-8"))
    try:
        for eveData in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["Response"]["KeyPairSet"]:
            print(eveData)
        # for eveData in json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["Response"]["KeyPairSet"]["PrivateKey"]:
        #     print(eveData)
    except :
        pass