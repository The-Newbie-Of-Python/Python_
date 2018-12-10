#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/12
'''
类
面向对象特性：
1、封装
2、继承
3、多态
'''
#self  指调用方法的 对象

class num1:
    def __init__(self,ip,port,name,pwd):
        self.ip = ip
        self.port = port
        self.name = name
        self.pwd = pwd
        print(self)
    def fun(self):
        print(self,'\n',self.name,self.ip,self.port)

x = num1('1.1.1.1',3306,'wun','123.com')
# x.name = 'wun'
# x.age = '24'
# x.gender = 'male'
# x.fun(333)
x.fun()
# y = num1()
# y.name = 'wun'
# y.age = '24'
# y.gender = 'male'
# y.fun(666)

class F:
    def Ff0(self):
        print('F.Ff0')
    def Ff1(self):
        print('F.Ff1')
class f:
    def Ff0(self):
        print("f")
class S(F):
    def Ss0(self):
        print('S.Ss0')

obj = S()
obj.Ff0()