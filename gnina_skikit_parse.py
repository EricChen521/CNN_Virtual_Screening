#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:17:02 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
#parsing the gnina output file
import os
import sys

print(os.getcwd())

#os.chdir("/Users/eric/Desktop/102_AA_gnina/abl1")

#file=open(sys.argv[1]+"_receptor_gnina.out","r").readlines()

#sys.argv.extend(['abl1'])
#sys.argv.remove("-a")
#print(sys.argv[1])

#print(sys.argv)
# receptor auc

y_true=[]
y_CNN_scores=[]

y_CNN_affinity=[]




file=open(sys.argv[1]+"_receptor_gnina.out","r").readlines()
key_info=[]

for index in range(29,len(file)-8):
    line=file[index]
    if "##" in line:
        #print(line)
        y_true.append(1)
        
        CNN_score=file[index+3].split()[-1]
        
        CNN_affinity=file[index+4].split()[-1]
        
        y_CNN_scores.append(float(CNN_score))
        y_CNN_affinity.append(float(CNN_affinity))
        

import glob

decoys_file=[fn for fn in glob.glob("*receptor*out") if not fn.startswith(sys.argv[1])]

for file in decoys_file:
    
    
    file_decoys=open(file,"r").readlines()
    #print(file)

    for index in range(29,len(file_decoys)-8):
        line=file_decoys[index]
        if "CHEMBL" in line:
            #print(line)
            y_true.append(0)
        
            CNN_score=file_decoys[index+3].split()[-1]
        
            CNN_affinity=file_decoys[index+4].split()[-1]
            y_CNN_scores.append(float(CNN_score))
            y_CNN_affinity.append(float(CNN_affinity))


import numpy as np

import matplotlib.pyplot as plt

plt.switch_backend("agg")

from sklearn.metrics import roc_curve, auc

fpr=dict()
tpr=dict()
roc_auc=dict()


fpr["CNN_score"], tpr["CNN_score"],_ =roc_curve(y_true,y_CNN_scores)

roc_auc["CNN_score"]=auc(fpr["CNN_score"],tpr["CNN_score"])

fpr["CNN_affinity"],tpr["CNN_affinity"],_=roc_curve(y_true,y_CNN_affinity)

roc_auc["CNN_affinity"]=auc(fpr["CNN_affinity"],tpr["CNN_affinity"])

fig=plt.figure()

ax=fig.add_subplot(121)

ax.plot(fpr["CNN_score"],tpr["CNN_score"],color="blue",label="CNN_score: "+str("%.2f" % 
        roc_auc["CNN_score"]),linewidth=2)

ax.plot(fpr["CNN_affinity"],tpr["CNN_affinity"],color="red",label="CNN_affinity: "+str("%.2f" % 
        roc_auc["CNN_affinity"]))

ax.plot([0,1],[0,1],color="grey",linestyle='--',linewidth=2,label="Random: 0.50")

ax.set_title(sys.argv[1]+" receptor Enrichment")

ax.set_xlabel("FPR")

ax.set_ylabel("TPR")

ax.set_ylim((0,1))

ax.set_xlim((0,1))

plt.legend(loc="lower right")



# dummy auc

y_true=[]
y_CNN_scores=[]

y_CNN_affinity=[]




file=open(sys.argv[1]+"_dummy_gnina.out","r").readlines()
key_info=[]

for index in range(29,len(file)-8):
    line=file[index]
    if "##" in line:
        #print(line)
        y_true.append(1)
        
        CNN_score=file[index+3].split()[-1]
        
        CNN_affinity=file[index+4].split()[-1]
        
        y_CNN_scores.append(float(CNN_score))
        y_CNN_affinity.append(float(CNN_affinity))
        



decoys_file=[fn for fn in glob.glob("*dummy*out") if not fn.startswith(sys.argv[1])]

for file in decoys_file:
    
    
    file_decoys=open(file,"r").readlines()
    #print(file)

    for index in range(29,len(file_decoys)-8):
        line=file_decoys[index]
        if "CHEMBL" in line:
            #print(line)
            y_true.append(0)
        
            CNN_score=file_decoys[index+3].split()[-1]
        
            CNN_affinity=file_decoys[index+4].split()[-1]
            y_CNN_scores.append(float(CNN_score))
            y_CNN_affinity.append(float(CNN_affinity))




fpr=dict()
tpr=dict()
roc_auc=dict()


fpr["CNN_score"], tpr["CNN_score"],_ =roc_curve(y_true,y_CNN_scores)

roc_auc["CNN_score"]=auc(fpr["CNN_score"],tpr["CNN_score"])

fpr["CNN_affinity"],tpr["CNN_affinity"],_=roc_curve(y_true,y_CNN_affinity)

roc_auc["CNN_affinity"]=auc(fpr["CNN_affinity"],tpr["CNN_affinity"])



ax_2=fig.add_subplot(122)

ax_2.plot(fpr["CNN_score"],tpr["CNN_score"],color="blue",label="CNN_score: "+str("%.2f" % 
        roc_auc["CNN_score"]),linewidth=2)

ax_2.plot(fpr["CNN_affinity"],tpr["CNN_affinity"],color="red",label="CNN_affinity: "+str("%.2f" % 
        roc_auc["CNN_affinity"]))

ax_2.plot([0,1],[0,1],color="grey",linestyle='--',linewidth=2,label="Random: 0.50")

ax_2.set_title(sys.argv[1]+" dummy Enrichment")

ax_2.set_xlabel("FPR")

ax_2.set_ylabel("TPR")

ax_2.set_ylim((0,1))

ax_2.set_xlim((0,1))





plt.legend(loc="lower right")

fig.tight_layout()

plt.show()

fig.savefig(sys.argv[1]+"_enrichment_curve.png")







            
            






