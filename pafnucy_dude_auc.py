#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:41:40 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# the performace of pafnucy on DUDe
import os, glob

files=glob.glob("*csv")

targets=[]

for item in files:
    name=item.split("_")[0]
    if name not in targets:
        targets.append(name)

targets=sorted(targets)
print(targets)

targets.remove("ampc")

# calculate the auc for DUDe targets

file_auc=open("pafnucy_dude_auc.txt","w+")
file_auc.write("target"+"\t"+"AUC"+"\n")
Pafnucy_auc={}
from sklearn.metrics import roc_auc_score

for receptor in targets:
    y_true=[]
    y_score=[]
    f_actives=open(receptor+"_actives_predict.csv").readlines()
    
    for line in f_actives:
        if "CHEMBL" in line:
            score=float(line.split(",")[-1])
            y_true.append(1)
            y_score.append(score)
            
            
    f_decoys=open(receptor+"_decoys_predict.csv").readlines()
    for line in f_decoys:
        if "ZINC" in line:
            score=float(line.split(",")[-1])
            y_true.append(0)
            y_score.append(score)
    
    auc=roc_auc_score(y_true,y_score)
    Pafnucy_auc[receptor]=auc
    
    string=receptor +"\t"+ str(auc)+ "\n"
    
    file_auc.write(string)
    
file_auc.close()

import matplotlib.pyplot as plt

fig=plt.figure()

f1=open("pafuncy_Vina.txt","w+")

f_vina=open("/Users/eric/Desktop/102_DUDE/102_dude_auc.txt","r").readlines()

Vina_auc={}

for line in f_vina:
    if ":" not in line:
        name=line.split()[0]
    if "Vina" in line:
        vina_score=float(line.split()[0].split(":")[1])
        Vina_auc[name]=vina_score
        
         

auc_vina=[Vina_auc[i] for i in Vina_auc]

group_vina=["vina" for i in range(len(auc_vina))]

auc_pafnucy=[Pafnucy_auc[i] for i in Pafnucy_auc]

group_pafnucy=["pafnucy" for i in range(len(auc_pafnucy))]

AUC=[]

AUC=auc_vina + auc_pafnucy

Groups=[]
Groups=group_vina + group_pafnucy

d={"auc":AUC,"enrichment":Groups}

import pandas as pd
import seaborn as sns

df=pd.DataFrame(data=d)

ax=sns.boxplot(x="enrichment",y="auc",data=df)
ax=sns.swarmplot(x="enrichment",y="auc",data=df,color=".25")
ax.set_ylim(0,1)

plt.savefig("84_DUDE_targets_Vina_Pafnucy_enrichment.png")

        
            
    
