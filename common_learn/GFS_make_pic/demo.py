#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 15:33
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import xarray as xr
import metpy
import metpy.calc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cmaps
import numpy as np
import cartopy.io.shapereader as shpreader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER



data = xr.open_dataset(r'work/GFS_2021052500.nc')
tem_2m = data['Temperature_surface'].metpy.unit_array.squeeze()
dewpoint_2m = data['Dewpoint_temperature_height_above_ground'].metpy.unit_array.squeeze()
rh_2m = data['Relative_humidity_height_above_ground'].metpy.unit_array.squeeze()
lon_1d = data['lon']
lat_1d = data['lat']
data.close()
rh_2m_cal = metpy.calc.relative_humidity_from_dewpoint(tem_2m, dewpoint_2m)
rh_2m_cal[rh_2m_cal>1]=1
rh_2m_cal = rh_2m_cal*100



lon_2d, lat_2d = np.meshgrid(lon_1d, lat_1d)


#2m气温预报图
fig = plt.figure(figsize=(15, 12))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([70, 140, 0, 50])
contours = ax.contourf(lon_2d, lat_2d, tem_2m.to('degC'), levels=range(-5,46),
                       transform=ccrs.PlateCarree(),cmap=cmaps.NCV_bright)
province = shpreader.Reader(r'lact/中国.shp')
# nineline = shpreader.Reader('./work/nine_line.shp')
ax.add_geometries(province.geometries(), crs=ccrs.PlateCarree(), linewidths=0.5,edgecolor='k',facecolor='none')
# ax.add_geometries(nineline.geometries(), crs=ccrs.PlateCarree(),linewidths=0.5, color='k')
gl = ax.gridlines(draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False  #关闭顶端标签
gl.ylabels_right = False  #关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  #x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  #y轴设为纬度格式
cbar = fig.colorbar(contours,shrink=0.8)
cbar.set_label('Temperature(℃)',fontsize=15)
cbar.set_ticks(np.arange(-5,46,5))
ax.set_title('GFS_Temperature_2m  valid at 2021-05-25T00:00:00(UTC)',fontsize=15)

plt.show()


#2m露点预报图
fig = plt.figure(figsize=(15, 12))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([70, 140, 0, 50])
contours = ax.contourf(lon_2d, lat_2d, dewpoint_2m.to('degC'), levels=range(-15,36),
                       transform=ccrs.PlateCarree(),cmap=cmaps.NCV_bright)
province = shpreader.Reader(r'lact/中国.shp')
# nineline = shpreader.Reader('./work/nine_line.shp')
ax.add_geometries(province.geometries(), crs=ccrs.PlateCarree(), linewidths=0.5,edgecolor='k',facecolor='none')
# ax.add_geometries(nineline.geometries(), crs=ccrs.PlateCarree(),linewidths=0.5, color='k')
gl = ax.gridlines(draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False  #关闭顶端标签
gl.ylabels_right = False  #关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  #x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  #y轴设为纬度格式
cbar = fig.colorbar(contours,shrink=0.8)
cbar.set_label('Dewpoint Temperature(℃)',fontsize=15)
cbar.set_ticks(np.arange(-15,36,5))
ax.set_title('GFS_Dewpoint_Temperature_2m  valid at 2021-05-25T00:00:00(UTC)',fontsize=15)

plt.show()


#2m相对湿度预报图
fig = plt.figure(figsize=(15, 12))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([70, 140, 0, 50])
contours = ax.contourf(lon_2d, lat_2d, rh_2m, levels=range(0,101),
                       transform=ccrs.PlateCarree(),cmap=cmaps.MPL_terrain_r)
province = shpreader.Reader(r'lact/中国.shp')
# nineline = shpreader.Reader('./work/nine_line.shp')
ax.add_geometries(province.geometries(), crs=ccrs.PlateCarree(), linewidths=0.5,edgecolor='k',facecolor='none')
# ax.add_geometries(nineline.geometries(), crs=ccrs.PlateCarree(),linewidths=0.5, color='k')
gl = ax.gridlines(draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False  #关闭顶端标签
gl.ylabels_right = False  #关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  #x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  #y轴设为纬度格式
cbar = fig.colorbar(contours,shrink=0.8)
cbar.set_label('Relative Humidity(%)',fontsize=15)
cbar.set_ticks(np.arange(0,101,5))
ax.set_title('GFS_Relative Humidity_2m  valid at 2021-05-25T00:00:00(UTC)',fontsize=15)
plt.savefig('pic/rh.png')
plt.show()



#2m相对湿度预报图（计算所得）
fig = plt.figure(figsize=(15, 12))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([70, 140, 0, 50])
contours = ax.contourf(lon_2d, lat_2d, rh_2m_cal, levels=range(0,101),
                       transform=ccrs.PlateCarree(),cmap=cmaps.MPL_terrain_r)
province = shpreader.Reader(r'lact/中国.shp')
# nineline = shpreader.Reader('./work/nine_line.shp')
ax.add_geometries(province.geometries(), crs=ccrs.PlateCarree(), linewidths=0.5,edgecolor='k',facecolor='none')
# ax.add_geometries(nineline.geometries(), crs=ccrs.PlateCarree(),linewidths=0.5, color='k')
gl = ax.gridlines(draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabels_top = False  #关闭顶端标签
gl.ylabels_right = False  #关闭右侧标签
gl.xformatter = LONGITUDE_FORMATTER  #x轴设为经度格式
gl.yformatter = LATITUDE_FORMATTER  #y轴设为纬度格式
cbar = fig.colorbar(contours,shrink=0.8)
cbar.set_label('Relative Humidity(%)',fontsize=15)
cbar.set_ticks(np.arange(0,101,5))
ax.set_title('GFS_Relative Humidity_2m[calculated]  valid at 2021-05-24T00:00:00(UTC)',fontsize=15)
plt.show()