#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: resize.py 
@time: 2018/12/26 
"""
from PIL import Image
import os
from tqdm import tqdm

def convert(input_dir,output_dir,width, height):
    file_list = os.listdir(input_dir)
    file_list = [x for x in file_list if x[-3:] == 'jpg' or x[-3:] == 'png']
    for file_name in tqdm(file_list):
        path = input_dir + file_name
        im = Image.open(path)
        out = im.resize((width,height), Image.ANTIALIAS)
        out.save(output_dir + file_name)

if __name__ == "__main__":
    convert('dataset/train_sat/','dataset/resize_train_sat/',256, 256)
    convert('dataset/train_label/','dataset/resize_train_label/',256, 256)
    convert('dataset/valid_sat/','dataset/resize_valid_sat/',256, 256)
    convert('dataset/valid_label/','dataset/resize_valid_label/',256, 256)