#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = "Auther"
# Date: 2018/7/19

'''格式化输出'''

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit():
    salary = float(salary)
else:
    exit("must be digit")

msg = '''
------INFORMATION OF %s------
name : %s
age : %d
job : %s
salary : %.2f
------        END      ------
''' % (name,name,age,job,salary)

print(msg)
