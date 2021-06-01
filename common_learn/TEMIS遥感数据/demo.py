#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:56
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo_no.py
# @Software: PyCharm

import urllib.request
import os
import datetime

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)

def dateRange(start, end, step=1, format="%Y%m%d"):
    strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
    days = (strptime(end, format) - strptime(start, format)).days
    return [strftime(strptime(start, format) + datetime.timedelta(i), format) for i in range(0, days, step)]

for i in dateRange('20190901','20190905'):
    url = 'http://www.temis.nl/uvradiation/archives/v2.0/'+i[0:4]+'/'+i[4:6]+'/uvief'+i+'.hdf'
    local = os.path.join('data/'+i+'.hdf')
    #urllib.request.urlretrieve(url,local,Schedule)   # 显示下载进度
    urllib.request.urlretrieve(url,local)
    print(i+'下载完成')