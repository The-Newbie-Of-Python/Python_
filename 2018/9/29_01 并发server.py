#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/29
'''
利用框架实现并发
'''
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("服务端启动成功...")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(self.client_address,'\n',str(client_data,'utf8'))
                print('waiting...')
                #conn.sendall(client_data)
                inp = input('>>>')
                conn.sendall(bytes(inp,'utf8'))
            conn.close()




if __name__ == "__main__":

    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),Myserver)

    server.serve_forever()