#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:03:21 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os, glob

print(os.getcwd())

files=glob.glob("*out")

import matplotlib.pyplot as plt


file=open(files[2]).readlines()

train_RMSD=[]
test_RMSD=[]

x=[i*40 for i in range(1,170)]

for line in file:
    test=float(line.split()[1])
    train=float(line.split()[2])
    train_RMSD.append(train)
    test_RMSD.append(test)
    

plt.plot(x,train_RMSD,"r",label="Train_RMSD")
plt.plot(x,test_RMSD,'g',label="Test_RMSD")

plt.legend()
plt.title("ligand")
plt.xlabel("Iteractions")
plt.ylabel("RMSD")
plt.savefig("ligand.png")
plt.show()

