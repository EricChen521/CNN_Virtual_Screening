#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:32:30 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 
import urllib.request
os.chdir("/Users/eric/Desktop/DUDe_ligand_center")
file=open("dude_pdb_id","r").readlines()

pdb_id=[]
targets=[]
for line in file:
    name=line.split()[0]
    os.mkdir(name)
    ID=line.split()[-1]
    pdb_id.append(ID)
    targets.append(name)
    
# download the pdb file and put into the right dic
i=0  
for item in pdb_id:
    path="/Users/eric/Desktop/DUDe_ligand_center/"+targets[i]
    
    os.chdir(path)
    link="http://files.rcsb.org/download/"+item+".pdb"
    urllib.request.urlretrieve(link,item+".pdb")
    os.chdir("/Users/eric/Desktop/DUDe_ligand_center/")
    i=i+1


    

