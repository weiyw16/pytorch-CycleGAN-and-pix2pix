#import
import os
#import torch
#import torch.nn as nn
import torch.utils.data as Data
#import torchvision
import matplotlib.pyplot as plt
import h5py
#from torch.autograd import Variable
import numpy as np
import torch
class rawdataDataset(Data.Dataset):
    
    def __init__(self):
        super(rawdataDataset, self).__init__()
    
    #def __init__(self, filename, root_dir, transform=None):
    #    self.frame = h5py.File(root_dir + filename, 'r')
    #    self.root_dir = root_dir
    #    self.transform = transform
        
    def name(self):
        return 'rawdataDataset'

    @staticmethod
    def modify_commandline_options(parser, is_train):
        return parser
    
    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_AB = os.path.join(opt.dataroot, opt.phase) # phase: train test
        #self.AB_paths = sorted(make_dataset(self.dir_AB))
        self.A_paths = self.dir_AB + "/A.h5"
        self.B_paths = self.dir_AB + "/B.h5"
        self.frameA = h5py.File(self.A_paths, 'r')
        self.frameB = h5py.File(self.B_paths, 'r')
        #assert(opt.resize_or_crop == 'resize_and_crop')
    
    def __len__(self):
        return len(self.frameA)
    
    def __getitem__(self, index):
        #img_name = torch.FloatTensor([[ self.frame["pic" + str(index)] ]])
        #img_name = Variable(torch.FloatTensor([[ self.frame["pic" + str(index)] ]])
        A = torch.FloatTensor([[ self.frameA["A" + str(index)] ]])
        B = torch.FloatTensor([[ self.frameB["B" + str(index)] ]])
        
        #AB_path = self.AB_paths[index]
        #AB = Image.open(AB_path).convert('RGB')
        #w, h = AB.size
        #w2 = int(w / 2)
        #A = AB.crop((0, 0, w2, h)).resize((self.opt.loadSize, self.opt.loadSize), Image.BICUBIC)
        #B = AB.crop((w2, 0, w, h)).resize((self.opt.loadSize, self.opt.loadSize), Image.BICUBIC)
        #A = transforms.ToTensor()(A)
        #B = transforms.ToTensor()(B)
        #w_offset = random.randint(0, max(0, self.opt.loadSize - self.opt.fineSize - 1))
        #h_offset = random.randint(0, max(0, self.opt.loadSize - self.opt.fineSize - 1))

        #A = A[:, h_offset:h_offset + self.opt.fineSize, w_offset:w_offset + self.opt.fineSize]
        #B = B[:, h_offset:h_offset + self.opt.fineSize, w_offset:w_offset + self.opt.fineSize]

        #A = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(A)
        #B = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(B)
        
        if self.opt.which_direction == 'BtoA':
            input_nc = self.opt.output_nc
            output_nc = self.opt.input_nc
        else:
            input_nc = self.opt.input_nc
            output_nc = self.opt.output_nc
        #return img_name     
        return {'A' : A, 'B' : B, 'A_paths' : self.A_paths, 'B_paths' : self.B_paths}
#%hist -f rawdata_dataset.py
