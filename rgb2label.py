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
rgb_path = '119_mask.png'
label_path = '119_label.png'
def rgb2label(input_path, output_path):
    img = cv2.imread(input_path)
    print(img)
    label = np.ones(img.shape[0])


    cv2.imwrite(output_path,label)


rgb2label(rgb_path,label_path)