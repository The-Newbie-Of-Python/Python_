#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/25
'''

'''
import os
import time
from multiprocessing import Process


def info(title):
    print(title)
    print("moudle name:",__name__)
    print("parent process:",os.getppid())
    print("process id:",os.getpid())

def f(name):
    # info("\033[31;1mmain process line\033[0m")
    info("\033[31;1mfunction f\033[0m")
    print('hello',name)

if __name__ =="__main__":
    info("\033[32;1mmain process line\033[0m")
    time.sleep(10)
    p = Process(target=info,args=("bob",))
    p.start()
    p.join()