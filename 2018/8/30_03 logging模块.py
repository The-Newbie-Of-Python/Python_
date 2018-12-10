#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/30
'''
logging模块
'''

import logging

#日志级别
# # logging.debug("debug message")
# # logging.info("info message")
# # logging.warning("warning message")                  #默认级别     WARNING:root:warning message
# # logging.error("error message")                      #ERROR:root:error message
# # logging.critical("critical message")                #CRITICAL:root:critical message
# # #如果没有设置级别的话从warning级别开始记录，warning和error，critical
# #
# #配置日志
# logging.basicConfig(
#                     level= logging.DEBUG,
#                     format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",
#                     datefmt= "%a %d %b %Y %H:%M:%S",
#                     filename="test.log",
#                     filemode="w"
#                     )
#
#
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")  #默认级别
# logging.error("error message")
# logging.critical("critical message")


logger = logging.getLogger()

#创建一个handler用于将日志输入到文件中
fh = logging.FileHandler("test.log")
#创建一个handler用于将日志打印在屏幕上
ch = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setLevel(level=logging.INFO)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logging.debug("logger debug message")
logging.info("logger info message")
logging.warning("logger warning message")  #默认级别
logging.error("logger error message")
logging.critical("logger critical message")