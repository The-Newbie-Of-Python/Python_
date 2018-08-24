#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/7/30
'''
dict
'''

# dic1 = {}
#
# for i in range(10):
#     (key_ + i) = input("key_i = ")
#     value_i = input("value_i = ")
#     dic1.setdefault(key_i,value_i)
#
# print(dic1)

av_catalog = {
    "欧美":{
        "www.youporn.com":["很多免费，质量一般"],
        "www.pornhub.com":["很多免费，质量稍高"],
        "letmedothistoyou.com":["多是自拍，质量很高，资源少"],
        "x-art.com":["全部收费，屌丝绕道"]
},
    "日韩":{
        "tokyo-hot":["收费，质量一般"]
    },
    "大陆":{
        "1024":["全部免费，服务器在国外，速度慢"]
    }
}
av = "\n".join(av_catalog)
print(av_catalog)
print(av)

a = "wo"
b = "ai"
c = "ni"
d = a + b + c
e = "------".join([a,b,c])
f = "======".join((a,b,c))
print(d,"\n",e,"\n",f)

print(d .count("o"))
print(d.capitalize())
print(a.casefold())
print(d.center(50,"#"))
print(d.endswith("ni",5,6))
print(d.startswith("wo"))