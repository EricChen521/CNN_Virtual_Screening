#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:31:32 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
#find the duplicate compound
import os 

file=open("duplicates.txt").readlines()

target=[""]


overlap=[]
n=0

for line in file:
    
    sdf=line.split()[0]
    
    if sdf != target[-1]:
        target.append(sdf)
        print(sdf)
        print(n)
        overlap.append(n)
        n=1
    else:
        n=n+1

print(max(overlap))
