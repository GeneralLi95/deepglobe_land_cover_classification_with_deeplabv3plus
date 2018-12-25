#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yaoli 
@file: land_train.py 
@time: 2018/12/19 
"""
import numpy as np
import os
import tensorflow as tf
from utils.data_utils import DataSet, read_data
from tensorflow.python.framework import ops
ops.reset_default_graph()

class args:
    batch_size = 32
    lr = 0.0002
    display = 1
    weight_decay = 0.00001
    model_name = 'deeplab_v3'
    batch_norm_decay = 0.95

# prepare data
# train_path has 643 img and labels
# valid_path has 160 img and labels
train_sat_path = 'dataset/train_sat'
train_mask_path = 'dataset/train_mask'
train_label_path = 'dataset/train_label'
valid_sat_path = 'dataset/valid_sat'
valid_mask_path = 'dataset/valid_mask'
valid_label_path = 'dataset/valid_label'



train_img = read_data(train_sat_path)
train_label = read_data(train_mask_path)
valid_img = read_data(valid_sat_path)
valid_label = read_data(valid_mask_path)
print(train_img)
print(train_label)
dataset_tr = DataSet(image_path=train_img, label_path=train_label)
dataset_val = DataSet(image_path=valid_img, label_path=valid_label)
print('Data input success.')
