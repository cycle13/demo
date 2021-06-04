#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 13:18
# @Author  : Yanjun Wang
# @Site    : 
# @File    : NO2.py
# @Software: PyCharm

from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#import data
ncl_file = Dataset('data/S5P_OFFL_L2__NO2____20210122T050057_20210122T064228_16980_01_010400_20210123T223828.nc')
print(ncl_file.groups['PRODUCT'].variables)

#save data lat,lon and no2
lat = ncl_file.groups['PRODUCT'].variables['latitude'][0,:,:]
lon = ncl_file.groups['PRODUCT'].variables['longitude'][0,:,:]
no2_data = ncl_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'][0,:,:]

# extract fill value
fill_value = ncl_file.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column']._FillValue
fill_val = fill_value*1000000

no2_cm = np.array(no2_data)*1000000
no2_cm[no2_cm==fill_val] = np.nan
no2_data = no2_cm

#creat basemap

m = Basemap(projection='cyl',resolution='l',llcrnrlat=-89.96179,urcrnrlat=85.31206,llcrnrlon=-179.99873,urcrnrlon=179.99977)
m.drawcoastlines(linewidth=1.5)
m.drawcoastlines(linewidth=3)
cmap = plt.cm.get_cmap('jet')
cmap.set_under('w')

m.pcolormesh(lon,lat,no2_data,latlon = True,vmin=0,vmax = 500,cmap=cmap)
color_bar = m.colorbar()
color_bar.set_label('μ.mol/Sq.meter')

plt.title('NO2排放数据')
plt.show()

