#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 10:02
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import os
import imageio



def create_gif(image_list, gif_name, duration = 1.0):
    '''
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

fns = []
listdir = os.listdir(r'D:/pythonProject/GFS_data/hunheceng/pic/')
for i in listdir:
    fns.append(r'D:/pythonProject/GFS_data/hunheceng/pic/'+i)

create_gif(fns,'gif/demo.gif',duration = 1.0)