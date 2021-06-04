#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 17:04
# @Author  : Yanjun Wang
# @Site    : 
# @File    : NO2.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import netCDF4 as nc
import matplotlib as mpl
import pandas as pd
import maskout
import matplotlib.patheffects as path_effects


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=128):
    new_cmap = mpl.colors.LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name,a=minval, b=maxval),cmap(np.linspace(minval, maxval, n)))
    return new_cmap

topo_file= r'data/ETOPO2v2g_f4.nc'
data=nc.Dataset(topo_file)
print(data)
topo=data.variables['z'][2600:,5400:]
lat=data.variables['y'][2600:]
lon=data.variables['x'][5400:]

# sta = pd.read_csv('sta160.csv', header=0, names=['sname', 'sid', 'slat', 'slon'])
# sta_name_160 = sta['sname']
# sta_id_160 = sta['sid']
# lo_160= sta['slon'].to_numpy()
# la_160 = sta['slat'].to_numpy()

fig, ax = plt.subplots(figsize=(11,8)) #建立绘图平台
m = Basemap(width=6500000,height=4300000
            ,resolution='l',projection='lcc',
            lat_1=30.,lat_2=45,lat_0=36,lon_0=109.)
m.readshapefile('bou1\\bou1_4l', 'chn', color='k', linewidth=0.5)
m.drawcoastlines(linewidth=0.3, color='gray')

parallels = np.arange(0,80,10) #纬线
m.drawparallels(parallels,labels=[True,False,False,False],linewidth=0.3,dashes=[1,4])
meridians = np.arange(80,150,10) #经线
m.drawmeridians(meridians,labels=[False,False,False,True],linewidth=0.3,dashes=[1,4])

lons, lats = np.meshgrid(lon,lat) #经纬度2维化
x, y = m(lons, lats) #投影映射

cmap_new = truncate_colormap(plt.cm.terrain, 0.23, 1.0) #截取colormap，要绿色以上的（>=0.23）
cmap_new.set_under([198/255,234/255,250/255]) #低于0的填色为海蓝
lev=np.arange(0,5600,200)
norm3 = mpl.colors.BoundaryNorm(lev, cmap_new.N) #标准化level，映射色标
cf=m.contourf(x,y,topo,levels=lev,norm=norm3
              ,cmap=cmap_new,extend='both')
clip=maskout.shp2clip(cf,ax,m,'county\\country1',['China'])
plt.title('中国地形图')
cb=plt.colorbar(cf, ax=ax,shrink=0.7,aspect=30,pad=0.05,orientation='horizontal') #色标
cb.ax.tick_params(labelsize=10,pad=2,direction='in') #色标tick

# aa,bb=m(lo_160, la_160)
# t=m.scatter(aa, bb, s=25, marker='^',label='CMA   (%d Stations)'%len(lo_160), color='g', zorder=6)
# t.set_path_effects([path_effects.PathPatchEffect(edgecolor='k', facecolor='r', linewidth=0.3)])
# ax.legend(loc=1)

# 南海小图
a = plt.axes([0.73, 0.27, 0.12, 0.23])
lon_leftup=107;lat_leftup=24
lon_rightdown=121.3;lat_rightdown=2.4
m = Basemap(projection='cyl', llcrnrlat=lat_rightdown, urcrnrlat=lat_leftup, llcrnrlon=lon_leftup, urcrnrlon=lon_rightdown, resolution='l')
m.drawcoastlines(linewidth=0.3, color='gray')
m.readshapefile('bou1\\bou1_4l', 'chn', color='k', linewidth=0.5)

x, y = m(lons, lats) #投影映射
cf=m.contourf(x,y,topo,levels=lev,norm=norm3
              ,cmap=cmap_new,extend='both')
clip2=maskout.shp2clip(cf,a,m,'county\\country1',['China'])
# aa,bb=m(lo_160, la_160)
# t=m.scatter(aa, bb, s=25, marker='^',label='CMA   (%d Stations)'%len(lo_160), color='g', zorder=6)
# t.set_path_effects([path_effects.PathPatchEffect(edgecolor='k', facecolor='r', linewidth=0.3)])

font1={'family':'SimHei','size':8,'color':'black'}
a.text(0.58,0.04,'南海诸岛',transform=a.transAxes,fontdict=font1,
       bbox=dict(boxstyle='square',ec='k',fc='w',pad=0.3))

plt.savefig(r'pic\chn_etopo160.png',dpi=300,bbox_inches='tight') #存图
plt.show()



