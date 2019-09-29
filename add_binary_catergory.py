#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:08:24 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
# add binart catagory for compound
import os
import h5py
print(os.getcwd())

import glob

decoys_list=glob.glob("ZINC*hdf")

actives_list=glob.glob("CHEMBL*hdf")

for item in actives_list:
    with h5py.File(item,"r+") as f:
        
        f.attrs['affinity']=1
        print(f.attrs["affinity"])

for item in decoys_list:
    with h5py.File(item,"r+") as f:
        f.attrs["affinity"]=0
        print(f.attrs["affinity"])
        
        
dataset_name="training"
ids = {}
affinity = {}
coords = {}
features = {}
for dictionary in [ids, affinity, coords, features]:
    
    dictionary[dataset_name] = []

with h5py.File("aa2ar.hdf","r") as f:
    i=0
    for pdb_id in f:
        print(pdb_id)
        dataset=f[pdb_id]
        coords[dataset_name].append(dataset[:,:3])
        affinity[dataset_name].append(dataset.attrs['affinity'])
        
        i=i+1
        break
        
print(coords["training"]) 

type(dataset) 
    
