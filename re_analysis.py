#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:54:29 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 

from numpy import genfromtxt

import seaborn as sns

import matplotlib.pylab as plt

data=genfromtxt("revised_AD_CNN_cross.csv",delimiter=",")

data[0,0]=0.93456
print(data[0,0])

ax=sns.heatmap(data,linewidth=0.01,center=0.5,cmap="PiYG",cbar_kws={"ticks":[0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]})
    
plt.xlabel("CNN model Index")
plt.ylabel("Target Index")
plt.tight_layout()

plt.savefig("revised_AD_cross_AUC.png",dpi=400)
plt.show()


import pandas as pd

data=pd.read_excel("revised_AD_CNN_cross.xlsx")



models=list(data.columns.values)

targets=list(data.index.values)

subsets={"GPCR":set(['aa2ar','adrb1','adrb2','cxcr4','drd3']),
         "Kinase":set(['abl1','akt1','akt2','braf','cdk2','csf1r'
                       ,'egfr','fak1','fgfr1','igf1r','jak2','kit','kpcb',
                       'lck','mapk2','met','mk01','mk10','mk14','mp2k1',
                       'plk1','rock1','src','tgfr1','vgfr2']),
    "Nuclear Receptor":set(['andr','esr1','esr2','gcr','mcr','ppara','ppard',
                            'pparg','prgr','rxra','thb']), 
    "Protease":set(['ace','ada17','bace1','casp3','dpp4','fa10','fa7','hivpr',
                    'lkha4','mmp13','reni','thrb','try1','tryb1','urok']),
    "Ion Channel":set(['gria2','grik1'])}



same_target_AUC=[]
same_function_AUC=[]
diff_function_AUC=[]


for target in targets:
    
    # get the function of target
    target_function="other"
    for sub in subsets:
        if target.lower() in subsets[sub]:
            target_function=sub
            
    for model in models :
        
        model_name=model.split()[0]
        
        # get the model function 
        model_function="other"
        for sub in subsets:
            if model_name.lower() in subsets[sub]:
                model_function=sub
        
        value=data.at[target,model]
        
        if target == model_name:
            same_target_AUC.append(value)
            
        elif target_function == model_function and target_function != "other":
            same_function_AUC.append(value)
        else:
            diff_function_AUC.append(value)
        

import statistics as sta

same_target_mean=sta.mean(same_target_AUC)  # AD:0.927   DUDE: 0.983
same_target_stdev=sta.stdev(same_target_AUC) # AD: 0.060  DUDE: 0.019

same_function_mean=sta.mean(same_function_AUC) # AD:0.682 DUDE: 0.835
same_function_stdev=sta.stdev(same_function_AUC) # AD:0.137 DUDE: 0.133

diff_function_mean=sta.mean(diff_function_AUC) # AD: 0.500   DUDE:0.618
diff_function_stdev=sta.stdev(diff_function_AUC) # AD: 0.165 DUDE: 0.176


for i in range(102):
    if same_target_AUC[i]<0.9:
        print(i)
        print(same_target_AUC[i])

from matplotlib import pyplot

import numpy

fig=pyplot.figure()

bins=numpy.linspace(0,1,60)

pyplot.hist(same_target_AUC,bins,density=1,label="Same target",color='red',alpha=0.7)
pyplot.hist(same_function_AUC,bins,density=1,label="Similar function",color="blue",alpha=0.7)
pyplot.hist(diff_function_AUC,bins,density=1,label="Different function",color='grey',alpha=0.7)

pyplot.xlabel("AUC value in AD",fontsize=12)
pyplot.ylabel("Normalized Frequency",fontsize=12)
pyplot.legend(loc="upper left")
pyplot.tight_layout()
pyplot.savefig("CNN_AD_1_group_auc_histogram.png",dpi=300)
pyplot.show()