#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/21
'''
函数返回值
'''

def m():
    print("....")

    #return None   #默认返回None
    return  1,"edgsdgs",[1,3,5,6]     #return 标志着函数结束,多个返回值会封装成一个元组返回
print(m())