#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:37:32 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os

print(os.getcwd())

import numpy as np

across_auc=np.zeros(shape=(102,102))

import glob

auc_files=sorted(glob.glob("*auc"))

print(auc_files)
for i in range(102):
    file=open(auc_files[i]).readlines()
    auc_list=[]
    for line in file:
        if "=" in line:
        
            auc_data=line.split(" ")[2]
            auc_list.append(auc_data)
        else:
            print(auc_files[i])
    across_auc[i]=auc_list
   
np.savetxt("CNN_cross_target.csv",across_auc,delimiter=",")    

import seaborn as sns

import matplotlib.pylab as plt

plt.subplot(111)



#ax=sns.heatmap(across_auc,linewidth=0.01,center=0.5,cmap="PiYG",cbar_kws={"ticks":[0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]})

from numpy import genfromtxt

adjusted_data=genfromtxt("ada_ada17_adjusted.csv",delimiter=",")




ax=sns.heatmap(adjusted_data,linewidth=0.01,center=0.5,cmap="PiYG",cbar_kws={"ticks":[0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]})
plt.xlabel("KNN Model Index")
plt.ylabel("Target Index")
plt.tight_layout()


plt.savefig("KNN_cross_AUC.png", dpi=2000)
plt.show


# TGFR1 index 92 has the most serious cross target overlap

print(adjusted_data[19])

index=0
for auc in adjusted_data[19]:
    
    if auc>0.9:
        
        print(auc_files[index])
        print(auc)
        print(index)
    
    index=index+1

#print(auc_files)
### the sorrted result changed

sorted(["ada17.8822", "ada.8823"])
sorted(["ada17_CNN_cross_predict.auc","ada_CNN_cross_predict.auc"])
sorted(auc_files)


# adjust the ada ada17 sequence 

