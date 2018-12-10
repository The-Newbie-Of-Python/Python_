#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/4
'''
计算器
'''

# import re
# import time
#
# #输出当前时间
# def sj():
#     shijian = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#     print("\tWelcome\n",shijian)
#
# #sj()
# # + - * / ^
# #幂函数
# def Mi(x,y,n=1):
#     if x > 0:
#         if y > 1:
#             for i in range(y):
#                 n = x * n
#             return n
#         elif y == 0:
#             n = 1
#             return n
#         elif y == 1:
#             n = x
#             return n
#         elif y == -1:
#             n = 1/x
#             return n
#         else:
#             for i in range(abs(y)):
#                 n = x * n
#             return 1/n
#     elif x == 0:
#         return 0
#     else:
#         if y % 2 == 0:
#             if y > 0:
#                 for i in range(abs(y)):
#                     n = x * n
#                 return n
#             elif y < 0:
#                 for i in range(abs(y)):
#                     n = x * n
#                 return 1/n
#             elif y==0:
#                 n = 1
#                 return n
#         else:
#             if y > 0:
#                 for i in range(abs(y)):
#                     n = x * n
#                 return n
#             elif y < 0:
#                 for i in range(abs(y)):
#                     n = x * n
#                 return (1/n)
#             elif y == 0:
#                 n = 1
#                 return n
#
# num = input("Please input number :")
# ret = re.findall('\([^()]+\)',num)
# print(ret)

######################################################华丽的分割线######################################################
import re

source = input("") #520+657*589-(705.78+578)/(9076-(56783*653+7843.88))

#合法检查
def check(s):
    flag =True
    if re.search('[a-zA-Z]',s):
        print("Error Input")
        flag = False
    return flag

#合规检查且返回有效值
def format(s):
    s = s.replace(' ','')
    s = s.replace('++','+')
    s = s.replace('--','-')

    return s

def cal_mul_div(s):
    ret = re.search('[\-]?\d+\.?\d*  [*/]  [\-]?\d+\.?\d*',s).group()
    #x,y = float(re.split('[*/]',ret))
    if ret[1] =='*':
        s = float(ret[0])*float(ret[2])
    elif ret[1] == '/':
        s = float(ret[0])/float(ret[2])
    return s

def cal_add_sub(s):
    ret = re.search('[\-]?\d+\.?\d*  \+  [\-]?\d+\.?\d*', s).group()
    #ret2 = re.search('\d+\.?\d*-\d+\.?\d*', s).group()
    if ret:
        s = float(ret[0]) + float(ret[2])
    else:
        s = float(ret[0]) - float(ret[2])
    return s

if check(source):
    real_s = format(source)

    while re.search('\(',real_s):
        real_s = re.search('\([^()]+\)',real_s).group()
        if re.search('[*/]', real_s):
            real_s = cal_mul_div(real_s)
            real_s = cal_add_sub(real_s)
        else:
            real_s = cal_add_sub(real_s)

    else:
        if re.search('[*/]', real_s):
            real_s = cal_mul_div(real_s)
            real_s = cal_add_sub(real_s)
        else:
            real_s = cal_add_sub(real_s)
