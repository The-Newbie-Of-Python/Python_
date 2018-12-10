#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/10/26
'''

'''
from  urllib.request import urlopen


def fun(url):
    print("GET %s:" %site)
    resp = urlopen(url)
    data = resp.read()
    with open("%s.html" %site,"wb") as f:
          f.write(data)
    print("%d bytes received from %s" %(len(data),url))



if __name__ == "__main__":

    site = str(input("\033[32;1mplease input url:\033[0m"))

    url = "http://www."+ site + ".com"
    fun(url)
    # url_list = []
    # flag = True
    # while flag:
    #     url = str(input("\033[32;1mplease input url:\033[0m"))
    #     url_list.append(url)
    #     if url == "exit":
    #         flag = False
    #
    # start_time = time.time()
    #
    # gevent.joinall(
    #     [
    #         gevent.spawn(fun,"%s"%url_list[0]),
    #         gevent.spawn(fun,"%s"%url_list[1]),
    #         # gevent.spawn(fun,"%s"%url_list[2]),
    #     ]
    # )
    # end_time = time.time()
    # spend_time = end_time - start_time
    # print(spend_time)