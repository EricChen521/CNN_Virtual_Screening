#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:31:06 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# three models' reaction to pose chnange 
import os

f_vina=open("actives_final_docked_vina.sdf","r").readlines()

f_gnina=open("aa2ar_actives_dude_gnina.out","r").readlines()

f_pafnucy=open("aa2ar_actives_allpose_pafnucy.txt","r").readlines()

Pose_vina={}
Pose_gnina={}
Pose_pafnucy={}

def duplicates_vina(lst,item):
    return [i for i, x in enumerate(lst) if "Name = "+item in x]


for line in f_vina:
    if "Name" in line:
        compound=line.split()[-1]
        
        if compound not in Pose_vina:
            index_list=duplicates_vina(f_vina,compound)
            
            score=[round(float(f_vina[index+ 8]),3) for index in index_list]
            Pose_vina[compound]=score
  

          
def duplicates_gnina(lst,item):
    return [i for i, x in enumerate(lst) if item in x]

for line in f_gnina:
    if "CHEMBL" in line:
        compound=line.split()[1]
        if compound not in Pose_gnina:   
            index_list=duplicates_gnina(f_gnina,compound)
            affinity=[round(float(f_gnina[index -4].split()[-1]),3) for index in index_list]
            Pose_gnina[compound]=affinity
   
for line in f_pafnucy:
    if "CHEMBL" in line:
        compound=line.split(",")[0].split("_")[0]
        if compound not in Pose_pafnucy:
            index_list=duplicates_gnina(f_pafnucy,compound)
            affinity=[round(float(f_pafnucy[index].split(",")[-1]),3) for index in index_list]
            Pose_pafnucy[compound]=affinity

import statistics 
   
def avg_std(dic):
    values=[]
    for i in dic:
        avg=statistics.mean(dic[i])
        std=statistics.stdev(dic[i])
        values.append(abs(std/avg))
        
    return values

Vina_avg_std=avg_std(Pose_vina)
Gnina_avg_std=avg_std(Pose_gnina)
Pafnucy_avg_std=avg_std(Pose_pafnucy)

group_vina=["Vina" for i in range(len(Vina_avg_std))]
group_gnina=["Gnina_affinity" for i in range(len(Gnina_avg_std))]
group_pafnucy=["Pafnucy" for i in range(len(Pafnucy_avg_std))]

AVG_STD=[]
Group=[]

AVG_STD=Vina_avg_std+Gnina_avg_std+Pafnucy_avg_std

Group=group_vina+group_gnina+group_pafnucy

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig=plt.figure()

d={"averaged_stdev":AVG_STD,"Method":Group}
df=pd.DataFrame(data=d)

ax=sns.violinplot(x="Method",y="averaged_stdev",data=df)

plt.savefig("Vina_gnina_pafnucy_pose_sensitive.png")
