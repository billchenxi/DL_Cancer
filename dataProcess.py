# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from os import listdir
import gzip
import os.path

# Data process
folders = listdir("./Desktop/CancerDLPaper/Cancer")

dest_folder = "./Desktop/CancerDLPaper/Cancer_txt/"

# Unzip all the cancer files
for i in folders:
    source_folder = "./Desktop/CancerDLPaper/Cancer/" + i
    for gzfile in listdir(source_folder):
        if gzfile.endswith(".gz"):
            base = os.path.splitext(gzfile)[0]
            dest_name = dest_folder + base + ".txt"
            print(dest_name)
            gzname = source_folder+ "/"+gzfile
            with gzip.open(gzname, 'rb') as infile:
                with open(dest_name, 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)

# Unzip all the normal files
folders = listdir("./Desktop/CancerDLPaper/Normal")

dest_folder = "./Desktop/CancerDLPaper/Normal_txt/"

for i in folders:
    source_folder = "./Desktop/CancerDLPaper/Normal/" + i
    for gzfile in listdir(source_folder):
        if gzfile.endswith(".gz"):
            base = os.path.splitext(gzfile)[0]
            dest_name = dest_folder + base + ".txt"
            print(dest_name)
            gzname = source_folder+ "/"+gzfile
            with gzip.open(gzname, 'rb') as infile:
                with open(dest_name, 'wb') as outfile:
                    for line in infile:
                        outfile.write(line)

# Since each file has different Ensembl IDs, so collect them all to find the commom ones
import pandas as pd
## For cancer files
folder = "./Desktop/CancerDLPaper/Cancer_txt/"
fileList = listdir(folder)
names = list()
for i in fileList:
    fileName = folder + i
    print(fileName)
    name = list(pd.read_csv(fileName, delimiter='\t', header=None)[0])
    names.append(name)
## For normal files
folder = "./Desktop/CancerDLPaper/Normal_txt/"
fileList = listdir(folder)
for i in fileList:
    fileName = folder + i
    print(fileName)
    name = list(pd.read_csv(fileName, delimiter='\t', header=None)[0])
    names.append(name)


                        
# Include all the data in one file(cancer)                     
import numpy as np
folder = "./Desktop/CancerDLPaper/Cancer_txt/"
fileList = listdir(folder)
first = fileList.pop(0)
cancerNPArray = np.genfromtxt((folder+first), delimiter='\t')[:,1]
for i in fileList:
    fileName = folder + i
    data = np.genfromtxt(fileName, delimiter='\t')[:,1]
    print(data.shape)
    cancerNPArray= np.c_[cancerNPArray, data]

# Include all the data in one file(normal)
folder = "./Normal_txt/"
fileList = listdir(folder)
first = fileList.pop(0)
NormalNPArray = np.genfromtxt((folder+first), delimiter='\t')[:,1]
for i in fileList:
    fileName = folder + i
    data = np.genfromtxt(fileName, delimiter='\t')[:,1]
    print(fileName)
    np.concatenate((NormalNPArray, data))