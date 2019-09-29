#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:04:07 2018

@author: Eric Chen, Graduate Center, CUNY

@ Prof. Kurtzman's Lab
"""

import os 
import numpy as np
print(os.getcwd())

from multiprocessing import Pool
from scipy.spatial.distance import cdist, is_valid_dm

from rdkit.Chem.AtomPairs import Pairs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.rdMolDescriptors import GetHashedAtomPairFingerprint,GetHashedAtomPairFingerprintAsBitVect
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit import DataStructs

def readMols( file ) :
  fileName, fileExtension = os.path.splitext( file )
  mols = []
  if( fileExtension == ".smi" ) :
    f = open( file, 'r' )
    l = f.readline()
    f.close()
    if '\t' in l :
      mols = Chem.SmilesMolSupplier( file, delimiter='\t', titleLine=False )
    else :
      mols = Chem.SmilesMolSupplier( file, delimiter=' ', titleLine=False ) 
  elif( fileExtension == ".sdf" ) : 
    mols = Chem.SDMolSupplier( file )
  else: 
    raise Exception( "un-supported input file format: "+fileExtension + " . ")
  return mols

def get_fp( mols ):
    
    fps=[]
    
    for x in mols:
        if (x):
            #z=FingerprintMols.FingerprintMol( x)
            z=AllChem.GetMorganFingerprintAsBitVect( x, 2 )
            #z= FingerprintMols.FingerprintMol( x )
            fps.append(z)
    
    return fps
    

def calcDistMat( fp1, fp2, distType ) :
  
    return cdist( fp1, fp2, distType )

          
comt_actives=[ m for m in readMols("/Users/eric/Desktop/CNN_manuscript/FP_distant/comt/test_actives.smi") if m is not None]

comt_decoys=[ m for m in readMols("/Users/eric/Desktop/CNN_manuscript/FP_distant/comt/test_decoys.smi") if m is not None]

def_actives=[ m for m in readMols("/Users/eric/Desktop/CNN_manuscript/FP_distant/thb/train_actives.smi") if m is not None]

def_decoys=[ m for m in readMols("/Users/eric/Desktop/CNN_manuscript/FP_distant/thb/train_decoys.smi") if m is not None]

comt_actives_FP=get_fp(comt_actives)
comt_decoys_FP=get_fp(comt_decoys)

def_actives_FP=get_fp(def_actives)
def_decoys_FP=get_fp(def_decoys)

C_aa=calcDistMat(comt_actives_FP,comt_actives_FP,"jaccard")
C_dd=calcDistMat(comt_decoys_FP,comt_decoys_FP,"jaccard")

H_aa=calcDistMat(def_actives_FP,def_actives_FP,"jaccard")
H_dd=calcDistMat(def_decoys_FP,def_decoys_FP,"jaccard")

comt_actives_decoys_D=calcDistMat(comt_actives_FP,comt_decoys_FP,"jaccard")

def_actives_decoys_D=calcDistMat(def_actives_FP,def_decoys_FP,"jaccard")

C_H_actives_D=calcDistMat(comt_actives_FP,def_actives_FP,"jaccard")

C_H_decoys_D=calcDistMat(comt_decoys_FP,def_decoys_FP,"jaccard")

C_actives_H_decoys_D=calcDistMat(comt_actives_FP,def_decoys_FP,"jaccard")
C_decoys_H_actives_D=calcDistMat(comt_decoys_FP,def_actives_FP,"jaccard")



#x=[np.mean( np.any( comt_actives_decoys_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 50 ) ]

#print((np.any( comt_actives_decoys_D < 0.7, axis=1 )))
#print(x)
"""
comt_actives_decoys_S= np.mean( [ np.mean( np.any( comt_actives_decoys_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 20 ) ] )
def_actives_decoys_S=np.mean( [ np.mean( np.any( def_actives_decoys_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 20 ) ] )

C_H_actives_S=np.mean( [ np.mean( np.any( C_H_actives_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 20 ) ] )
C_H_decoys_S=np.mean( [ np.mean( np.any( C_H_decoys_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 20 ) ] )


C_actives_H_decoys_S=np.mean( [ np.mean( np.any( C_actives_H_decoys_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 50 ) ] )
C_decoys_H_actives_S=np.mean( [ np.mean( np.any( C_decoys_H_actives_D < t, axis=1 ) ) for t in np.linspace( 0, 1.0, 50 ) ] )



[t for t in np.linspace(0,1,50)]

print(np.any( C_actives_H_decoys_D < 0.5, axis=1 ))
"""
C_actives_decoys_mean=np.mean(comt_actives_decoys_D)
H_actives_decoys_mean=np.mean(def_actives_decoys_D)

C_H_actives_mean=np.mean(C_H_actives_D)
C_H_decoys_mean=np.mean(C_H_decoys_D)

C_actives_H_decoys_mean=np.mean(C_actives_H_decoys_D)
C_decoys_H_actives_mean=np.mean(C_decoys_H_actives_D)

C_aa_mean=np.mean(C_aa)

C_dd_mean=np.mean(C_dd)

H_aa_mean=np.mean(H_aa)
H_dd_mean=np.mean(H_dd)

print(C_H_actives_mean)
print(C_actives_H_decoys_mean)
print(C_decoys_H_actives_mean)
print(C_H_decoys_mean)
