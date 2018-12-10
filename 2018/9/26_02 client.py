#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/26
'''

'''

import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1',8888)
sk.connect(address)

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp, 'utf8'))
    try:
        data = sk.recv(1024)
        print('......',str(data, 'gbk'))
    except Exception as e:
        break
sk.close()