#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "Auther"
# Date: 2018/7/23

'''购物车程序'''
import time

print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            WELCOME TO JD SHOP                          
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
)

#Mycharge =float(input("Please input your charge number :"))
Shop_list = [
    ("iphoneX",8000),
    ("macbook",9000),
    ("iwatch",2000),
    ("ipod",1000),
    ("ipad",3000)
             ]
Shop_car = []

# print(
# "+++++++++++++++++++++++Shop_list+++++++++++++++++++++++++++++++++++++++++++\n"
# "iphoneX: 8000\nmacbook: 9000\niwatch: 2000\nipod: 1000\nipad: 3000""\n",
# "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
# )

# x = input("_____")
# if x in Shop_list:
#     print(x)

# y = float(Mycharge)
# BOX = []

# class box():
#     def addbox(self,x):
#         while True:
#             if x not in Shop_list:
#                 exit("not alivable!!!")
#
#             elif y < Shop_list.get(x):
#                 exit("余额不足")
#
#             else:
#                 return(x)
#                 BOX.append(x)
#                 y = float(Mycharge) - Shop_list.get(x)
#                 print(BOX)
#                 print(y)
#
# if __name__ == '__main__':
#     object = box()
#     object.addbox(x)
saving = input("Please input your saving:")

if saving.isdigit():
    saving = int(saving)
    while True:
    #    for i in Shop_list:
    #        print(Shop_list.index(i),i)
        for i,v in enumerate(Shop_list,1):
            print(i,">>>",v)

        choice = input("the number of goods[EXIT:q]:")

        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(Shop_list):
                S_item = Shop_list[choice-1]
                print(S_item)
                if S_item[1] <= saving:
                    saving -= S_item[1]
                    Shop_car.append(S_item[0])
                else:
                    print("Saving is not enough !!!")

            else:
                print("invalivd number")
                sleep(5)

        elif choice == "q":
            print("+++++++++++++++++++shopped list+++++++++++++++++++++++++")
            for i in Shop_car:
                print(i)
            print("The saving is %s:"%saving)
            exit("Thks for shopping !!!")
        else:
            print("Invalid input")
else:
    exit("Invalid input!!!!")