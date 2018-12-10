#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/5
'''
计算器
'''
import re


#检查输入是否正确
def check_in(s):
    if re.search('[a-zA-Z]',s):
        print('U•ェ•*U Invalid')
    return s
#格式化输入
def format_in(s):
    s.replace(' ','')
    s.replace('++','+')
    s.replace('+-','-')
    s.replace('*+','*')
    s.replace('//','/')
    s.replace('--','+')
    return s
#乘除运算
def cal_mul_div(s):
    rule_mul_div = '-?\d+\.?\d*[*/]-?\d+\.?\d*'
    ret = re.search(rule_mul_div,s).group()
    if ret[1] =='*':
        s = float(ret[0]) * float(ret[2])
    if ret[1] =='/':
        s = float(ret[0]) / float(ret[2])
    return s
#加减运算
def cal_add_sub(s):
    rule_add = '-?\d+\.?\d*\+-?\d+\.?\d*'
    rule_sub = '-?\d+\.?\d*--?\d+\.?\d*'
    pass
    return s
#幂运算
def cal_mi(s):
    pass
    return s

#正式计算
print("\t\t\t(￢︿̫̿￢☆)Start Input(￢︿̫̿￢☆)\t\t\t")
source = input(">>>>>>")

if check_in(source):
    real_s = format_in(source)
    while source.count("(")>0:
        ret = re.search('\([^()]+\)',real_s).group()[1:-1] #(3+4*6)   3+4*6
        #print(ret,type(ret))
        # ret_mul_div = re.split('[\+\-*/]', ret)
        # for i in ret_mul_div:
        #     i = float (i)
        #     print(i)
        cal_mul_div(ret)

        # if re.search('[*/]',ret):
        #     re.split('[*/]',)
    else:
        pass
