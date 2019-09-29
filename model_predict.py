#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:00:36 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# compare two models
import sys, os
import glob, matplotlib, xlsxwriter
os.chdir("/Users/eric/Desktop/CNN_manuscript/Per_target_AUC/receptor_model_prediction/")

print(os.getcwd())
workbook=xlsxwriter.Workbook("Prediction.xlsx")
worksheet=workbook.add_worksheet()

col=1
worksheet.write(1,0,"No Receptor")
# change dir to receptor dir and read the Receptor Per target auc

Receptor_files=sorted(glob.glob("*predict"))

for file in Receptor_files:
    target=file.split("_")[0]
    lines=open(file).readlines()
    auc=round(float(lines[-1].split()[-1]),3)
    print(target,auc)
    worksheet.write(0,col,target.upper())
    worksheet.write(1,col,auc)
    col=col+1

workbook.close()
