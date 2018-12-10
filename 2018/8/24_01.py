#!/usr/bin/env python3
#-*- coding:utf8  -*-
# __author__ = "Auther"
# Date : 2018/8/24
'''
生成器
'''

#列表生成式：先用for语句将元素取出，进行操作后将元素再重新放入列表中
a = [x for x in range(10)]
b = [x*x for x in range(10)]
print(a,b)
print(type(a),type(b))


def f(n):
    return n**3
c = [f(x) for x in range(10)]
print(c)
print(type(c))

t = ("123",555)  #t=["123",5555]  t={a:1213,b:"1212"}  序列:字符串，列表，元组
a,b=t
print(type(t))
print(a)
print(b)


#***********************************************************************************************************#


#生成器不会直接生成内容，所以不会占大量内存，但是可以调用生成器的方法按顺序生成内容
#生成器就是一个可迭代对象 Iterable
s = (x*2  for x in range(5))  #<generator object <genexpr> at 0x0000020B9168C048>  生成器对象
print(s)
s.__next__()
print(s.__next__())
print(next(s))    # s.__next__() == next(s)
print(next(s))    # s.__next__() == next(s)
print(next(s))    # s.__next__() == next(s)
#for i in s:print(i)


#生成器对象的两种生成方式
#方式一、x for x in range(10)
#方式儿、yield

def ss():
    print("ok")
    yield 1    #返回一个值1，但是不结束
    print("ok2")
    yield 2
    return None
g = ss()
g.__next__()
next(g)
