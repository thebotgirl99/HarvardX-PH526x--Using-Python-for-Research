"""
Created on Tue Aug  2 13:03:03 2022

@author: HP
"""



import numpy as np
import matplotlib.pyplot as plt
import random
import time

def increment(n):
    n += 1
    if n == 10:
        print(n)
n = 1
for i in range(10):
    n = increment(n)
print(n)

import numpy as np
matrix = np.zeros((3,3))
print(matrix)
A = np.array([[1,2],[3,4]])
B = A.transpose()
print(B)
print(A[0][1]) #same as print(A[0,1])
print(A[:,1]) #prints column, opp prints row

x = 20
print(not np.any([x%i == 0 for i in range(2, x)]))

x = np.linspace(0,10,10)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"rd-", linewidth = 2 , markersize = 12 ,label = "square")
plt.plot(x,y2,"bo-", linewidth = 2 , markersize = 12, label = "cube")
plt.legend(loc="upper left")
plt.axis([0, 11, 0, 101])
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("first_plot.pdf")

x = np.logspace(0,1,20)
y1 = x**2
y2 = x**3
plt.loglog(x,y1,"rd-", linewidth = 2 , markersize = 12 ,label = "square")
plt.loglog(x,y2,"bo-", linewidth = 2 , markersize = 12, label = "cube")
plt.legend(loc="upper left")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

x = np.random.gamma(2,3,100000)
plt.figure()
plt.subplot(221)
plt.hist(x, density = True, stacked = True)
plt.subplot(222)
plt.hist(x, bins = 30, density = True, stacked = True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative= True)
plt.subplot(224)
plt.hist(x, density = True, stacked = True, cumulative = True, bins = 30, histtype= "step")

die1 = list(range(1,7))
die2 = list(range(1,9))
die3 = list(range(1,11))
print(random.choice([random.choice(die1), random.choice(die2), random.choice(die3)]))

ys = []
for j in range(1000000):
    sums = 0
    for i in range(10):
       x = random.choice(list(range(1,7)))
       sums += x
    ys.append(sums)
plt.hist(ys)

x = np.random.randint(1,7,(1000000,10))
y = np.sum(x, axis=1)
plt.hist(y)

import time
start_time = time.process_time()
delta_x = np.random.normal(0,1,(2,10000))
sums = np.cumsum(delta_x, axis=1)
x0 = np.array([[0],[0]])
new = np.concatenate((x0, sums), axis = 1)
plt.plot(new[0],new[1], "bd-")
end_time = time.process_time()
print(start_time-end_time)
