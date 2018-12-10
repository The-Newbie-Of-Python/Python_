#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/9
'''

'''

import threading
import time

def music(func):
    for i in range(2):
        print("Begin listening to %s. %s" %(func,time.ctime()))
        time.sleep(2)
        print("End listening %s" %time.ctime())

def move(func):
    for i in range(2):
        print("Begin watching to %s. %s" %(func, time.ctime()))
        time.sleep(3)
        print("End watching %s" %time.ctime())


threads = []
t1 = threading.Thread(target=music,args=('七里香',))
t2 = threading.Thread(target=move,args=('头文字D',))
threads.append(t1)
threads.append(t2)


if __name__ == "__main__":

    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print("All over %s" %time.ctime())
