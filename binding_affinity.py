#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:53:33 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
#extract the binding affinity value
import os, math

print(os.getcwd())

file=open("/Users/eric/Desktop/PDBbind_2017_plain_text_index/general_PL.2017.txt","r").readlines()

file_affinity=open("general_PL_affinity_2017.txt","w+")

item={}

unit_change={"M":0,"mM":3,"uM":6,"nM":9,"pM":12,"fM":15}

for line in file[6:]:
    pdb=line.split()[0]
    ligand=line.split("(")[1].split(")")[0]
    unit=line.split()[3][-2:]
    
    if "=" in line.split()[3]:
        
        affinity_string=line.split()[3].split("=")[1]
    
    
        affinity_value=unit_change[unit]-math.log10(float(affinity_string.replace(unit,"")))
        
        item[pdb]=ligand +"\t"+ str(round(affinity_value,3))
        element=pdb+","+ligand+","+str(round(affinity_value,3))+"\n"
        file_affinity.write(element)

file_affinity.close()
bryce_file=open("pdb_pActivityAgg_011818.csv","r").readlines()


for line in bryce_file[1:]:
    PDB_ID=line.split(",")[0]
    ligand=line.split(",")[1]
    
    affinity=round(float(line.split(",")[2]),3)
    #print(affinity)
    
    #if PDB_ID.lower() in item:
    #and ligand.lower() in item[PDB_ID.lower()][0]:
        #print(PDB_ID,ligand,affinity,item[PDB_ID.lower()])
        
    

