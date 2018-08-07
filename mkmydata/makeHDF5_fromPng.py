import os
import h5py
from PIL import Image
import numpy as np

import struct
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
NX = 276
NZ = 276
workpath = "./"
phase = 'train' #['train', 'test']
mode = 'B' #['A', 'B']
content = ['vx_split', 'vz_split']

fileNum = 0 
for root,dirs,files in os.walk(workpath + content[0]):    #遍历统计  
    for each in files:  
        if each[-4:] == '.png':  
            #print( root,dirs,each)  
            fileNum += 1  
#print(fileNum)

outfile = h5py.File(workpath + phase + mode +'.h5', 'w')  #./trainB.h5
outdata = torch.zeros((2, NX, NZ))

for count in range(1, fileNum):
    for i, iterm in enumerate(content):
        iname = workpath + iterm + "/" + mode + str(count) + ".png" # ./vz_split/B1.png
        data = Image.open(iname).convert('L').resize((NX, NZ)) # 276*276
        outdata[i] = transforms.ToTensor()(data) #np.matrix(data, dtype='float')/255.0
    #infile = Image.open(iname)
    outfile.create_dataset(mode+str(count), data=outdata, dtype=np.float64) #B1.png
outfile.close()
workpath = "./"
phase = 'train' #['train', 'test']
mode = 'A' #['A', 'B']
content = ['curl_split', 'div_split']

fileNum = 0 
for root,dirs,files in os.walk(workpath + content[0]):    #遍历统计  
    for each in files:  
        if each[-4:] == '.png':  
            #print( root,dirs,each)  
            fileNum += 1  
#print(fileNum)

outfile = h5py.File(workpath + phase + mode +'.h5', 'w')  #./trainB.h5
outdata = torch.zeros((2, NX, NZ))

for count in range(1, fileNum):
    for i, iterm in enumerate(content):
        iname = workpath + iterm + "/" + mode + str(count) + ".png" # ./vz_split/B1.png
        data = Image.open(iname).convert('L').resize((NX, NZ)) # 276*276
        outdata[i] = transforms.ToTensor()(data) #np.matrix(data, dtype='float')/255.0
    #infile = Image.open(iname)
    outfile.create_dataset(mode+str(count), data=outdata, dtype=np.float64) #B1.png
outfile.close()
#%hist -f makeHDF5.py
