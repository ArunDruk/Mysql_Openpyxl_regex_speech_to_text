# import re
# from selenium import webdriver
#

# journal=[""]
# # for i in journal:
# #     if i is None:
# #         print("Hello")
# print(len(journal))
# if any(journal) == False:
#     print("Hello")

# n=int(input())
#
# T = tuple(map(int,input().split()))
# print(T)
# print(hash(T))

# from datetime import datetime
#
# now1=datetime.now().strftime("%d(DD)-%m(MM)-%Y(yyyy) %H(hr):%M(min):%S(ss) ")
# print(now1)

# from random import randint
#
# a=randint(10,99)
# print(a)

# L=[0,0]
#
# if any(L):
#     print("True")
# else:
#     print("Some element is false")

# D ={"vehicle" : "Car","Make":"Honda","Model":1995}
#
#
# D["Made"]="Spanish"
# print(D)
#
# D.pop("Make")
# print(D)
#
# del D["Made"]
#
# print(D)
# global x, y
# class my_class():
#    x=4
#    y=4
#    def method1(self):
#         return x*y
#
#
# a=my_class()
# print(a.method1())

# import re
#
# txt = "The rain in Spain, comain"
#
# pattern=re.compile(r'ai')
# matches = pattern.finditer(txt)
#
# for match in matches:
#     print(match)

# s="5678"
# k=s.zfill(6)
# print(k)

# with open("text_file_with_limit.txt",'r+') as fr:
#     to=fr.readlines()
#     # with open("sample_test_write",'w') as fw:
#     #     fw.writelines(to)



# # import os
# #
# # print(os.getcwd())
# #
# # os.chdir("C:\\Arun")
# #
# # print(os.getcwd())
# # print(os.listdir())
# A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1=range(10)
# print(A1,type(A1))
# print(A0,type(A0))
#
# # A2=sorted([i for i in A1 if i in A0])
# # print(A2,type(A2))
#
# # A3= [[i,i*i] for i in A1]
# # print(A3,type(A3))
#
# A4 = {i:i*i for i in A1}
# print(type(A4),A4)

# global l
# l=[]
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#         # print(l)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)


# def outer_func(func1):
#     def inner_func():
#         print("Good Morning")
#         func1()
#         print("How are you Doing!!")
#     return inner_func
#
# @outer_func
# def main_func():
#     print("Hello Arun")
#
# main_func()


# import random
# L=random.randint(1,1035)
# print(L)
# from datetime import datetime
# import re
# gl_date=str(datetime.now().strftime("%d-%b-%Y")).upper()
# s="Invoice Date: 10-JUL-19"
# inv_date=str(datetime.now().strftime("%d-%b-%y")).upper()
# new_s=re.sub(r'Invoice\sDate:\s\d{2}-[A-Z]{3}-\d{2}',"Invoice Date: "+inv_date,s)
# print(s)
# print(new_s)

import pytest

def tc_1():
    print("This is the output of test1")

def tc_2():
    print("This is the output of test2")

def tc_3():
    print("This is the output of test3")







































