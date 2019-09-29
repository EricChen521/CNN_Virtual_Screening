#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:29:23 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

# Plot the prediction scores of XIAP and Target
import os

print(os.getcwd())

import matplotlib.pyplot as plt

import glob

# read the socre files 

#files=["Target_ligand.finaltest"]

files=sorted(glob.glob("*finaltest"))

for f in files:
    
    Target=f.split("_")[0]
    data=open(f).readlines()
    Target_actives_x=[]
    Target_actives_y=[]
    Target_decoys_x=[]
    Target_decoys_y=[]
    i=1
    d=1
    for line in data[0:-1]:
        label=str(line.split()[0])
        score=float(line.split()[1])
    
        if label=="1.0":
       
            Target_actives_x.append(i)
            Target_actives_y.append(score)
            i=i+1
        
        if label=="0.0":
            Target_decoys_x.append(d)
            Target_decoys_y.append(score)
            d=d+1
    
        
    Target_actives=(Target_actives_x,Target_actives_y)
    Target_decoys=(Target_decoys_x,Target_decoys_y)

    points=(Target_actives,Target_decoys)
    groups=("actives", "decoys")
    colors=("red","blue")

    fig=plt.figure()

    ax1=fig.add_subplot(111)
    for point, color, group in zip(points,colors,groups):
        x,y=point
        ax1.scatter(x,y,alpha=1,c=color,edgecolors="none",s=15,label=group)
    
    ax1.set_xlabel("Ligand index",fontsize=15)
    ax1.set_ylabel("Predicted score",fontsize=15)
    ax1.set_xlim([0,600])
    ax1.set_xticks([0,100,200,300,400,500,600])
    #ax1.set_title("AUC=0.98")
    plt.legend(loc=(0.75,0.6))
    plt.show()
    

    fig.savefig(Target+"_test_scores.png",dpi=1200)



        
            
        



