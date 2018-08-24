#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/6
'''
三级菜单
'''

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP': {},
                '渣打银行': {},
                'CCTV': {},

            },
            '望京':{
                '优衣库':{},
                'apple': {},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑': {
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五道口':{
                '谷歌':{},
                '网易':{},
                'Sohu':{},
                'Sogo':{},
                '快手': {},

            },
            '中关村':{
                'Youku':{},
                "Iqiyi":{},
                "汽车之家": {},
                "新东方": {},
                "QQ": {},

            },
        },
    },
    '上海':{
        "浦东":{
            "陆家嘴":{
                "CICC":{},
                "高盛": {},
                "摩根": {},
            },
            "外滩":{}
        },
        "闵行":{},
        "静安":{},
    },
    '山东':{
        "济南":{},
        "德州":{
            "乐陵":{
                "丁务镇":{},
                "城区":{}
            },
            "平原":{}
        },
        "青岛": {},

    },
}

back_flag = False
exit_flag = False

while not back_flag and not exit_flag:
    for key in menu:#打印第一层 (循环第一层)
        print(key)
    choice = input(">>:").strip()
    if choice == "q":
        exit_flag = True
    if choice in menu:#打印第二层
        while not back_flag and not exit_flag:#让程序停留在第二层
            for key2 in menu[choice]:
                print(key2)
            choice2 = input(">>:").strip()
            if choice2 == "b":
                back_flag = True
            if choice2 == "q":
                exit_flag = True
            if choice2 in menu[choice]:
                while not back_flag and not exit_flag:#False
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input("3>>:").strip()
                    if choice3 == "b":
                        back_flag = True
                    if choice3 == "q":
                        exit_flag = True
                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_flag:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input("4>>:").strip()
                            print("last level")
                            if choice4 == "b":
                                back_flag=True
                            if choice4 == "q":
                                exit_flag=True
                        else:
                            back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False
