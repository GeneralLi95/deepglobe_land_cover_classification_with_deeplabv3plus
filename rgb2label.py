#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: rgb2label.py 
@time: 2018/12/21
The mask.png are RGB img. We have to change it into a one-chanel img.
将3通道的RGB图像转换为单通道的图像
"""

import numpy as np
import cv2
import os
from tqdm import tqdm

def read_data(path):
    """

    :param path:
    :return: a name_list
    """

    # print(os.path.exists(path))
    a = os.listdir(path)
    name_list = [x for x in a if x[-3:] == 'jpg' or x[-3:] == 'png']
    name_list.sort()
    name_list = [(path + '/' + x) for x in name_list]
    return name_list

def rgb2label(input_path, output_path, color_codes = None, one_hot_encode=False):
    img = cv2.imread(input_path)
    if color_codes is None:
        color_codes = {val:i for i,val in enumerate(set( tuple(v) for m2d in img for v in m2d ))}
    n_labels = len(color_codes)
    result = np.ndarray(shape=img.shape[:2], dtype=int)
    result[:,:] = -1
    for rgb, idx in color_codes.items():
        result[(img==rgb).all(2)] = idx

    if one_hot_encode:
        one_hot_labels = np.zeros((img.shape[0],img.shape[1],n_labels))
        # one-hot encoding
        for c in range(n_labels):
            one_hot_labels[: , : , c ] = (result == c ).astype(int)
        result = one_hot_labels

    cv2.imwrite(output_path, result)

my_codes = {(0, 255, 255): 0, (255, 255, 0): 1, (255, 0, 255): 2, (0, 255, 0): 3, (0,0,255): 4, (255, 255, 255): 5, (0,0,0): 6}

train_mask_path = 'dataset/train_mask'
train_label_path = 'dataset/train_label'

valid_mask_path = 'dataset/valid_mask'
valid_label_path = 'dataset/valid_label'

train_mask = read_data(train_mask_path)
valid_mask = read_data(valid_mask_path)

# generate train label
for x in tqdm(train_mask):
    img_path = x
    number = img_path.split('/')[2].split('_')[0]
    label_path = train_label_path + '/' + number + '_label.png'
    print(rgb2label(input_path=img_path, output_path=label_path, color_codes = my_codes))

# generate valid label
for x in tqdm(valid_mask):
    img_path = x
    number = img_path.split('/')[2].split('_')[0]
    label_path = valid_label_path + '/' + number + '_label.png'
    rgb2label(input_path=img_path, output_path=label_path, color_codes = my_codes)



