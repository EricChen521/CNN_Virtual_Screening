#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:20:15 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os

print(os.getcwd())


targets=next(os.walk("."))[1]

for target in targets:
    os.chdir(target)
    train_actives=open("train_actives.smi","w+")
    train_decoys=open("train_decoys.smi","w+")
    
    train=open("train.smi").readlines()
    for line in train:
        if line.split()[1]=="1":
            train_actives.write(line.split()[0]+"\n")
        if line.split()[1]=="0":
            train_decoys.write(line.split()[0]+"\n")
            
    test_actives=open("test_actives.smi","w+")
    test_decoys=open("test_decoys.smi","w+")
    
    test=open("test.smi").readlines()
    
    for line in test:
        if line.split()[1]=="1":
            test_actives.write(line.split()[0]+"\n")
        if line.split()[1]=="0":
            test_decoys.write(line.split()[0]+"\n")
    
    os.chdir("../")  
    
    train_actives.close()
    train_decoys.close()
    test_actives.close()
    test_decoys.close()
    
