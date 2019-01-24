#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/22
'''

'''
import hashlib
import hmac
import random
import time

import requests

secretId = 'AKIDQlwvowGkxT6a6Urp13CLS9LOKAAINHB4'
secretKey = '7BkhzCJGHVnWI7rRtdGnFA7oBOQNZir0'

data = {
    'Action': 'DescribeProject',
    'Nonce': random.randint(10000, 99999),
    'Region': 'bj',
    'SecretId': secretId,
    'Timestamp': int(time.time()),
    'allList': 1
}
#print(data)
url = 'account.api.qcloud.com/v2/index.php'

signature_old = ''
for i in sorted(data):
    signature_old = signature_old + i + "=" + str(data[i]) + "&"
signature_old = signature_old[:-1]
# print(signature_old)

query = 'GET' + url + "?" + signature_old
# print(query)
# #
#hmac_str = hmac.new(secretKey.encode('utf-8'), query.encode('utf-8'), hashlib.sha1).digest()
hmac_str = hmac.new(secretKey.encode('utf-8'), query.encode('utf-8'), hashlib.sha1)
# print(hmac_str)
# signature = base64.b64decode(hmac_str)
import binascii
signature = binascii.b2a_base64(hmac_str.digest())[:-1]
# print(signature)

data["Signature"] = signature

resp = requests.get('http://' + url,params=data)

print(resp)