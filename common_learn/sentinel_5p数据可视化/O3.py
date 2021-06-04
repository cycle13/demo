#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 12:14
# @Author  : Yanjun Wang
# @Site    : 
# @File    : O3.py
# @Software: PyCharm

from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#import data
ncl_file = Dataset('data/S5P_NRTI_L2__O3_____20210604T060701_20210604T061201_18867_01_020104_20210604T065312.nc')

#save data lat,lon and no2
lat = ncl_file.groups['PRODUCT'].variables['latitude'][0,:,:]
lon = ncl_file.groups['PRODUCT'].variables['longitude'][0,:,:]
O3_data = ncl_file.groups['PRODUCT'].variables['ozone_total_vertical_column'][0,:,:]

# extract fill value
fill_value = ncl_file.groups['PRODUCT'].variables['ozone_total_vertical_column']._FillValue
fill_val = fill_value*1000000

O3_cm = np.array(O3_data)*1000000
O3_cm[O3_cm==fill_val] = np.nan
O3_data = O3_cm

#creat basemap

m = Basemap(projection='cyl',resolution='l',llcrnrlat=-89.96179,urcrnrlat=85.31206,llcrnrlon=-179.99873,urcrnrlon=179.99977)
m.drawcoastlines(linewidth=1.5)
m.drawcoastlines(linewidth=3)
cmap = plt.cm.get_cmap('jet')
cmap.set_under('w')
m.pcolormesh(lon,lat,O3_data,latlon = True,vmin=120000,vmax = 140000,cmap=cmap)
color_bar = m.colorbar()
color_bar.set_label('μ.mol/Sq.meter')

plt.title('6月4日6时O3在我国广东、海口等地分布图')
plt.show()

