#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 13:58
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo_no.py
# @Software: PyCharm

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.units import units
import numpy as np
import xarray as xr


ds = xr.open_dataset('work/GFS_2021052501.nc').metpy.parse_cf()

# 设置数据地理范围的子集切片以限制下载
lon_slice = slice(200, 350)
lat_slice = slice(85, 10)

# 抓取纬度/经度值（GFS为1D）
lats = ds.lat.sel(lat=lat_slice).values
lons = ds.lon.sel(lon=lon_slice).values

# 使用nine-point滤波器抓取数据并平滑处理50次以获取天气信号
level = 850 * units.hPa
hght_850 = mpcalc.smooth_n_point(ds['Geopotential_height_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze(), 9, 50)
tmpk_850 = mpcalc.smooth_n_point(ds['Temperature_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze(), 9, 25)
uwnd_850 = mpcalc.smooth_n_point(ds['u-component_of_wind_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze(), 9, 50)
vwnd_850 = mpcalc.smooth_n_point(ds['v-component_of_wind_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze(), 9, 50)

# 将温度转换为摄氏度以进行绘图
tmpc_850 = tmpk_850.to('degC')

# 获取合理的日期时间格式
vtime = ds.time.data[0].astype('datetime64[ms]').astype('O')

# 计算数据的网格间距
dx, dy = mpcalc.lat_lon_grid_deltas(lons, lats)

# 计算Q矢量分量
uqvect, vqvect = mpcalc.q_vector(uwnd_850, vwnd_850, tmpk_850, 850*units.hPa, dx, dy)

# 计算上面计算的Q矢量的散度
q_div = -2*mpcalc.divergence(uqvect, vqvect, dx, dy, dim_order='yx')

# 设置地图投影（如何显示数据）
mapcrs = ccrs.LambertConformal(
    central_longitude=-100, central_latitude=35, standard_parallels=(30, 60))

# 设置数据项目（GFS为经/纬格式）
datacrs = ccrs.PlateCarree()

# 启动图形并设置范围以仅显示较小的图形区域
fig = plt.figure(1, figsize=(14, 12))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-130, -72, 20, 55], ccrs.PlateCarree())

# 添加地图要素以绘制海岸线和州界
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

# 绘制850-hPa Q矢量散度和比例
clevs_850_tmpc = np.arange(-40, 41, 2)
clevs_qdiv = list(range(-30, -4, 5))+list(range(5, 31, 5))
cf = ax.contourf(lons, lats, q_div*1e18, clevs_qdiv, cmap=plt.cm.bwr,
                 extend='both', transform=datacrs)
cb = plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50, extendrect=True,
                  ticks=clevs_qdiv)
cb.set_label('Q-Vector Div. (*10$^{18}$ m s$^{-1}$ kg$^{-1}$)')

# 绘制850-hPa温度
csf = ax.contour(lons, lats, tmpc_850, clevs_850_tmpc, colors='grey',
                 linestyles='dashed', transform=datacrs)
plt.clabel(csf, fmt='%d')

# 绘制850-hPa地势高度
clevs_850_hght = np.arange(0, 8000, 30)
cs = ax.contour(lons, lats, hght_850, clevs_850_hght, colors='black', transform=datacrs)
plt.clabel(cs, fmt='%d')

# 绘制850-hPa Q矢量，缩放以获得漂亮的大小箭头
wind_slice = (slice(None, None, 5), slice(None, None, 5))
ax.quiver(lons[wind_slice[0]], lats[wind_slice[1]],
          uqvect[wind_slice].m,
          vqvect[wind_slice].m,
          pivot='mid', color='black',
          scale=1e-11, scale_units='inches',
          transform=datacrs)

# 添加标题
plt.title('850-hPa GFS Geo. Heights (m), Temp (C),'
          ' and Q-Vectors (m$^2$ kg$^{-1}$ s$^{-1}$)', loc='left')
plt.title('Valid Time: {}'.format(vtime), loc='right')
plt.show()