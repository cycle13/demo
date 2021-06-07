#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 9:51
# @Author  : Yanjun Wang
# @Site    : 
# @File    : poumian.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader as shpreader
import matplotlib.ticker as mticker
import xarray as xr


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False#######################################
filename=r'data/ETOPO2v2g_f4.nc'
f=xr.open_dataset(filename)
lat=f['y'][3591:3621]
height=f['z'][3591:3621,8669]
fig=plt.figure(figsize=(10,10),dpi=60)
ax=fig.add_axes([0,0,1,1])
ax.plot(lat,height,c='k',lw=1)
ax.fill_between(lat,height,facecolor='white',hatch='///')#填充阴影
ax.set_xlim(29.7,30.6)
ax.set_xlabel('北纬(N)',fontsize=7)
ax.set_ylim(0,1650)
ax.set_ylabel('海拔高度(m)',fontsize=7)
ax.tick_params(which='both',labelsize=5)
plt.savefig('county_image/county_image.png')
plt.show()
