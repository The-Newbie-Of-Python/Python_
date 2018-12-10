#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/11/13
'''
数据库
'''
import time

import pymysql

print(time.ctime())

#创建连接
conn = pymysql.connect(host='172.20.6.158',port=3306,user='auther',passwd='123.com',db='employees',charset='utf8')
#创建游标
cursor =conn.cursor()


#传入Sql语句
#cursor.execute('CREATE TABLE py_test(nid int,name varchar(20),date datetime)')
cursor.execute("insert into py_test(nid,name) values(1,'wun')")
#提交Sql
conn.commit()

#获取数据
result = cursor.fetchall()
result = cursor.fetchone()
result = cursor.fetchmany()
print(result)


#关闭游标
cursor.close()
#关闭连接
conn.close()