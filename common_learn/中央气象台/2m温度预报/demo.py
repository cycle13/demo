#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 14:19
# @Author  : Yanjun Wang
# @Site    : 
# @File    : sendemail.py
# @Software: PyCharm
import requests
import datetime
import time
import os


first_url = 'http://image.nmc.cn/product/2021/06/27/NWPR/medium/SEVP_CNWP_NWPR_SRGRP_{}_2021062700000{}03.png'
session = requests.Session()

def spidrs(name):
    for i in range(85):
        print(i)
        if i <10:
            url = first_url.format(name,'0'+str(i))
        else:
            url = first_url.format(name,str(i))
        res = session.get(url)
        if res.status_code == 200:
            if not os.path.exists('pic/{}'.format(name)):
                os.makedirs('pic/{}'.format(name))
            with open('pic/{}/{}.png'.format(name,str(i)),'wb') as f:
                f.write(res.content)


code = ['ETMP_ACHN_L2M_PB','EDA_ACHN_L10M_P9']
for name in code:
    spidrs(name)