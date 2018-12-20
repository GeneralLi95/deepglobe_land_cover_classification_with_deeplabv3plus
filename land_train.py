#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:yaoli 
@file: land_train.py 
@time: 2018/12/19 
"""

# from utils.data_utils import DataSet
from utils.data_utils import DataSet

import numpy as np
import os


train_path = 'dataset/land_train_sat'


def read_data(path):
    """

    :param path:
    :return: a dict with key == train_name value == label_name
    """

    print(os.path.exists(path))
    a = os.listdir(train_path)
    train_name_list = [x for x in a if x[-3:] == 'jpg']
    label_name_list = [x for x in a if x[-3:] == 'png']
    train_name_list.sort()
    label_name_list.sort()
    train_name_list = [(path + '/' + x) for x in train_name_list]
    label_name_list = [(path + '/' + x) for x in label_name_list]
    train_label_dict = dict(zip(train_name_list, label_name_list))
    return train_name_list, label_name_list

a , b = read_data(train_path)
print(a)
print(b)
a = np.array(a)
b = np.array(b)
print(a)
print(b)
