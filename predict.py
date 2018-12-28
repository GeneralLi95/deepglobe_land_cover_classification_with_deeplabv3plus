#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: predict.py 
@time: 2018/12/28
模型保存后
"""
import tensorflow as tf
import numpy as np
import cv2
from utils.color_utils import color_annotation

def sat_img_predict(sat_img_path,input_node,is_training_node, predict_node,predict_path,color_path):

    sat_img = cv2.imread(sat_img_path, cv2.CAP_MODE_RGB)
    feed_dict = {input_node: np.expand_dims(sat_img, 0),
                 is_training_node:False}
    predict = sess.run(predict_node, feed_dict=feed_dict)
    cv2.imwrite(predict_path, np.squeeze(predict))
    color_annotation(predict_path, color_path)


if __name__ == '__main__':
    checkpoint_file = tf.train.latest_checkpoint('ckpts_result/deeplab_v3')
    graph = tf.Graph()
    with graph.as_default():
        sess = tf.Session()
        saver = tf.train.import_meta_graph('{}.meta'.format(checkpoint_file))
        saver.restore(sess, checkpoint_file)

        is_training = graph.get_tensor_by_name('is_training: 0')
        input_node = graph.get_tensor_by_name('input_x: 0')
        predicts = graph.get_tensor_by_name('predicts: 0')

        param = {
            'sat_img_path':'./10452_sat.jpg',
            'input_node':input_node,
            'is_training_node': is_training,
            'predict_node': predicts,
            'predict_path': './annotation.png',
            'color_path':'./color.png'
        }
        sat_img_predict(**param)

