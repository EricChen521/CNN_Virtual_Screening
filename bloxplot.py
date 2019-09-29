#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:40:09 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 

print(os.getcwd())

import xlrd

wb=xlrd.open_workbook("10trained_CNN_model.xlsx")

sheet=wb.sheet_by_index(0)

#sheet.cell_value(1,1)

Receptor_auc=[]

Ligand_auc=[]

for col in range(1,93):
    Receptor_auc.append(float(sheet.cell_value(1,col)))
    Ligand_auc.append(float(sheet.cell_value(2,col)))
    
group_receptor=["Receptor-ligand model" for i in range(92)]
group_ligand=["Ligand-only model" for i in range(92) ] 

auc=Receptor_auc + Ligand_auc
groups=group_receptor+group_ligand

import seaborn as sns
import pandas as pd

d={"AUC":auc, "Multi-targets Trained Model":groups}

df=pd.DataFrame(data=d)

import matplotlib.pyplot as plt

fig=plt.figure()

ax=sns.boxplot(x="Multi-targets Trained Model",y="AUC",data=df)
ax=sns.swarmplot(x="Multi-targets Trained Model",y="AUC",data=df,color=".25")
#plt.ylim(0.8,1)
#plt.legend()
plt.savefig("10trained_Model_compare.png",dpi=500)
plt.show()