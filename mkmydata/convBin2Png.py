import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
workpath = "./"
mode = "Pmultitrain" # "test"
mode_A1 = "div"
mode_A2 = "curl"
mode_B1 = "vz"
mode_B2 = "vx"

if not os.path.exists(workpath + mode):
    os.makedirs(workpath + mode)
if not os.path.exists(os.getcwd() + "/" + mode_A1  + "_split"):
    os.makedirs(os.getcwd() + "/" + mode_A1  + "_split")
if not os.path.exists(os.getcwd() + "/" + mode_B1  + "_split"):
    os.makedirs(os.getcwd() + "/" + mode_B1  + "_split")
if not os.path.exists(os.getcwd() + "/" + mode_A2  + "_split"):
    os.makedirs(os.getcwd() + "/" + mode_A2  + "_split")
if not os.path.exists(os.getcwd() + "/" + mode_B2  + "_split"):
    os.makedirs(os.getcwd() + "/" + mode_B2  + "_split")


filenum = 0
for root,dirs,files in os.walk(workpath + mode_B1):    #遍历统计  
    for each in files:  
        if each[-4:] == '.bin':  
            #print( root,dirs,each)  
            filenum += 1  

nt = 4000
nr = 301
out_data = np.empty((nt,nr))
nx_out = 276
nz_out = 276
NX = nx_out * 2
NZ = nz_out
for count in range(filenum): # 0 ~ filenum-1
    in_A1_path = os.getcwd() + "/" + mode_A1  + "/div" + str(count) + ".bin"
    in_B1_path = os.getcwd() +  "/" + mode_B1  + "/vz" + str(count) + ".bin"
    in_A2_path = os.getcwd() + "/" + mode_A2  + "/curl" + str(count) + ".bin"
    in_B2_path = os.getcwd() +  "/" + mode_B2  + "/vx" + str(count) + ".bin"


    out_A1_path =  os.getcwd() + "/" + mode_A1  + "_split/A" + str(count+1) + ".png"
    out_B1_path =  os.getcwd() + "/" + mode_B1  + "_split/B" + str(count+1) + ".png"
    out_A2_path =  os.getcwd() + "/" + mode_A2  + "_split/A" + str(count+1) + ".png"
    out_B2_path =  os.getcwd() + "/" + mode_B2  + "_split/B" + str(count+1) + ".png"
    outname = os.getcwd() + "/" + mode + "/" + str(count+1) + ".png"
    
    FA = open(in_A1_path, "rb")
    for tt in range(nt):
        for rr in range(nr):
            data = FA.read(4)
            data_float = struct.unpack("f", data)[0]
            out_data[tt][rr] = data_float
     #np.shape(out_data)   # (4000,301)
    cut_data = out_data[0:4000, 8:301]
    #pic = plt.imshow(cut_data,vmin=-0.00000001, vmax = 0.00000001, extent=[0, 256, 256, 0])#, shape=[100,100])
    plt.imsave(out_A1_path, cut_data, vmin=-0.00000001, vmax = 0.00000001)
    #plt.imsave('A01.png', cut_data, vmin=-0.00000001, vmax = 0.00000001)
    Image.open(out_A1_path).resize((nx_out, nz_out), Image.ANTIALIAS).save(out_A1_path)

    # B
    FB = open(in_B1_path, "rb")
    for tt in range(nt):
        for rr in range(nr):
            data = FB.read(4)
            data_float = struct.unpack("f", data)[0]
            out_data[tt][rr] = data_float
     #np.shape(out_data)   # (4000,301)
    cut_data = out_data[0:4000, 8:301]
    #pic = plt.imshow(cut_data,vmin=-0.00000001, vmax = 0.00000001, extent=[0, 256, 256, 0])#, shape=[100,100])
    plt.imsave(out_B1_path, cut_data, vmin=-0.00000001, vmax = 0.00000001)
    Image.open(out_B1_path).resize((nx_out, nz_out), Image.ANTIALIAS).save(out_B1_path)

    FA = open(in_A2_path, "rb")
    for tt in range(nt):
        for rr in range(nr):
            data = FA.read(4)
            data_float = struct.unpack("f", data)[0]
            out_data[tt][rr] = data_float
     #np.shape(out_data)   # (4000,301)
    cut_data = out_data[0:4000, 8:301]
    #pic = plt.imshow(cut_data,vmin=-0.00000001, vmax = 0.00000001, extent=[0, 256, 256, 0])#, shape=[100,100])
    plt.imsave(out_A2_path, cut_data, vmin=-0.00000001, vmax = 0.00000001)
    #plt.imsave('A01.png', cut_data, vmin=-0.00000001, vmax = 0.00000001)
    Image.open(out_A2_path).resize((nx_out, nz_out), Image.ANTIALIAS).save(out_A2_path)

    # B
    FB = open(in_B2_path, "rb")
    for tt in range(nt):
        for rr in range(nr):
            data = FB.read(4)
            data_float = struct.unpack("f", data)[0]
            out_data[tt][rr] = data_float
     #np.shape(out_data)   # (4000,301)
    cut_data = out_data[0:4000, 8:301]
    #pic = plt.imshow(cut_data,vmin=-0.00000001, vmax = 0.00000001, extent=[0, 256, 256, 0])#, shape=[100,100])
    plt.imsave(out_B2_path, cut_data, vmin=-0.00000001, vmax = 0.00000001)
    Image.open(out_B2_path).resize((nx_out, nz_out), Image.ANTIALIAS).save(out_B2_path)
#%hist -f convBin2Png.py
