#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/9
'''
线程threading
IO密集型
计算密集型
'''

import threading
import time

begin = time.time()

def foo(n):
    print("this is %s" %n)
    time.sleep(2)
    print("end foo")

def bar(n):
    print('this is %s' %n)
    time.sleep(3)
    print('end bar')

# foo('haha')
# bar('huhu')
#创建线程对象
t1 = threading.Thread(target=foo,args=(1,))
t2 = threading.Thread(target=bar,args=(2,))
t1.start()
t2.start()

print('waiting....')

t1.join()
t2.join()

end = time.time()

spendtime = str(end - begin) + '秒'
print('消耗时间为%s' %spendtime)
