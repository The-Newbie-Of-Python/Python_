#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/23
'''
商城登陆系统
'''
import time

#注册
def zhuce():
    with open("customer", "r+") as customer:  # open("nick","w+") as nick ,open("passwd","w+") as passwd:
    # nick.write("user=%s"%user)
    # passwd.write("password=%s"%password)
        while True:
            customer.seek(0)                                                                                                            # 让光标回到开头位置
            user = input("Please input your nick:")
            if user not in customer.read():                                                                                         #判断注册的用户名是否已经存在
                password = input("Please input your password:")
                sex = input("Please input your sex:")
                phonenumber = input("Please input your phonenumber:")
                job = input("Please input your job:")
                mail = input("Please input your mail:")
                user_info = {user: {"password": password, "sex": sex, "phonenumber": phonenumber, "job": job, "mail": mail}}      #将用户信息打包成字典存储
                #customer.write("\nuser:%s\npassword:%s"%(user,password))
                customer.write(str(user_info))
                customer.write("\n")
                break
            else:
                print("Repeat nick ,try again!!!")
                time.sleep(1)



'''
字典存放用户信息，再将字典信息存放在文档中
{User:{Password:xxx,Sex:xxx,Phonenumber:xxx,Job:xxx,Mail:xxx,}}
'''

login_status = False
#登陆 装饰器
def login_(f):
    def login():
        global login_status
        if login_status == False:
            with open("customer","r") as customer:
                while True:
                    customer.seek(0)                                                    #对比txt内容前让光标回到开头位置
                    user = input("user=")
                    password = input("password=")
                    flag = "false"
                    if user in customer.read():
                        customer.seek(0)                                           #遍历前让光标回到开头位置
                        for line in customer.readlines():                               #遍历txt文件
                            if line != "\n":
                                line1 = eval(line)                                      #将字符串转化成字典
                                if user in line1 and line1[user]["password"] == password:
                                    print("welcome !!!")
                                    flag = "true"
                                    login_status = True                         #该代码中flag和login_status都是标志位
                                    break                                       #跳出for循环
                        if flag == "true":                                      #如果跳出了for循环才跳出while循环
                            f()
                            break                                                  #跳出while循环
                    else:
                        print("Please check your information,error nick or password !!!")
                        time.sleep(1)
        else:
            f()
    return login




@login_
#主菜单
def menu_main():
    print("...")

@login_
#菜单一
def menu1():
    print("....")

#zhuce()

menu_main()
menu1()