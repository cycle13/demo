from netCDF4 import Dataset
import numpy as np
import pandas as pd
import datetime
import os
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import cartopy.crs as ccrs
import matplotlib.cm as cm
import matplotlib.colors as col
import imageio
import demo1

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# import maskout
ln = ['00','10','20','30','40','50']
for x in list(pd.date_range(start='2021-05-05', end='2021-05-06',freq='H')):
    fns = []
    dt = x.strftime('%Y%m%d')
    d = x.strftime('%H')
    for k in ln:
        dir1 = r'data/'+'NC_H08_{}_{}{}_L2ARP030_FLDK.02401_02401.nc'.format(dt,d,k)
        data = Dataset(dir1, mode='r')
        aot = data.variables['AOT']
        aot = np.array(aot)
        aot[aot < -1000] = -1
        lons = data.variables['longitude']
        lats = data.variables['latitude']
        lon, lat = np.meshgrid(lons, lats)
        proj = ccrs.LambertConformal(central_latitude=35.74, central_longitude=103.95)
        fig, ax = plt.subplots(figsize=(15, 15), subplot_kw=dict(projection=proj))  # 建立页面
        ax.set_extent([75, 130, 15, 55], ccrs.PlateCarree())  # 设置经纬度范围
        levels = np.array([0,1,2,3,4])
        cf = plt.contourf(lon, lat, aot, transform=ccrs.PlateCarree(), cmap="jet", levels=levels)
        fig.canvas.draw()
        ax.xaxis.set_major_formatter(LONGITUDE_FORMATTER)
        ax.yaxis.set_major_formatter(LATITUDE_FORMATTER)
        xticks = list(range(75, 130, 5))
        yticks = list(range(15, 55, 5))
        demo1.lambert_xticks(ax, xticks)
        demo1.lambert_yticks(ax, yticks)
        ax.gridlines(xlocs=xticks, ylocs=yticks, linewidth=0.1, linestyle='--',color = 'black')
        cb=fig.colorbar(cf,shrink=0.8)
        # cb.set_label("单位：℃",fontsize=15)
        cb.ax.tick_params(direction='out',length=5)
        plt.title('葵花8号全国气溶胶光学厚度',fontsize=16)
        shpname = r'lact/china1/中国.shp'
        adm1_shapes=list(shpreader.Reader(shpname).geometries())
        ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
        plt.savefig('pic/'+'{}_{}{}.png'.format(dt,d,k))
        plt.close('all')
        print('{}_{}{}.png绘制完成'.format(dt,d,k))


