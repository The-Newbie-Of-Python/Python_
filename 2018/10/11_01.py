#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/11
'''

'''
# import threading
#
# n = 0
# #lock = threading.Lock()
#
# def foo():
#     global n
#     n += 1
#
# threads = []
# for i in range(100):
#     t = threading.Thread(target=foo)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(n)


import threading

import requests

urls = [...]


def worker():
    while True:
        try:
            url = urls.pop()
        except IndexError:
            break  # Done.

        requests.get(url)


for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()