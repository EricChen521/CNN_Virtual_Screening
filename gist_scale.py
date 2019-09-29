#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:04:28 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

# this script will scale the value in to value/Max_value, therefore in the new dx file, the max value 
# will be 1, others are the percentage of the max.


import os,sys

import numpy as np

from gridData import Grid

g=Grid(sys.argv[1])

values=g.grid

coordinates=g.edges

max_value=np.amax(values)

scaled_values=values * (1/max_value)

g_scaled=Grid(scaled_values,edges=coordinates)


g_scaled.export(sys.argv[1].split(".")[0]+"_scaled.dx","DX")

"""

# plot to test the result

import matplotlib.pyplot as plt

x=[]
y=[]
point=0
for i in range(48):
    for j in range(48):
        for k in range(48):
            y.append(scaled_values[i,j,k])
            point+=1
            x.append(point)
            k=k+1
        j=j+1
    i=i+1
    
fig=plt.figure()

ax1=fig.add_subplot(111)
ax1.plot(x,y,c="b")
plot.show()
"""
