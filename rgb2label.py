#!usr/bin/env python  
#-*- coding:utf-8 _*-
"""
@author:yaoli
@file: rgb2label.py
@time: 2018/12/21
The mask.png are RGB img. We have to change it into a one-chanel img.
"""

import numpy as np
import cv2
import os
from tqdm import tqdm
import scipy.misc
import imageio

def color2annotation(input_path, output_path):

    # image = scipy.misc.imread(input_path)
    # imread is deprecated in SciPy 1.0.0, and will be removed in 1.2.0. Use imageio.imread instead.
    image = imageio.imread(input_path)
    image = (image >= 128).astype(np.uint8)
    image = 4 * image[:, :, 0] + 2 * image[:, :, 1] + image[:, :, 2]
    cat_image = np.zeros((2448,2448), dtype=np.uint8)
    cat_image[image == 3] = 0  # (Cyan: 011) Urban land
    cat_image[image == 6] = 1  # (Yellow: 110) Agriculture land
    cat_image[image == 5] = 2  # (Purple: 101) Rangeland
    cat_image[image == 2] = 3  # (Green: 010) Forest land
    cat_image[image == 1] = 4  # (Blue: 001) Water
    cat_image[image == 7] = 5  # (White: 111) Barren land
    cat_image[image == 0] = 6  # (Black: 000) Unknown


    # scipy.misc.imsave(output_path, cat_image)
    imageio.imsave(output_path, cat_image)
    pass

one_channel_label_path = 'dataset/land_train'
test_mask_path = 'dataset/onechannel_label'

filelist = os.listdir(one_channel_label_path)
file_names = np.array([file.split('_')[0] for file in filelist if file.endswith('.png')], dtype=object)

for filename in tqdm(file_names):
    mask_path = os.path.join(one_channel_label_path, filename + '_mask.png')
    label_path = os.path.join(test_mask_path, filename + '_label.png')
    color2annotation(mask_path, label_path)




"""
old encode part
"""
# def read_data(path):
#     """
#
#     :param path:
#     :return: a name_list
#     """
#
#     # print(os.path.exists(path))
#     a = os.listdir(path)
#     name_list = [x for x in a if  x[-3:] == 'png']
#     name_list.sort()
#     name_list = [(path + '/' + x) for x in name_list]
#     return name_list
#
# def rgb2label(input_path, output_path, color_codes = None, one_hot_encode=False):
#     img = cv2.imread(input_path)
#     if color_codes is None:
#         color_codes = {val:i for i,val in enumerate(set( tuple(v) for m2d in img for v in m2d ))}
#     n_labels = len(color_codes)
#     result = np.ndarray(shape=img.shape[:2], dtype=int)
#     result[:,:] = -1
#     for rgb, idx in color_codes.items():
#         result[(img==rgb).all(2)] = idx
#
#     if one_hot_encode:
#         one_hot_labels = np.zeros((img.shape[0],img.shape[1],n_labels))
#         # one-hot encoding
#         for c in range(n_labels):
#             one_hot_labels[: , : , c ] = (result == c ).astype(int)
#         result = one_hot_labels
#
#     cv2.imwrite(output_path, result)
#
# my_codes = {(0, 255, 255): 0, (255, 255, 0): 1, (255, 0, 255): 2, (0, 255, 0): 3, (0, 0, 255): 4, (255, 255, 255): 5, (0, 0, 0): 6}
#
# mask_path = 'dataset/test'
# one_channel_label_path = 'dataset/onechannel_label'
#
# mask_filelist = read_data(mask_path)
#
#
# # generate onechannel_label
# for x in tqdm(mask_filelist):
#     img_path = x
#     number = img_path.split('/')[2].split('_')[0]
#     label_path = one_channel_label_path + '/' + number + '_label.png'
#     rgb2label(input_path=img_path, output_path=label_path, color_codes = my_codes)
