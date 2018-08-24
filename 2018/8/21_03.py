#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/21
'''
函数
'''

#必需参数
def print_info(name,age):
    print("Name: %s"%name)
    print("Age: %s"%age)
    print(30*"*")

print_info(15,"wunan")
print(print_info(12,"wunan"))
#关键字参数
def print_info(name,age):
    print("Name: %s"%name)
    print("Age: %s"%age)
    print(30*"*")
print_info(age = 15,name = "wunan")

#默认参数  默认参数要跟在其他参数之后
def print_info(name,age,sex="male"):
    print("Name: %s"%name)
    print("Age: %s"%age)
    print("Sex: %s"%sex)
    print(30*"*")
print_info(age = 15,name = "wunan")
print_info(age = 15,name = "ali")

#不定长参数   接收元组
def add(x,y):
    print(x,"+",y,"=",x+y)

add(1,2)

def QiuHe(*args):         #  *args 无命名参数
    # print(args)
    sum = 1
    for i in args:
        sum += i
    print(sum)
QiuHe(3,4,6,75,8,990)


def dengji(**kwargs):         # **kwargs 键值对参数 有命名参数
    # print(args)
    for i in kwargs:
        print("%s : %s" %(i,kwargs[i]))

dengji(name="wunan",age="20")

def super(sex="male",*args,**kwargs):  #无命名参数必须放在有命名参数前面  ,默认参数放在无命名参数之前
    pass
# def super1(**kwargs,*args):
#     pass

####参数优先级
##必需参数》关键字参数》默认参数》无命名不定长参数》命名不定长参数