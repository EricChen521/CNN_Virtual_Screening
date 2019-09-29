#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:54:04 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os

print(os.getcwd())

f=open("pafnucy_DUDe_auc.txt","w+")

import glob

from sklearn.metrics import roc_curve, auc

# get the DUDe targte name

files=sorted(glob.glob("*prediction.csv"))
targets=sorted(list(set(i.split("_")[0] for i in files)))

for t in targets:
    
    y_scores=[]
    y_true=[]
    
    #target_name=t.split("_")[0]
    
    # read the actives prediction scores
    
    a_lines=open(t+"_actives_prediction.csv","r").readlines()
    y_actives_score=[]
    compound_ID=[]
    
    
    compound_start=a_lines[1].split("_")[0]
    score_start=round(float(a_lines[1].split(",")[-1]),3)
    compound_ID.append(compound_start)
    y_actives_score.append(score_start)
    for i in a_lines[2:]:
        ID=i.split("_")[0]
        score=round(float(i.split(",")[-1]),3)
        
        
        if ID==compound_ID[-1] and score > y_actives_score[-1]:
            y_actives_score[-1]=score
            
        if ID != compound_ID[-1]:
            compound_ID.append(ID)
            y_actives_score.append(score)
    
        
    
        
    y_true=[1]*len(y_actives_score)
    y_scores=y_actives_score
    
    d_lines=open(t+"_decoys_prediction.csv","r").readlines()
    y_decoys_score=[]
    compound_ID=[]
    
    
    compound_start=d_lines[1].split("_")[0]
    score_start=round(float(d_lines[1].split(",")[-1]),3)
    compound_ID.append(compound_start)
    y_decoys_score.append(score_start)
    
    for i in d_lines[2:]:
        
        if "name" not in i:
            
            ID=i.split("_")[0]
            score=round(float(i.split(",")[-1]),3)
        
        
            if ID==compound_ID[-1] and score > y_decoys_score[-1]:
                y_decoys_score[-1]=score
            
            if ID != compound_ID[-1]:
                compound_ID.append(ID)
                y_decoys_score.append(score)
            
        
    y_true=y_true+[0]*len(y_decoys_score)
    y_scores=y_scores+y_decoys_score
    
    fpr=dict()
    tpr=dict()
    roc_auc=dict()

    fpr["pafnucy"],tpr["pafnucy"],_=roc_curve(y_true,y_scores)
    roc_auc["pafnucy"]=auc(fpr["pafnucy"],tpr["pafnucy"])
    
    f.write(t+"\n")
    f.write("{}".format(round(float(roc_auc["pafnucy"]),3))+"\n")

f.close()



 
           
       
        
        
    