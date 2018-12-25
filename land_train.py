#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yaoli 
@file: land_train.py 
@time: 2018/12/19 
"""
from utils.data_utils import DataSet, read_data
from tensorflow.python.framework import ops
from deeplab_v3 import Deeplab_v3
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import numpy as np
import tensorflow as tf
import pandas as pd
import os

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
train_label = read_data(train_label_path)
valid_img = read_data(valid_sat_path)
valid_label = read_data(valid_label_path)
# print(train_img)
# print(train_label)
dataset_tr = DataSet(image_path=train_img, label_path=train_label)
dataset_val = DataSet(image_path=valid_img, label_path=valid_label)
print('Data input success.')

model = Deeplab_v3(batch_norm_decay=args.batch_norm_decay)

image = tf.placeholder(tf.float32, [None, 2448, 2448, 3], name='input_x')
label = tf.placeholder(tf.int32, [None, 2448, 2448])
lr = tf.placeholder(tf.float32)

logits = model.forward_pass(image)
predicts = tf.argmax(logits, axis=-1, name='predicts')

