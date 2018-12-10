#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/21
'''

'''
import socket

sk = socket.socket()
print(sk)

address = ('127.0.0.1',8000)
sk.connect(address)

# while True:
#     data = sk.recv(1024)
#     T = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print(T)
#     print('........',str(data,'utf8'))
#     if not data:break
#     inp = input(T + '\n>>>')
#     sk.send(bytes(inp, 'utf8'))
# sk.close()
# T = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# data = sk.recv(1024)
# print(T)
# print(data)
while True:

    inp = input('>>>>')

    sk.send(bytes(inp, 'utf8'))
    try:
        data = sk.recv(1024)
    except Exception as e:
        break
    print('..........',str(data, 'utf8'))

sk.close()