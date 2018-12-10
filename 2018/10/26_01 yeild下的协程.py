#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/26
'''

'''


def menu():
    print("\033[33;1mWelcome\033[0m")
    num = int(input("Please check how many baozi do you need:"))
    return num

def consumer(name):
    print("\033[32;1m---- starting ----\033[0m")
    while True:
        new_baozi = yield
        print("%s eating baozi %s" %(name,new_baozi))

def producer(num):
    next(con1)
    next(con2)
    n = 0
    while n < num:
        n +=1
        print("\33[32;1m[producer]\33[0m is making baozi %s" %n)
        con1.send(n)
        con2.send(n)

if __name__ == "__main__":
    con1 = consumer("c1")
    con2 = consumer("c2")
    m = menu()
    p=producer(m)
