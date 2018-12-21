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


# prepare data
# train_path has 643 img and labels
# valid_path has 160 img and labels
train_path = 'dataset/train'
valid_path = 'dataset/valid'



train_img, train_label = read_data(train_path)
valid_img, valid_label = read_data(valid_path)
dataset_tr = DataSet(image_path=train_img, label_path=train_label)
dataset_val = DataSet(image_path=valid_img, label_path=valid_label)
print('Data input success.')
