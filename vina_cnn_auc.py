#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:08:39 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# auc from vina and CNN
import os

print(os.getcwd())

file=open("102_dude_auc.txt","r").readlines()

target=[]

vina_auc=[]

CNN_score=[]

CNN_affinity=[]

for line in file:
    
    if "Vina" in line:
        vina_auc.append(float(line[5:9]))
        CNN_affinity.append(float(line[23:27]))
        CNN_score.append(float(line[38:]))
    else:
        target.append(line.split()[0])

import matplotlib.pyplot as plt

fig=plt.figure()


"""
ax.plot(target,vina_auc,color="blue",label="Vina",linewidth=2)
ax.plot(target,CNN_affinity,color="red",label="CNN_affinity",linewidth=2)
ax.plot(target,CNN_score,color="green",label="CNN_score",linewidth=2)
"""

import seaborn as sns

import pandas as pd
auc=[]
auc=vina_auc+CNN_affinity+CNN_score
group_vina=["vina" for i in range(84)]
group_CNN_affinity=["CNN_affinity" for i in range(84)]
group_CNN_score=["CNN_score" for i in range(84)]
groups=[]
groups=group_vina + group_CNN_affinity+ group_CNN_score


d={"auc":auc,"enrichment":groups}

df=pd.DataFrame(data=d)

print(df)

ax=sns.boxplot(x="enrichment",y="auc",data=df)
ax=sns.swarmplot(x="enrichment",y="auc",data=df,color=".25")

plt.savefig("84_DUDE_targets_enrichment")



#fig.savefig("94_AA_targets_enrichment.png")
import xlsxwriter

workbook=xlsxwriter.Workbook("84_DUDE_target_revised.xlsx")

worksheet=workbook.add_worksheet()


col=0

for i in target:
    worksheet.write(0,col,i)
    col+=1


col=0

for i in vina_auc:
    worksheet.write(1,col,i)
    col+=1
col=0
for i in CNN_affinity:
    worksheet.write(2,col,i)
    col+=1

col=0

for i in CNN_score:
    worksheet.write(3,col,i)
    col+=1

workbook.close()

vina_max=[]
CNN_affinity_better=[]
CNN_score_better=[]

CNN_better=[]
for i in range(84):
    
    if vina_auc[i] > CNN_affinity[i] and vina_auc[i]> CNN_score[i] and vina_auc[i]>0.8:
        vina_max.append(target[i])
    
    if CNN_affinity[i] > vina_auc[i] and CNN_affinity[i]>0.8:
        CNN_affinity_better.append(target[i])
    
    if CNN_score[i] > vina_auc[i] and CNN_score[i] > 0.8:
        CNN_score_better.append(target[i])
        
    if CNN_affinity[i]> vina_auc[i] and CNN_score[i] > vina_auc[i] and CNN_affinity[i] > 0.8 and CNN_score[i]>0.8:
        
        CNN_better.append(target[i])
        
    
from scipy import stats

stats.ttest_rel(vina_auc,CNN_score)
stats.ttest_rel(vina_auc,CNN_affinity)
stats.ttest_rel(CNN_score,CNN_affinity)

stats.wilcoxon(vina_auc,CNN_score)
stats.wilcoxon(vina_auc,CNN_affinity)
stats.wilcoxon(CNN_score,CNN_affinity)


