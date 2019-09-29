#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:53:29 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import numpy as np

from sklearn.metrics import roc_auc_score

actives=[1 for i in range(50)]
decoys=[0 for i in range(50)]

y_true= np.array(actives+decoys)

import random 



AUC=[]

Y_scores=[]
for i in range(100):
    Y_scores.append(random.random())
    
    
for i in range(100000):
    
    random.shuffle(Y_scores)
   
    """
    for j in range(100):  
        #random.seed(123)
        Y_scores.append(random.random())
    """
    auc=roc_auc_score(y_true,np.array(Y_scores))
    AUC.append(auc)   

#print(AUC) 

import matplotlib.pyplot as plt

plt.hist(np.array(AUC),bins='auto')
plt.show()
    