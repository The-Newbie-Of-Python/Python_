#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/16
'''
队列  先进先出  FIFO
'''
import queue


d = queue.Queue(4)

d.put('hello',0)
d.put('world')
d.put('pyhton')
# d.put('pyhton',0)

#FIFO
print(d.get())
print(d.get())
print(d.get())