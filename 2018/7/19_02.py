#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "Auther"
# Date: 2018/7/19

'''login de 循环'''

_user = "wun"
_passwd = "123.com"

for i in range(3):
    username = input("Please input username:")
    password = input("Please input password")
    if username == _user and password == _passwd:
        print("welcome %s login" % _user)
        break#中断，跳出循环
    else:
        print("Invalid username or password!")
else:#只有当for循环全部执行完毕后才会执行else中的内容
    print("Too many worry try!!!")


