#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:05:20 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 

print(os.getcwd())

import glob

files=sorted(glob.glob("*finaltest"))

import xlsxwriter

workbook=xlsxwriter.Workbook("Few_ligand_AUC.xlsx")

worksheet=workbook.add_worksheet()

col=0
i=0

for file in files:
    target=file.split("_")[0]
    lines=open(file).readlines()
    auc=round(float(lines[-1].split()[-1]),3)
    row=i%3
    if (row==0):
        col=col+1
        worksheet.write(row,col,target.upper())
    worksheet.write(row+1,col,auc)
    
    i=i+1
    
workbook.close()
    
    
    




