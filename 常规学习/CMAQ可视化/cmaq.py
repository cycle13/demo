from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
import maskout
import imageio
# from moviepy.editor import ImageSequenceClip
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



data = Dataset(r'data/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_20210131.nc', mode='r')
data1 = pd.read_csv('data/Export_Output_7.csv',encoding='utf-8')
ROW = data.dimensions['ROW'].size
COL = data.dimensions['COL'].size
lon = []
lat = []

for i in range(ROW):
    xl = []
    yl = []
    for j in range(COL):
        xl.append(data1['lons'][i*COL+j])
        yl.append(data1['lats'][i*COL+j])

    lon.append(xl)
    lat.append(yl)


# 确定纬度的计算方式，偏差较大
# ROW = data.dimensions['ROW'].size
# COL = data.dimensions['COL'].size
# XCELL = data.XCELL/1000
# YCELL = data.YCELL/1000
# XCEN = data.XCENT
# YCEN = data.YCENT
# XLON = XCELL*COL/(2*111)
# YLON = YCELL*ROW /(2*111*np.cos(YCEN))
# lons = np.linspace(XCEN-XLON,XCEN+XLON,COL)
# lats = np.linspace(YCEN-YLON,YCEN+YLON,ROW)

# # 动态计算经纬度
# ROW = data.dimensions['ROW'].size
# COL = data.dimensions['COL'].size
# XCELL = data.XCELL/1000
# YCELL = data.YCELL/1000
# XCEN = data.XCENT
# YCEN = data.YCENT
# s = (np.pi/18)*6371
# YLON = (YCELL*(ROW/2))/s
# latt = []
# for i in range(ROW):
#     latt.append((YCEN-YLON)+i*(2*YLON)/ROW)
# lons = []
# for k in latt:
#     xl = []
#     XLON = XCELL * COL / (2 * s * np.cos(k))
#     for i in range(COL):
#         xl.append((XCEN - XLON)+i*(2*XLON)/COL)
#     lons.append(xl)
# lats = []
# for j in range(COL):
#     lats.append(latt)




# lon, lat = np.meshgrid(lons, lats)
#
PM25AC = data.variables['PM25AC'][2][0]
# print(data.variables['PM25AC'])
# print(len(lon),len(lat),np.shape(PM25AC))
pb = PM25AC
fig = plt.figure(figsize=(10,5))


ax = plt.axes(projection=ccrs.PlateCarree())
cf = plt.contourf(lon,lat, pb,transform=ccrs.PlateCarree(),cmap="jet")
ax.set_xticks(np.arange(110,115,1),crs = ccrs.PlateCarree())    # x轴
ax.set_yticks(np.arange(34,41,1),crs = ccrs.PlateCarree())
cb=fig.colorbar(cf,shrink=0.8)
cb.set_label("单位："+r"$\rm \mu g \cdot m^{-3}$",fontsize=10)
cb.ax.tick_params(direction='out',length=5)
plt.title('PM2.5浓度',fontsize=12)
# clip = maskout.shp2clip(cf,ax,r'shanxi/shanxi.shp',1)
shpname = r'shanxi3/Export_Output_5.shp'
# shpname = r'sx_shp/county_pophu.shp'
adm1_shapes=list(shpreader.Reader(shpname).geometries())
ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
# plt.show()
plt.savefig('pic/1.png')
