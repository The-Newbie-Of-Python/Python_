#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/29
'''
os
'''
import os

print(os.getcwd())   #C:\Users\38454\Desktop\Road_Of_Python-master\2018\8   获取当前工作目录

#os.chdir(r"C:\Users")   #修改工作目录
print(os.curdir)
print(os.pardir)
#os.makedirs("8\\abc\\123")   #创建多层目录dir
#os.mkdir("8\\2324\\34")
#os.removedirs("8\\abc\\123")
#os.remove("8")
dirs = os.listdir(r"C:\Users\38454\Desktop\Road_Of_Python-master\2018\8")
print(dirs)
#r  原生字符串，所有内容不具备转义功能 例如"\n"
#os.remove()  #只能删除文件，不能删除文件夹
#os.rename("29_01 os模块","29_01 os模块.py")
print(os.stat(r".\29_01 os模块.py"))
#print(info.st_size)
s = os.sep          #输出当前操作系统特定的路径分隔符
print(s)
print(os.linesep)   #输出当前平台使用的行终止符
print(os.pathsep)   #输出用于分隔文件路径的字符串

print("C:%sUsers%s38454%sDesktop%sRoad_Of_Python-master%s2018%s8" %((s,)*6))
b = ("C:%sUsers%s38454%sDesktop%sRoad_Of_Python-master%s2018%s8" %((s,)*6))
os.system("dir")  #输入系统bash命令
print(os.environ)  #系统环境变量
print(os.path.abspath("./21_03"))   #取绝对路径
print(os.path.split(b))
print(os.path.dirname("./21_03"))
print(os.path.join(os.getcwd() , "7"))
#os.path.join()
print(os.fspath(r"C:\Users\38454\Desktop\Road_Of_Python-master\2018"))