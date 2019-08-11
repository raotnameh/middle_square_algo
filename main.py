#python 2.7.15+ tested
# -*- coding: utf-8 -*-
"""
Code to reproduce middle square algorithm and plot to see the results if the numbers are randomly producing and all of them between 0 to 1.
"""

r=int(input("Enter number:\n"))
l=len(str(r))
list = []
# list.append(r)
while len(list) == len(set(list)) :
    x=str(r*r)
    if l % 2 == 0:
        x = x.zfill(l*2)
    else:
        x = x.zfill(l)
    y=(len(x)-l)/2
    r=int(x[y:y+l])
    list.append(r)
    

import numpy as np

list = np.array(list,dtype = 'float64')
print(list)
num = (max(list)-min(list))
print(num)
list = list/num

import time
import matplotlib.pyplot as plt

x = np.linspace(1,len(list),len(list))
plt.scatter(x,list)
