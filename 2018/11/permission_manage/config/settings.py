#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/11/19
'''
config文件
'''

#当前登陆用户的信息
current_user_info = {}

#当前登陆用户的权限信息
current_user_permission_list = []

#数据库连接信息
PY_MYSQL_CONNCECT_DICT = {
    'host':'172.20.6.158',
    'port':3306,
    'user':'auther',
    'passwd':'123.com',
    'db':'employees',
    'charset':'utf8'
}