#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/11
'''

'''
import threading

def Subnum():
    global num     #在每个线程中获取这个全局变量
    # time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000001)
    # num -= 1
    #
    r.acquire()
    temp = num
    print('ok!')
    num = temp - 1
    r.release()

num = 100
thread_list = []
r = threading.Lock()
for i in range(num):
    t = threading.Thread(target=Subnum)
    #print(t)
    t.start()
    #print(t)
    thread_list.append(t)
print(thread_list)

for i in thread_list:  #等待所有线程执行完毕
    t.join()

print(" final num ",num)