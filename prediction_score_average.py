#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:24:32 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# calculate the average prediction of actives and decoys in each targets 


import os 

print(os.getcwd())

import glob

files=sorted(glob.glob("*finaltest"))

all_actives=[]
all_decoys=[]
for i in files:
    target=i.split("_")[0]
    contents=open(i).readlines()
    active_sum=[]
    decoy_sum=[]
    for line in contents:
        if line.split()[0]=="1.0":
            active_sum.append(float(line.split()[-1]))
        elif line.split()[0]=="0.0":
            decoy_sum.append(float(line.split()[-1]))
        
    print(target)
    print("actives average: {0}".format(sum(active_sum)/len(active_sum)))
    print("decoys average: {0}".format(sum(decoy_sum)/len(decoy_sum)))
    
    all_actives.append(sum(active_sum)/len(active_sum))
    all_decoys.append(sum(decoy_sum)/len(decoy_sum))
    
print("the average of all actives: {0}".format(sum(all_actives)/len(all_actives))) 
# 0.896


print("the average of all decoys: {0}".format(sum(all_decoys)/len(all_decoys)))  
# 0.038          
                
        
        
            
        
        

