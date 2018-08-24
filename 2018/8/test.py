#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/7
'''
三级菜单改进
'''
# menu = {
#     '北京':{
#         '朝阳':{
#             '国贸':{
#                 'CICC':{},
#                 'HP': {},
#                 '渣打银行': {},
#                 'CCTV': {},
#
#             },
#             '望京':{
#                 '优衣库':{},
#                 'apple': {},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '阿泰包子':{},
#             },
#             '天通苑': {
#                 '链家':{},
#                 '我爱我家':{},
#             },
#             '回龙观':{},
#         },
#         '海淀':{
#             '五道口':{
#                 '谷歌':{},
#                 '网易':{},
#                 'Sohu':{},
#                 'Sogo':{},
#                 '快手': {},
#
#             },
#             '中关村':{
#                 'Youku':{},
#                 "Iqiyi":{},
#                 "汽车之家": {},
#                 "新东方": {},
#                 "QQ": {},
#
#             },
#         },
#     },
#     '上海':{
#         "浦东":{
#             "陆家嘴":{
#                 "CICC":{},
#                 "高盛": {},
#                 "摩根": {},
#             },
#             "外滩":{}
#         },
#         "闵行":{},
#         "静安":{},
#     },
#     '山东':{
#         "济南":{},
#         "德州":{
#             "乐陵":{
#                 "丁务镇":{},
#                 "城区":{}
#             },
#             "平原":{}
#         },
#         "青岛": {},
#
#     },
# }
#
# back_flag = False
# exit_flag = False
#
# while not back_flag and not exit_flag:                                                                                 #while True循环控制整个流程能够一直运行
#     for city in menu:                                                                                                   #
#         print("\t\t",city)                                                                                              #
#     choice = input("1>>>").strip()
#     if choice == "q":
#         exit_flag = True
#     if choice in menu:
#         while not back_flag and not exit_flag:
#             for state in menu[choice]:
#                 print("\t\t",state)
#             choice1 = input("2>>>").strip()
#             if choice1 == "b":
#                 back_flag = True
#             if choice1 == "q":
#                 exit_flag = True
#             if choice1 in menu[choice]:
#                 while not back_flag and not exit_flag:
#                     for landmark in menu[choice][choice1]:
#                         print("\t\t",landmark)
#                     choice2 = input("3>>>").strip()
#                     if choice2 == "b":
#                         back_flag = True
#                     if choice2 == "q":
#                         exit_flag = True
#                     if choice2 in menu[choice][choice1]:
#                         while not back_flag and not exit_flag:
#                             for company in menu[choice][choice1][choice2]:
#                                 print("\t\t",company)
#                             choice3 = input("4>>>").strip()
#                             if choice3 == "b":
#                                 back_flag = True
#                             if choice3 == "q":
#                                 exit_flag = True
#                             if choice3 in menu[choice][choice1][choice2]:
#                                 pass
#                         else:                                       #while True ... else跳出while循环
#                             back_flag = False
#                 else:
#                     back_flag = False
#         else:
#             back_flag = False
import sys

# menu = {
#     '北京':{
#         '朝阳':{
#             '国贸':{
#                 'CICC':{},
#                 'HP': {},
#                 '渣打银行': {},
#                 'CCTV': {},
#
#             },
#             '望京':{
#                 '优衣库':{},
#                 'apple': {},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '阿泰包子':{},
#             },
#             '天通苑': {
#                 '链家':{},
#                 '我爱我家':{},
#             },
#             '回龙观':{},
#         },
#         '海淀':{
#             '五道口':{
#                 '谷歌':{},
#                 '网易':{},
#                 'Sohu':{},
#                 'Sogo':{},
#                 '快手': {},
#
#             },
#             '中关村':{
#                 'Youku':{},
#                 "Iqiyi":{},
#                 "汽车之家": {},
#                 "新东方": {},
#                 "QQ": {},
#
#             },
#         },
#     },
#     '上海':{
#         "浦东":{
#             "陆家嘴":{
#                 "CICC":{},
#                 "高盛": {},
#                 "摩根": {},
#             },
#             "外滩":{}
#         },
#         "闵行":{},
#         "静安":{},
#     },
#     '山东':{
#         "济南":{},
#         "德州":{
#             "乐陵":{
#                 "丁务镇":{},
#                 "城区":{}
#             },
#             "平原":{}
#         },
#         "青岛": {},
#
#     },
# }
#
# current_layer = menu
# father_layer = []
#
# while True:
#     for key in current_layer:
#         print(key)
#     choice = input(">>>>>").strip()
#    # if len(choice) == 0:continue
#     if choice in current_layer:
#         father_layer.append(current_layer)
#         current_layer = current_layer[choice]
#     elif choice == "b":
#         if father_layer:
#             current_layer = father_layer.pop()
#     else:
#         print("none")
#

# a = { "beijing" :{"nihao" : 1123244241 } }
# b = str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a["beijing"])
# print(b[10:])
#
# b = eval(b)
# print(type(b))
# print(b["beijing"])


with open("customer","r") as customer:
    #
    # for line in customer.readlines():
    #     if line != "\n":
    #         # print(type(line))
    #         # print(type(eval(line)))
    #         line1 = eval(line)
    #         print(type(line1))
    #         print(line1)

    print(customer.read())
    customer.seek(0)
    if '1' in customer.read():
        print('fas')