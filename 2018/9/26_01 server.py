#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/26
'''
远程执行命令
'''
import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1',8888)
sk.bind(address)
sk.listen(2)  #指定可以建立连接的个数，建立链接保持的数量，0可以建立1个链接，必须要指定
print('waiting...')

while True:
    conn,addr = sk.accept()
    print(addr,'已连接')
    while True:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        print('......',str(data,'utf8'))

        # obj = subprocess.Popen(str(data,'gbk'),shell= True,stdout= subprocess.PIPE)
        # cmd_result = obj.stdout.read()
        # conn.sendall(cmd_result)

        inp = input('>>>')
        conn.sendall(bytes(inp,'utf8'))

    conn.close()

