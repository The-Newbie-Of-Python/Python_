#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/6
'''
三级菜单改进
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

current_layer = menu #实现动态循环
# parent_layer = menu

parent_layers = []#保持所以父级 ，最后一个元素永远都 是父亲级

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:#改之前相当于父亲
        parent_layers.append(current_layer)#在进入下一层之前，把当前层追加到父级
        #下一次loop  当用户选择b的选择，就可以直接取列表的最后一个值出来就ok了
        current_layer = current_layer[choice]#改成了子层
    elif choice == "b":
        # current_layer = parent_layer
        if parent_layers:#判断是否为空
            current_layer = parent_layers.pop()#取出列表最后一个值，因为他就是当前的父值
    else:
        print("无此项")