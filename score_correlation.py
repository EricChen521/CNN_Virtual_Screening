#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:59:40 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

# plot the correlation line of the predicted scores with/without receptor 
# in
import os 

print(os.getcwd())

import glob
receptor_file=sorted(glob.glob("*receptor*"))

ligand_file=sorted(glob.glob("*ligand*"))


## make sure the files are matched
for i in range(102):
    
    if receptor_file[i].split("_")[0] != ligand_file[i].split("_")[0]:
        print(receptor_file[i])
        print(ligand_file[i])
 
 
receptor_scores=[]
ligand_scores=[]

      
for file in receptor_file[0:102]:
    contents=open(file).readlines()
    for line in contents[0:-1]:
        score=line.split()[-1]
        receptor_scores.append(float(score))
        
for file in ligand_file[0:102]:
    contents=open(file).readlines()
    for line in contents[0:-1]:
        score=line.split()[0]
        ligand_scores.append(float(score))
        
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

results=sm.OLS(ligand_scores,sm.add_constant(receptor_scores)).fit()

print(results.summary())

plt.scatter(ligand_scores,receptor_scores,s=10)

plt.xlabel("score without receptor",size=12)
plt.ylabel("score with receptor", size=12)

from numpy.polynomial.polynomial import polyfit

x=np.array(ligand_scores)
y=np.array(receptor_scores)

b, m = polyfit(x,y,1)
plt.plot(x,b+m*x,"-",color="red")

# b=0.0016, m=0.993

import scipy

scipy.stats.pearsonr(ligand_scores,receptor_scores)



X_plot=np.linspace(0,1,100)
plt.savefig("all_targets_score_correlation.png",dpi=400) 
#plt.plot(X_plot,X_plot*results.params[0]+results.params[1])
plt.show()    # R squared 0.988

# person correlation 0.994

   