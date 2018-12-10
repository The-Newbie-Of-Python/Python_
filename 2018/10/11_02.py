#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/11
'''

'''
import threading
import time


class MyThread(threading.Thread):

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number %s" %self.num)
        time.sleep(3)

if __name__ == "__main__":

    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()

