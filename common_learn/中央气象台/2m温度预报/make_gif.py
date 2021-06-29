#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 14:27
# @Author  : Yanjun Wang
# @Site    : 
# @File    : make_gif.py
# @Software: PyCharm

import imageio
import os


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


code = ['ETMP_ACHN_L2M_PB','EDA_ACHN_L10M_P9']
for name in code:
    img_names = ['pic/{}/{}.png'.format(name,str(i)) for i in range(48,85)]
    if not os.path.exists('gif'):
        os.makedirs('gif')
    create_gif(img_names,'gif/全国{}.gif'.format(name), duration=0.5)