#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 16:58:03 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""


import os, sys

#print(os.getcwd())

################## get the CNN_score top pose



class pose:
    def __init__(Self,CHEM_ID,CNN_score, CNN_affinity, label):
        
        Self.CHEM_ID=CHEM_ID
        
        #Self.affinity=affinity
        
        Self.CNN_score=CNN_score
        
        Self.CNN_affinity=CNN_affinity
        
        Self.label=label


POSE_list=[]
COMPOUND_pose_list=[]


sys.argv.extend(["aa2ar"])
## get the information of every pose
import glob

file=[fn for fn in sorted(glob.glob("*receptor*out"))]

for f in file:
    
    if f.split("_")[0]==sys.argv[1]:  #aa2ar is the true active, labeled as 1
        label=1
    
    else:
        
        label=0           # others are actives used as decoys, labeled as 0
    
    
    FILE=open(f,"r").readlines()
    
    COMPOUND_pose=0
    for index in range(29, len(FILE)-8):
    
        line=FILE[index]
        
        
    
        if "##" in line:
    
    
            CHEM_ID=line.split()[1]
        
            #affinity=abs(float(FILE[index+2].split()[1]))
            
            CNN_score=abs(float(FILE[index-5].split()[1]))
        
            CNN_affinity=abs(float(FILE[index-4].split()[1]))
        
        
        
            p=pose(CHEM_ID,CNN_score,CNN_affinity,label)
        
            POSE_list.append(p)
            
            COMPOUND_pose+=1
        
    COMPOUND_pose_list.append(COMPOUND_pose)
            
            


##choose Top vina pose

y_true=[]

y_CNN_score=[]


y_CNN_affinity=[]




CHEM_ID_list=[]



CHEM_ID_list.append(POSE_list[0].CHEM_ID)

y_CNN_score.append(POSE_list[0].CNN_score)
y_CNN_affinity.append(POSE_list[0].CNN_affinity)
y_true.append(POSE_list[0].label)
 
for element in POSE_list[1:]:
       
    if element.CHEM_ID != CHEM_ID_list[-1]:
        
        y_CNN_score.append(element.CNN_score)
        
       
        y_CNN_affinity.append(element.CNN_affinity)
        
        y_true.append(element.label)
        






    
    

import numpy as np

import matplotlib.pyplot as plt

#plt.switch_backend("agg")

from sklearn.metrics import roc_curve, auc

fpr=dict()
tpr=dict()
roc_auc=dict()




fpr["CNN_score"],tpr["CNN_score"],_=roc_curve(y_true,y_CNN_score)

fpr["CNN_affinity"],tpr["CNN_affinity"],_=roc_curve(y_true,y_CNN_affinity)



roc_auc["CNN_affinity"]=auc(fpr["CNN_affinity"],tpr["CNN_affinity"])


roc_auc["CNN_score"]=auc(fpr["CNN_score"],tpr["CNN_score"])



actives_num=y_true.count(1)

decoys_num=y_true.count(0)


y_vina_true=[]
y_vina_affinity=[]

# get the minimized affinity from vina sdf result


vina_compound_list=[]



actives_sdf=open(sys.argv[1]+"_actives_xdocked_top.sdf","r").readlines()

vina_compound=0
for i in range(len(actives_sdf)):
    
    if "minimizedAffinity" in actives_sdf[i]:
        
        #line_index=actives_sdf.index(line)
        
        
        
        y_vina_affinity.append(abs(float(actives_sdf[i+1])))
        
        y_vina_true.append(1)
        
        vina_compound+=1
        

vina_compound_list.append(vina_compound) 
      
decoys_sdf=[fn for fn in sorted(glob.glob("*xdocked*top*sdf")) if not fn.startswith(sys.argv[1])] 


for sdf in decoys_sdf:
    
    vina_compound=0
    
    f=open(sdf,"r").readlines()
    
    for i in range(len(f)):
        
        
        if "minimizedAffinity" in f[i]:
            
        
            
            y_vina_affinity.append(abs(float(f[i+1])))
            y_vina_true.append(0)
            
            vina_compound+=1
    vina_compound_list.append(vina_compound)
            
fpr["Vina"], tpr["Vina"],_=roc_curve(y_vina_true,y_vina_affinity)   

roc_auc["Vina"]=auc(fpr["Vina"],tpr["Vina"]) 

  


fig=plt.figure()

ax=fig.add_subplot(111)

ax.plot(fpr["Vina"],tpr["Vina"],color="blue",label="Vina: "+str("%.2f" % roc_auc["Vina"]),linewidth=2)

ax.plot(fpr["CNN_affinity"],tpr["CNN_affinity"],color="red",label="CNN_affinity: "+str("%.2f" % 
        roc_auc["CNN_affinity"]))

ax.plot(fpr["CNN_score"],tpr["CNN_score"],color="green",label="CNN_score: "+str("%.2f" % 
        roc_auc["CNN_score"]))

ax.plot([0,1],[0,1],color="grey",linestyle='--',linewidth=2,label="Random: 0.50")

ax.set_title(sys.argv[1]+" ({a}/{d}) enrichment".format(a=actives_num,d=decoys_num))

ax.set_xlabel("FPR")

ax.set_ylabel("TPR")

ax.set_ylim((0,1))

ax.set_xlim((0,1))

plt.legend(loc="lower right")

fig.tight_layout()

#plt.show()

fig.savefig(sys.argv[1]+"_top_pose_CNN_vina_AA.enrichment.png")




    
    


            


         
              




























