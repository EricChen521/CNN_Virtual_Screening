#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:42:21 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os, math

print(os.getcwd())


class pose:
    def __init__(self, rmsd, smina_affinity,gnina_affinity,pafnucy_affinity):
        self.rmsd=rmsd
        self.vina_affinity=smina_affinity
        self.gnina_affinity=gnina_affinity
        self.pafnucy_affinity=pafnucy_affinity
 
# read the crystal smina and gnina affinity score

gnina_file=open("xld_gnina.out").readlines()

smina_affinity=[]
gnina_affinity=[]

for line in gnina_file:
    if "kcal" in line:
        smina_score=round(float(line.split()[1]),3)
        Kd=math.exp(1.688*smina_score) #25 C temperature transform 
        pKd=-(math.log(Kd,10))
        smina_affinity.append(pKd)

    
    if "CNNaffinity" in line:
        
        gnina_affinity.append(round(float(line.split()[1]),3))

pafnucy_file=open("xld_pafnucy_prediction.csv").readlines()

pafnucy_affinity=[]

for line in pafnucy_file[1:]:
    
    pafnucy_affinity.append(round(float(line.split(",")[-1]),3))
    
pose_file=open("xld_pose_reference.csv").readlines()

rmsd=[]
for line in pose_file[1:]:
    rmsd.append(float(line.split(",")[5]))
    
#add the crysal pose rmsd=0
    
rmsd.append(0)

import operator
xld_poses=[]
for i in range(101):
    xld_poses.append(pose(rmsd[i],smina_affinity[i],gnina_affinity[i],pafnucy_affinity[i]))

#sort pose by rmsd key
    
sorted_xld_pose=sorted(xld_poses,key=operator.attrgetter("rmsd")) 

"""
for i in sorted_xld_pose:
    print(i.rmsd)
""" 
rmsd=[i.rmsd for i in sorted_xld_pose]
smina=[i.vina_affinity for i in sorted_xld_pose]
gnina=[i.gnina_affinity for i in sorted_xld_pose]
pafnucy=[i.pafnucy_affinity for i in sorted_xld_pose]

SMINA=(rmsd,smina)
GNINA=(rmsd,gnina)
PAFNUCY=(rmsd,pafnucy)
points=(SMINA,GNINA,PAFNUCY)
groups=("Vina","Gnina","Pafnucy")

colors=("blue","orange","green")

import matplotlib.pyplot as plt

fig=plt.figure()

ax1=fig.add_subplot(111)

for point, color, group in zip(points,colors,groups):
    x,y=point
    ax1.scatter(x,y,alpha=1,c=color,edgecolors="none",s=15,label=group)
    
ax1.set_xlabel("RMSD to Xray, Å", fontsize=12)

ax1.set_ylabel("-LogKi", fontsize=12)

ax1.set_ylim(0,14)

#ax1.set_title("xld")

plt.legend(loc="upper right")

plt.show()

fig.savefig("xld_pose_sensitivity.png",dpi=1200)

   
    




        
        
    
