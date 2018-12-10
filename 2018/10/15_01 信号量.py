#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/15
'''
信号量   threading.BoundedSemaphore( ) 控制线程数量
'''
import threading
import time


class MyThread(threading.Thread):

    def run(self):

        if semaphore.acquire():

            print(self.name)

            time.sleep(3)

            semaphore.release()

if __name__ == "__main__":

    semaphore = threading.BoundedSemaphore(20)

    thrs = []

    for i in range(100):

        thrs.append(MyThread())

    for t in thrs:

        t.start()
