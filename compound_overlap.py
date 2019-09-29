#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:30:19 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 

print(os.getcwd())

import glob

actives_files=sorted(glob.glob("*actives*ism"))

decoys_files=sorted(glob.glob("*decoys*ism"))

targets_actives=[]
all_actives=[]
for file in actives_files:
    
    item=open(file).readlines()
    
    name=file.split("_")[0]
    
    
    compounds=[]
    for line in item:
        compound=line.split()[-1]
        compounds.append(compound)
        all_actives.append(compound)
    
    num=len(compounds)
    
    target={"name":name,"number":num,"compounds":compounds}
        
    targets_actives.append(target)

total_compounds=0
for i in targets_actives:
    #print(i["number"])
    total_compounds=total_compounds+i["number"]
print("non-overlap actives number:")       
print(len(set(all_actives))) # 20462

print("total actives numbers:")
print(total_compounds)  # 22805

import xlsxwriter

workbook=xlsxwriter.Workbook("DUD-E_actives_overlap.xlsx")
worksheet=workbook.add_worksheet()
col=0
for i in targets_actives:
    worksheet.write(0,col,"{0},{1}".format(i["name"],i["number"]))
    worksheet.write(col,0,"{0},{1}".format(i["name"],i["number"]))
    col=col+1

 
for i in targets_actives:
    index=targets_actives.index(i)
    print(i["name"])
    other_targts=targets_actives[index+1:]
    col=index+1
    for j in other_targts:
        overlap=set(i["compounds"]) & set(j["compounds"])
        if overlap:
            #print(j["name"])
            worksheet.write(index+1,col,len(overlap))
        else:
            worksheet.write(index+1,col,0)
        col=col+1
workbook.close()           

