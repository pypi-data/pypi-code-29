# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:14:05 2018

@author: yifal
"""

#%matplotlib notebook
from __future__ import print_function
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
import torch.nn.functional as F
import skimage
import skimage.io
import skimage.transform
import numpy as np
import time 
from PSMNet.models import basic,stackhourglass
from PSMNet.utils import preprocess,readpfm
from skimage import exposure,img_as_float
#from PSMNet import preprocess

processed = preprocess.get_transform(augment=False)

class Config(object):
    USE_CUDA = True
    SEED = 10
    USE_MODEL = 'stackhourglass'
    MAXDISP = 192

config = Config()

torch.cuda.manual_seed(config.SEED)

if config.USE_MODEL == 'stackhourglass':
    model = stackhourglass(config.MAXDISP)
elif config.USE_MODEL == 'basic':
    model = basic(config.MAXDISP)
else:
    print('no model')

model = nn.DataParallel(model, device_ids=[0])
model.cuda()


def load_model(model_file):
    state_dict = torch.load(model_file)
    model.load_state_dict(state_dict['state_dict'])
    print('Number of model parameters: {}'.format(sum([p.data.nelement() for p in model.parameters()])))


def test(imgL,imgR):
    model.eval()

    if config.USE_CUDA:
        imgL = torch.FloatTensor(imgL).cuda()
        imgR = torch.FloatTensor(imgR).cuda()     

    imgL, imgR= Variable(imgL), Variable(imgR)

    with torch.no_grad():
        output = model(imgL,imgR)
    output = torch.squeeze(output)
    pred_disp = output.data.cpu().numpy()

    return pred_disp


def calculate_disparity(imgL,imgR,model_file):
    load_model(model_file)
    imgL_o = (skimage.io.imread(imgL).astype('float32'))
    imgR_o = (skimage.io.imread(imgR).astype('float32'))
    
    imgL = processed(imgL_o).numpy()
    imgR = processed(imgR_o).numpy()
    imgL = np.reshape(imgL,[1,3,imgL.shape[1],imgL.shape[2]])
    imgR = np.reshape(imgR,[1,3,imgR.shape[1],imgR.shape[2]])
    
    pad_row = 1344
    pad_col = 1344
    
    top_pad = pad_row-imgL.shape[2]
    left_pad = pad_col-imgL.shape[3]
    imgL = np.lib.pad(imgL,((0,0),(0,0),(top_pad,0),(0,left_pad)),mode='constant',constant_values=0)
    imgR = np.lib.pad(imgR,((0,0),(0,0),(top_pad,0),(0,left_pad)),mode='constant',constant_values=0)

    start_time = time.time()
    pred_disp = test(imgL,imgR)
    print('time = %.2f' %(time.time() - start_time))
    
    top_pad   = pad_row-imgL_o.shape[0]
    left_pad  = pad_col-imgL_o.shape[1]
    img = pred_disp[top_pad:,:-left_pad]
    
    return img
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    