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

# import configparser

#
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# config = configparser.ConfigParser()
# file = config.read("api.ini")
# print(file)
#
# sec = config.sections()
# print(sec)
#
# opt = config.options("AccessKey")
# print(opt)
#
# value = config.items("ParamDict")
# print(value)
#
# SecrectId = config.get("AccessKey","SecrectId")
# SecrectKey = config.get("AccessKey","SecrectKey")
# print(SecrectId,SecrectKey)

import configparser
'''====================================================================================================='''
#区分大小写configparser模块重写
class myconf(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr
'''====================================================================================================='''

# def readin(filepath):
#     conf = myconf()
#     conf.read(filepath)
#     print (conf.sections())
#     for i in (conf.sections()):
#         for option in (conf.options(i)):
#             yield (option + ':'+ conf.get(i,option))
conf = myconf()
conf.read('api.conf')

AccessKey = conf.items('AccessKey')
AccessKey_ = {}
for i in AccessKey:
    AccessKey_[list(i)[0]] = list(i)[1]
SecretId = AccessKey_['SecretId']
SecretKey = AccessKey_['SecretKey']

uri = conf.items('URI')
uri = uri[0][1]

action = conf.items('Action')
Action = action[0][1]

region = conf.items('Region')
Region = region[0][1]

f = conf.items('ParamDict')
ParamDict = {}
for i in f:
    ParamDict[list(i)[0]] = (list(i)[1])







if __name__ == "__main__":
    # print(f)
    # print(uri)
    # print(Action)
    # print(ParamDict)
    #
    # print(SecretId,SecretKey)
    nihao = 'haha'
    x = 'nihao'
    print (eval(x))

    # m = []
    # n = [](uri[0][0] + "=" + uri[0][1])
    # listkey = []
    # listvalue = []
    # for i in f:
    #     m.append(":".join(i))
    # for x in m:
    #     n.append((x.split(":")))
    #     for y in n:
    #          listkey.append(y[0])
    #          listvalue.append(y[1])
    # ParamDict = dict(zip(listkey,listvalue))
    # print(ParamDict)










