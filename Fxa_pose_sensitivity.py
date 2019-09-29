#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:57:03 2019

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

# test the sensity to pose
import os

print(os.getcwd())

rmsd_file=open("xlc.rmsd").readlines()

RMSD=[]

for line in rmsd_file:
    if "RMSD" in line:
        RMSD.append(float(line.split()[3][0:3]))
 
    
Gnina_affinity=[]

gnina_file=open("xlc_gnina.out").readlines()

for line in gnina_file:
    if "CNNaffinity" in line:
        Gnina_affinity.append(round(float(line.split()[-1]),3))

pafnucy_affinity=[ 0 for i in range(98)]

pafnucy_file=open("xlc_pafnucy_prediction.csv").readlines()[1:]

for line in pafnucy_file:
    ID=line.split(",")[0]
    pose_index=int(ID.split("_")[-1])
    pafnucy_affinity[pose_index]=round(float(line.split(",")[-1]),3)
 
Vina_affinity=[]
import math
Vina_file=open("xlc_docked.sdf").readlines()
n=0


for i in range(84,len(Vina_file),87):
    line=Vina_file[i]
    
    affinity=round(float(line.rstrip()),3)
    Kd=math.exp(1.688*affinity) #25 C temperature transform 
    pKd=-(math.log(Kd,10))
    Vina_affinity.append(pKd)

     
class pose:
    def __init__(self, rmsd, vina_affinity,gnina_affinity,pafnucy_affinity):
        self.rmsd=rmsd
        self.vina_affinity=vina_affinity
        self.gnina_affinity=gnina_affinity
        self.pafnucy_affinity=pafnucy_affinity
 
XLC_pose=[]       
for i in range(98):
    XLC_pose.append(pose(RMSD[i],Vina_affinity[i],Gnina_affinity[i],pafnucy_affinity[i]))

import operator

sorted_XLC_pose=sorted(XLC_pose,key=operator.attrgetter("rmsd"))   
    
print([i.rmsd for i in sorted_XLC_pose])

rmsd=[i.rmsd for i in sorted_XLC_pose]
vina=[i.vina_affinity for i in sorted_XLC_pose]
gnina=[i.gnina_affinity for i in sorted_XLC_pose]
pafnucy=[i.pafnucy_affinity for i in sorted_XLC_pose]

VINA=(rmsd,vina)
GNINA=(rmsd,gnina)
PAFNUCY=(rmsd,pafnucy)
points=(VINA,GNINA,PAFNUCY)
groups=("Vina","Gnina","Pafnucy")

colors=("blue","orange","green")

import matplotlib.pyplot as plt

fig=plt.figure()

ax1=fig.add_subplot(111)

for point, color, group in zip(points,colors,groups):
    x,y=point
    ax1.scatter(x,y,alpha=1,c=color,edgecolors="none",s=15,label=group)
    
ax1.set_xlabel("RMSD to Xray, Å", fontsize=15)

ax1.set_ylabel("Predicted pLogKd", fontsize=15)

plt.legend()

plt.show()

fig.savefig("Fxa_pose_sensitivity.png",dpi=1200)


