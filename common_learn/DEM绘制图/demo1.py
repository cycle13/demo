#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:59
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import gdal
import cmaps


ds = gdal.Open(r"F:\内蒙古项目\呼市\hebing.tif")
dem = ds.ReadAsArray()
dem

nrows  =  ds.RasterXSize
ncols  =  ds.RasterYSize
print('行数；{}\n列数：{}'.format(nrows,ncols))

gt = ds.GetGeoTransform()
xres = gt[1]
yres = gt[5]
xmin = gt[0] + xres * 0.5
xmax = gt[0] + (xres * ds.RasterXSize) - xres * 0.5
ymin = gt[3] + (yres * ds.RasterYSize) + yres * 0.5
ymax = gt[3] - yres * 0.5
lons, lats = np.mgrid[xmin:xmax+xres:xres, ymax+yres:ymin:yres]
