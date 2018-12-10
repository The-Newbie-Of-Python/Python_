#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/31
'''
congifparser模块
'''
import configparser

config = configparser.ConfigParser()

# config["default"] = { "ForwardAgent":"no",
#         "ForwardX11": "no",
#         "RhostsAuthentication": "no",
#         "RhostsRSAAuthentication": "no"
#                         }
#
# config["top10"]= {}
# config["top10"]["user"] = "hp"
#
#
# config["hug"] = {}
#
# with open("config.ini","w") as configfile:
#     config.write(configfile)

print(config.sections())             #[]
print(type(config.sections()))       #<class 'list'>
config.read("config.ini")
print(config.sections())             #['default', 'top10', 'hug']   ['top10', 'hug']
print(config.defaults())             #OrderedDict([('forwardagent', 'no'), ('forwardx11', 'no'), ('rhostsauthentication', 'no'), ('rhostsrsaauthentication', 'no')])
