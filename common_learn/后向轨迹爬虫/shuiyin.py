#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 16:26
# @Author  : Yanjun Wang
# @Site    : 
# @File    : shuiyin.py
# @Software: PyCharm

from PIL import Image,ImageDraw,ImageFont


def shuiyin(name):
    imagefile = 'pic/'+name
    imageinfo = Image.open(imagefile)
    font = ImageFont.truetype('C:\Windows\Fonts\simfang.ttf',20)

    draw = ImageDraw.Draw(imageinfo)
    draw.text((imageinfo.size[0]/2+80,imageinfo.size[1]/2+310),'微信公众号：晴颸 浮阳',font=font)

    imageinfo.save(imagefile)
