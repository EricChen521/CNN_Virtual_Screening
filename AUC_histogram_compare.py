#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:32:38 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os

print(os.getcwd())

import glob

os.chdir("/Users/eric/Desktop/CNN_manuscript/Cross_target_prediction/CNN")
Default_files=glob.glob("*predict.auc")
default_auc=[]

for file in Default_files:
    contents=open(file).readlines()
    for line in contents:
        auc=float(line.split(" ")[2])
        default_auc.append(auc)
        

os.chdir("/Users/eric/Desktop/CNN_manuscript/Cross_target_prediction/CNN_AA")

AD_files=glob.glob("*.auc")
AD_auc=[]
for file in AD_files:
    contents=open(file).readlines()
    for line in contents:
        auc=float(line.split(" ")[2])
        AD_auc.append(auc)
        
os.chdir("/Users/eric/Desktop/CNN_manuscript/Cross_target_prediction")

from matplotlib import pyplot
import numpy

fig=pyplot.figure()
bins=numpy.linspace(0,1,100)

pyplot.hist(default_auc,bins,label="default decoys",alpha=0.8)
pyplot.hist(AD_auc,bins,label="AD decoys",alpha=0.8)
pyplot.xlabel("AUC value",fontsize=15)
pyplot.ylabel("Count",fontsize=15)
pyplot.legend(loc="upper left")
pyplot.tight_layout()
pyplot.savefig("CNN_AD_auc_histogram.png",dpi=2000)
pyplot.show()