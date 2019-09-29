#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:51:09 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# histogram for the prediction score
import os 

print(os.getcwd())

import glob

files=sorted(glob.glob("*finaltest"))

actives_scores=[]
decoys_scores=[]

for file in files:
    content=open(file).readlines()
    
    for line in content[0:-1]:
        
        if line.split()[0]=="1.0":
            actives_scores.append(float(line.split()[1]))
        if line.split()[0]=="0.0":
            decoys_scores.append(float(line.split()[1]))
"""           
import seaborn as sns

sns.distplot(actives_scores,color="red",label="actives")

sns.distplot(decoys_scores,color="grey",label="decoys")

sns.plt.legend()
"""

import statistics 

actives_mean=statistics.mean(actives_scores)
actives_stdev=statistics.stdev(actives_scores)

decoys_mean=statistics.mean(decoys_scores)
decoys_stdev=statistics.stdev(decoys_scores)

from matplotlib import pyplot
import numpy
fig=pyplot.figure()
bins=numpy.linspace(0,1,20)

pyplot.hist(actives_scores,bins,alpha=0.9,color="red",label="actives")
pyplot.hist(decoys_scores,bins,alpha=0.9,color="blue",label="decoys")
pyplot.xlabel("Predicted score",fontsize=15)
pyplot.ylabel("Count",fontsize=15)
pyplot.legend(loc="upper right")
pyplot.tight_layout()
pyplot.savefig("Actives_Decoys_score_histogram.png",dpi=2000)
pyplot.show()      

