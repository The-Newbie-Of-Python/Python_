#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/9/17
'''
一、成员修饰符
        公有成员
        私有成员 __ 包括静态字段，普通字段，静态方法，普通方法，构造方法__init__
            无法直接访问，需要间接访问

二、特殊成员
三、metaclass
四、异常处理
五、反射
六、单例模式
'''

# class Foo:
#
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#
# obj = Foo()
# obj()  # 对象加括号
# # Foo()()


# class Foo1:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return 'abc'
#
#     def __int__(self):
#         return 123
#
# obj = Foo1()
# print(obj,type(obj))
# i = str(obj)
# print(i)
# r = int(obj)
# print(r)


# class Foo2:
#
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#
#     def __str__(self):
#         return '%s-%s'%(self.name,self.age)
#
# obj = Foo2('wun',18)
# print(obj)


# class Foo3:
#
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#
#     def __add__(self, other):
#         # return 123
#         return self.age + other.age
#
#
#
# obj1 = Foo3('wun',13)
# obj2 = Foo3('maz',13)
# r = obj1 + obj2
# print(r,type(r))

# while True:
#
#     try:
#         #代码块，逻辑
#         inp = input("输入序号：")
#         i = int(inp)
#
#     except IndexError as e:
#         print("IndexError",e)
#
#     except ValueError as e:
#         print("ValueError",e)
#
#     except Exception as e:  #Exception可以捕获所有的异常错误
#         #如果上述代码块出错，自动执行当前块内容
#         print("Exception",e)
#         i = 1
#     else:
#         print("That's ok")
#     finally:
#         print(i)


# import time
# t0 = time.localtime()
# T = time.strftime('%Y-%m-%d %H:%M:%S',t0)
# print(T)
# def db():
#
#     pass
#     return False
# while True:
#     t1 = time.localtime()
#
#     try:
#         i = input("input:")
#         r = int(i)
#
#         m = db()
#         if m is not True:
#             raise Exception("数据库错误")
#     except Exception as e:
#         T = time.strftime('%Y-%m-%d %H:%M:%S', t1)
#         print("Error", e)
#         str_error = str(e)
#         f = open("error_log", "a")
#         f.write(T + "\t" + str_error)
#         f.write('\n')
#         f.close()


'''自定义异常'''
class MyError(Exception):

     def __init__(self,msg):
         self.message = msg

     def __str__(self):
         return self.message

try:
    pass
    raise MyError('I \'m wrong' )
except MyError as e:
    print(e)

'''断言'''
assert 1==2   #条件成立才执行，不成立报错