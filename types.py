#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:47:34 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
#generate the types input file
import os

os.getcwd()

file=open("general_PL_affinity_2017.txt","r").readlines()

Target={}

# read the target 
for line in file[1:]:
    name=line.split(",")[0].upper()
    print(name)
    affinity=float(line.split(",")[2])
    temp={name:affinity}
    Target.update(temp)
    
#print(len(Target))

# write type file for training and testing set
    
Training=open("nogist_train.types","w+")
Testing=open("nogist_test.types","w+")

train_set=open("training_set","r").readlines()
test_set=open("testing_set","r").readlines()

count_train=0
count_test=0
for line in train_set:
    i=line.split()[0]
    if i in Target:
        
        record="{0} {1} {2}".format(Target[i],str(i)+"_nogist.48.16.binmap.gz",str(i)+"_nogist_0.48.19.binmap.gz")+"\n"
        Training.write(record)
        count_train+=1
    
for line in test_set:
    
    i=line.split()[0]
    if i in Target:
        
        record="{0} {1} {2}".format(Target[i],str(i)+"_nogist.48.16.binmap.gz",str(i)+"_nogist_0.48.19.binmap.gz")+"\n"
        Testing.write(record)
        count_test+=1
    
Training.close()
Testing.close()    
    




    
    
