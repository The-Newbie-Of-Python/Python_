#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/21
'''
函数
#避免重复代码
#保持代码一致性
#方便修改易于扩展
'''
import time

def logger():
    #n = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)

    with open("日志信息","a+",) as l:
        l.write("%s end action\n" %(current_time))

# f = open("","",)
# f.close()

def action1():
    print("starting action%s......")
    logger()
def action2():
    print("starting action%s......")
    logger()
def action3():
    print("starting action%s......")
    logger()


#if __name__ == "__main__":
action1()
action2()
action3()



