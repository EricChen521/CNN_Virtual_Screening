#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:56:00 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# compare the auc 
import sys, os
import glob, matplotlib, xlsxwriter

print(os.getcwd())

#creat a workbook 
workbook=xlsxwriter.Workbook("Per_target_AUC.xlsx")
worksheet=workbook.add_worksheet()

col=1
worksheet.write(1,0,"Receptor")
worksheet.write(2,0,"Ligand")
# change dir to receptor dir and read the Receptor Per target auc

os.chdir("/Users/eric/Desktop/CNN_manuscript/Per_target_AUC/receptor/")
Receptor_files=sorted(glob.glob("*receptor*"))

for file in Receptor_files:
    target=file.split("_")[0]
    lines=open(file).readlines()
    auc=round(float(lines[-1].split()[-1]),3)
    print(target,auc)
    worksheet.write(0,col,target.upper())
    worksheet.write(1,col,auc)
    col=col+1


os.chdir("/Users/eric/Desktop/CNN_manuscript/Per_target_AUC/ligand")
Ligand_files=sorted(glob.glob("*ligand*"))
col=1
for file in Ligand_files:
    
    lines=open(file).readlines()
    auc=round(float(lines[-1].split()[-1]),3)
   
    worksheet.write(2,col,auc)
    col=col+1



workbook.close()
    



