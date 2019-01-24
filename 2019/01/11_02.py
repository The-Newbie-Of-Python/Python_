#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2019/1/11
'''

'''
import json


def store(data):
    with open('data.json', 'a+') as json_file:
        json_file.write(json.dumps(data))
        json_file.write('\n')


def load():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data



if __name__ == "__main__":
    #
    # data = time.strftime("%Y-%m-%d %H:%M:%S")
    # store(data)

    data = load()
    print (data)
    print (type(data))