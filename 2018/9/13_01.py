#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/13
'''
分页
'''
class pageaddtion:

    def __init__(self,current_page):
        self.page = int(current_page)
        try:
            #qwer
            p = int(self.page)
        except Exception as e:
            p = 1
    @property
    def start(self):
        val = self.page * 10
        return val
    @property
    def end(self):
        val = (self.page + 1) * 10
        return val


li = []
for i in range(1000):
    li.append(i)

while True:
    p = input("page_number:")
    obj = pageaddtion(p)
    print(li[obj.start:obj.end])