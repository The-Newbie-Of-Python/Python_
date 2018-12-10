#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/3
'''
re模块
正则表达式
匹配字符串的
正则表达式可以提供模糊匹配的方法
字符串string提供的的完全匹配的方法

默认符合贪婪匹配规则
正则元字符： . ^  $  *  +  ?  { }  [ ]  |  ( )  \
.  :  通配符 只能代指任意(一个)字符，不包括换行符"\n"
^  :  尖角符 放开头从开头开始匹配 ,放在中括号中加字符代表取反[^m,v,f,n]
$  :  $符 放末尾从末尾开始匹配
*  ： 星  重复匹配匹配的数量从0到正无穷[0,+∞]      * = {0,+∞}
+  ： 加号  重复匹配 [1,+∞]                       + = {1,+∞} = {1,}
?  :  问号  重复匹配[0,1]零或者一次                 ? = {0,1}
{ }： 大括号  重复匹配 次数自己规定
[ ]:  中括号  互斥匹配 相当于或  [a,b,c]   取消元字符的特殊功能(例外  \  , ^  , - )   [^4,5]取反，非
\  :   反斜杠  \+元字符  去除元字符特殊功能    \+部分普通字符  实现特殊功能
    \d :匹配任何十进制数 类似于[0-9]
    \D :匹配任何非数字字符 类似于[^0-9]
    \s :匹配任何空白字符 类似于[\t\n\r\f\v]
    \S :匹配任何非空白字符  类似于[^ \t\n\r\f\v]
    \w :匹配任何字母数字字符 类似于[0-9a-zA-Z]
    \W :匹配任何非字母数字字符 类似于[^ 0-9a-zA-Z]
    \b :匹配一个单词边界，也就是指单词和空格间的位置
( ): 小括号  分组匹配
|  :  管道符  或
'''

import re


# s = "hello world !!"
# print(s.find("llo"))            #2
# ret = s.replace("ll","xx")
# print(ret)                      #hexxo world !!
# print(s.split(" "))             #['hello', 'world', '!!']

# ret1 = re.findall("w\w{2}l","hello world")
# ret2 = re.findall("w..l","hello world")
# ret3= re.findall("w.l","hello w\nld")
#
# print(ret1,ret2,ret3)



# ret1 = re.findall("^h...o","hello world")
# ret2 = re.findall("^h...o","hdshjsghsjhello")
#
#
# print(ret1,ret2)


# ret1 = re.findall("h...o$","hello world")
# ret2 = re.findall("h...o$","hdshjsghsjhello")
#
#
# print(ret1,ret2)


# ret = re.findall("dss*","qdskbjablbjkfaishifjoeirhjcbknjbcjzbajdofihogcbvasndcndjng")
# print(ret)
#
# ret = re.findall("dsv+","qdskbjablbjkfaishifjoeirhjcbknjbcjzbajdofihogcbvasndcndjng")
# print(ret)


# ret = re.findall("qd{9}k","qdddddddddkfaishifjoeirhjcbknjbcjzbajdofihogcbvasndcndjng")
# print(ret)
# ret = re.findall("qd{1,9}k","qdddddddddkfaishifjoeirhjcbknjbcjzbajdofihogcbvasndcndjng")
# print(ret)


# ret = re.findall("q[a,b,d]g","qdddddddddkfaishifjoeirhjcbknjbcjzbajdofihogcbvasndcndjng")
# print(ret)
# ret = re.findall("qq[ com , cn ]","qq.com")
# print(ret)
# ret = re.findall("[a-z]","adx")
# print(ret)
# ret = re.findall("[w,*,.,]",",wad.x*")
# print(ret)
# ret = re.findall("[0-9a-zA-Z]","12asER")
# ret = re.findall("[0-9,a-z,A-Z]","12asER")
# print(ret)
# ret = re.findall("[^1]","12as， ER")
# print(ret)
ret = re.findall('\d{11}','asdfsfsd233243532178168968496218527846176491312')
print(ret)

ret = re.search("(abc)+","asdasdggdfabcabc")
print(ret)
print(ret.group())

#findall  返回所有的值到一个列表
#search     返回一个对象，用group查看
#match       从开头开始返回一个对象，用group查看
#spilt