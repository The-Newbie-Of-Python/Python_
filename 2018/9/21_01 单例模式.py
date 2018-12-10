#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/21
'''
单例模式
'''

import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("Hello boy!")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()