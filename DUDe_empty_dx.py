#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:19:10 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""
#creat a empty grid for the target"
import os
from gridData import Grid
import numpy as np
os.getcwd()

g_1=Grid("xiap_empty.dx")


g_O=Grid("gist_gO.dx")

values_1=g_1.grid
edge_1=g_1.edges
print(values_1[0,0,0])
print(type(values_1))
print(values_1[0])
print(type(edge_1))
print(edge_1[0])

values_O=g_O.grid
edge_O=g_O.edges
print(values_O[0,0,0])

print(values_O[0])
print(values_1[0])

empty_gO_grid=Grid(np.zeros((48,48,48)),edges=edge_O)
empty_gO_grid.export("empty_gO.dx","DX")

empty_gO=Grid("empty_gO.dx")
empty_values=empty_gO.grid
print(empty_values[0,0,0])
empty_edges=empty_gO.edges




file=open("102_ligand_coordinate.txt","r").readlines()

for line in file:
    print(line)
    target=line.split()[0]
    x_center=line.split()[2]
    y_center=line.split()[3]
    z_center=line.split()[4]
    coordinate_list=[]

    for center in [x_center,y_center,z_center]:
        
        coordinate_list.append(np.arange(float(center)-12,float(center)+12,0.5))
        """
        for point in range(float(center)-12,float(center)+12.5,0.5):
            coordinate[i].append(point)
            """
       
    #coordinate=[np.asarray(coordinate_list[0]),np.asarray(coordinate_list[1]),np.asarray(coordinate_list[2])]
    coordinate=np.asarray(coordinate_list)
    
    empty_grid=Grid(np.zeros((48,48,48)),edges=coordinate)
    empty_grid.export(target+"_empty.dx","DX")
    


          
            
    
