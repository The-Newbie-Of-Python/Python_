#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/8
'''
文件操作
'''
import time


f = open("document","r+",encoding="utf8")        #"r"只读   r+ 读写 不清空文件  ,光标位置在开头，可以读到内容
f1 = open("document1","w+",encoding="utf8")     #"w"清空文件  w+  写读，清空文件
f2 = open("document2","a+",encoding="utf8")      #"a"append ，追加模式   a+  追加读写，不清空文件，光标位置在末尾读不到内容
#data = f.read()
# f1.write("yes \n")
# f1.write("no")
# f2.write("\n\t  12313142141414")
# print(f1.tell())     #光标所在的”字节“位置
# print(f2.tell())
# f2.seek(30,0)
# print(f2.tell())
# print(f1.writable())
# print(f2.isatty())                  #  布尔值判断是否为终端
# print(f.readline())
# f.write("加油！！！")
# print(f.readline())
#
#
# print(f1.readline())
# f1.write("yeah!!!")
# f1.seek(0)
# print(f1.readline())



print(f2.readline())
f2.write("bingo!!!")
print(f2.tell())
f2.seek(0,0)
print(f2.readline())


f2.flush()           #将缓存中的内容立即写如磁盘

time.sleep(10)
#print(data)


f.close()