# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:38:45 2022

@author: HP
"""


with open("names.txt") as file:
    for line in file:
        print("hello", line.rstrip())

#sum([if i%2 != 0 for i in range(10)])

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear] == "friendly":
        print("Hello, "+bear+" bear!")
    else:
        print("odd")

x = [1,[2]]
print(type(x))
print(type(x[0]))
print(type(x[1]))

l1 = [2,3,4]
l2 = [2,3,4]
print(l1 is l2)

l1 = [2,3,4]
l2 = l1
l1[0] = 24
print(l1)
print(l2)

x = set([1,2,3])
y = set([2,3,4])
print(x.symmetric_difference(y))
x = set([1,2,3])
y = set([2,3,4])
print(y.difference(x))

import random
print(dir(random))

a = 5
def sum():
    global a
    a = 7
    b = 3
    return a+b
print(a)
print(sum())
print(a)

L = [1,2,3,4]
def modify(list):
    list[0] *= 10
    return list
M = modify(L)
print(L)
print(M)
print(L is M)

def intersection(s1,s2):
    res = []
    for i in s1:
        for j in s2:
            if i == j:
                res.append(i)
                break
    return res
print(intersection([1,2,3,4], [2,3,6,7]))    

import random
def password(l):
    pas = str()
    c_set = "ABCD1234"
    for i in range(l):
        pas = pas + random.choice(c_set)
    return pas
print(password(5))
               
