#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:18:45 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""


import os


file_1=open("gnina_DUDe_auc.txt","r").readlines()

file_2=open("pafnucy_DUDe_auc.txt","r").readlines()


target=[]

vina_auc=[]

gnina_auc=[]

pafnucy_auc=[]

for line in file_1:
    if "Vina" in line:
        vina_auc.append(float(line[5:9]))
        gnina_auc.append(float(line[23:27]))
    else:
        target.append(line.split()[0])

for line in file_2:
    if "." in line:
        pafnucy_auc.append(float(line.strip()))
    
import seaborn as sns

import pandas as pd

auc=[]

auc=vina_auc+gnina_auc+pafnucy_auc

group_vina=["Vina"] * len(vina_auc)

group_gnina=["Gnina"]*len(gnina_auc)

group_pafnucy=["Pafnucy"]*len(pafnucy_auc)

groups=group_vina+group_gnina+group_pafnucy

d={"AUC":auc, "Methods":groups}

df=pd.DataFrame(data=d)

import matplotlib.pyplot as plt

fig=plt.figure()

ax=sns.boxplot(x="Methods",y="AUC",data=df)
ax=sns.swarmplot(x="Methods",y="AUC",data=df,color=".25")


plt.savefig("Vina_Gnina_Pafnucy_auc_2.tiff",dpi=300)
plt.show()

Vina_mean=sum(vina_auc)/102

Gnina_mean=sum(gnina_auc)/102
Pafnucy_mean=sum(pafnucy_auc)/102


import xlsxwriter

workbook=xlsxwriter.Workbook("Vina_Gnina_Pafnucy_auc.xlsx")

worksheet=workbook.add_worksheet()

col=0

for i in target:
    
    worksheet.write(0,col,i)
    col=col+1
    
col=0

for i in vina_auc:
    worksheet.write(1,col,i)
    col+=1
    
col=0
for i in gnina_auc:
    worksheet.write(2,col,i)
    col+=1
    
col=0
for i in pafnucy_auc:
    worksheet.write(3,col,i)
    col+=1

workbook.close()










        
