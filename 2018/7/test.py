#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "Auther"
# Date: 2018/7/19

# import time
#
# counter = 0
#
# date0 = time.time()
# print(date0)
#
# while 1:
#     if counter < 2**16:
#         counter += 1
#     else:
#         date1 = time.time()
# print(date1)
# print("over")
#
# a = [1,23,45,645,6,756,4653,6,5,474,565,47,475,43,524]
# #a.sort()
# b = sorted(a)
# print(a)
# print(b)


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
#
