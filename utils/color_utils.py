#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: color_utils.py 
@time: 2018/12/23 
"""
import numpy as np
import cv2

# 给标签图上色

def color_annotation(label_path, output_path):

    '''

    给class图上色

    '''

    img = cv2.imread(label_path,cv2.CAP_MODE_GRAY)

    color = np.ones([img.shape[0], img.shape[1], 3])



    color[img==0] = [0, 255, 255]  # 浅蓝色，人造建筑 0

    color[img==1] = [255, 255, 0]  #  黄色，农田，1

    color[img==2] = [255, 0, 255]  #  紫色，除了森林，农田之外的绿色土地，草地 2

    color[img==3] = [0, 255, 0]    #  绿色，任何土地上有x%的树冠密度 3

    color[img==4] = [0, 0, 255]    #  深蓝色，江河湖海湿地 4

    color[img==5] = [255, 255, 255] # 白色，山地，荒漠，戈壁，沙漠，没有植被的地方

    color[img==6] = [0, 0, 0]       # 黑色，未知土地，云层遮盖或其他因素


    cv2.imwrite(output_path,color)
