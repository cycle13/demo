import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import pandas as pd
import numpy as np
from matplotlib.collections import LineCollection
#地图设置
proj = ccrs.PlateCarree(central_longitude=105)
leftlon, rightlon, lowerlat, upperlat = (60,150,-15,50)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
fig = plt.figure(figsize=(25,7))
f_ax = fig.add_axes([0.1, 0.1, 0.8, 0.8],projection = proj)
f_ax.set_extent(img_extent, crs=ccrs.PlateCarree())
f_ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
f_ax.add_feature(cfeature.LAKES, alpha=0.5)
f_ax.set_xticks(np.arange(leftlon,rightlon+10,10), crs=ccrs.PlateCarree())
f_ax.set_yticks(np.arange(lowerlat,upperlat+10,10), crs=ccrs.PlateCarree())
f_ax.xaxis.set_major_formatter(lon_formatter)
f_ax.yaxis.set_major_formatter(lat_formatter)
# 加载中国地图
china = shpreader.Reader('data/bou2_4l.dbf').geometries()
#绘制中国国界省界九段线等等
f_ax.add_geometries(china, ccrs.PlateCarree(),facecolor='none', edgecolor='black',zorder = 1)
#text是我的177条轨迹
n = 176
for i in range(n):
    lat = text[i].loc[:,9]
    lon = text[i].loc[:,10]
#h是高度值
    h = text[i].loc[:,11]
    points = np.array([lon, lat]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = plt.Normalize(0, 1000)
#设置颜色线条
    lc = LineCollection(segments, cmap='jet', norm=norm,transform=ccrs.PlateCarree())
    lc.set_array(h)
#绘制线条
    line = f_ax.add_collection(lc)
#colorbar
fig.colorbar(line)#方向
