#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/7
# '''
#
# '''
# import hashlib, hmac, json, os, sys, time
# from datetime import datetime
#
# # 密钥参数
# # secret_id = "AKIDMdjegcmoGY**********"
# # secret_key = "d5MRL4Voxyvl************"
#
# service = "cvm"
# host = "cvm.tencentcloudapi.com"
# endpoint = "https://" + host
# region = "ap-guangzhou"
# action = "DescribeInstances"
# version = "2017-03-12"
# algorithm = "TC3-HMAC-SHA256"
# timestamp = int(time.time())
# date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
# params = {"Limit": 10, "Offset": 0}
#
# # ************* 步骤 1：拼接规范请求串 *************
# http_request_method = "GET"
# canonical_uri = "/"
# canonical_querystring = "Limit=10&Offset=0"
# ct = "x-www-form-urlencoded"
# payload = ""
# if http_request_method == "POST":
#     canonical_querystring = ""
#     ct = "json"
#     payload = json.dumps(params)
# canonical_headers = "content-type:application/%s\nhost:%s\n" % (ct, host)
# signed_headers = "content-type;host"
# hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
# canonical_request = (http_request_method + "\n" +
#                      canonical_uri + "\n" +
#                      canonical_querystring + "\n" +
#                      canonical_headers + "\n" +
#                      signed_headers + "\n" +
#                      hashed_request_payload)
# print(canonical_request)
#
# # ************* 步骤 2：拼接待签名字符串 *************
# credential_scope = date + "/" + service + "/" + "tc3_request"
# hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
# string_to_sign = (algorithm + "\n" +
#                   str(timestamp) + "\n" +
#                   credential_scope + "\n" +
#                   hashed_canonical_request)
# print(string_to_sign)
#
# # ************* 步骤 3：计算签名 *************
# # 计算签名摘要函数
# def sign(key, msg):
#     return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
# secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
# secret_service = sign(secret_date, service)
# secret_signing = sign(secret_service, "tc3_request")
# signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
# print(signature)
#
# # ************* 步骤 4：拼接 Authorization *************
# authorization = (algorithm + " " +
#                  "Credential=" + secret_id + "/" + credential_scope + ", " +
#                  "SignedHeaders=" + signed_headers + ", " +
#                  "Signature=" + signature)
# print(authorization)
#
# # 公共参数添加到请求头部
# headers = {
#     "Authorization": authorization,
#     "Host": host,
#     "Content-Type": "application/%s" % ct,
#     "X-TC-Action": action,
#     "X-TC-Timestamp": str(timestamp),
#     "X-TC-Version": version,
#     "X-TC-Region": region,
# }
# print("#"*90)
# print(headers)

print("-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDDNtdxgVYl6ZlZr1r7lkHuw4wJOW5nD6J73pdEeD8ynMXepbQl\nHt8Hcyr7W79hiyQQIZU+ZDNvoQpUK7co0KnWS5KYgp+4os5eKwNTB7l3JvrSpYU5\njCWTdP9+PtK5bJglmk9fpIwrj1G/RSbQp4p5fd1LPbu3yJ/TlGUCb8gw3QIDAQAB\nAoGBAKOwE50Ib10g8EZEhIzbJHP5oi2F664dbQhi0AJIte1RiZU06sYJicfsaQkV\nmHdJPbcNAeCsEnky1r9XXKCrvwwLqQ1AwO8bEhH2qBERsDTlo5UaH1cwTm3ugzXt\n9f1eiWS1B5orER2GxjUnMNvCrpMCQP2a/Ss3Qe/h1746LWrdAkEA4o4I/Wi03Ff6\n/zrcpVkxdq3cr6Xl1br7CbGTfUHnJkp6FLXZjvZe2c8oZOJYMhmlkzLL8v2YaI+J\nlt9fdgugzwJBANyWCZkT9vNG0txHzydVJkuraLEnAs4PaIU82v2pPDUB5K4V5Dri\neLiRPaKtUfoQESYtvhf5n/2SharFCyLKBpMCQQDhzDo9hqwrqCxrURk0Wy8nX6VC\nExB88nzdbnTXNGXTDguatJv/FqH2Z7eUxNquJE2X5drLdeD+5YB2NG8KUhCVAkEA\nvjTF+/BiLe4xHm7xKmpbBj68nJ0V5xcUOmd6MeZ/GvoR9Sa9USU9kXDz49Vt7aFz\nGCezVbsTATUZ+2HDM3Fe7wJAZRKMqYoB3aKjCEq+WB5ofjxW0OgLh/m0ZU0xPoNS\nco3Y20cbhuGgcmeciboZZqjJhOzGrPPjuY5LwE1XFfe+Jw==\n-----END RSA PRIVATE KEY-----\n")
