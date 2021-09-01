#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 21:06
# @Author  : Yanjun Wang
# @Site    : 
# @File    : make_gif.py
# @Software: PyCharm

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





img_names = ['D:\pythonProject\GFS_data\demo2\pic\pic{}.png'.format(i) for i in range(248,305)]
create_gif(img_names,'山西省云图1.gif', duration=0.5)