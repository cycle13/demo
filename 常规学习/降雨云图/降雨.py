import numpy as np
import pandas as pd
from scipy.interpolate import Rbf  # 径向基函数 ： 将站点信息插到格点上 用于绘制等值线

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib as mpl

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter

import maskout  #只显示某个地区

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


# 数据准备
df = pd.read_excel('工作簿1.xlsx') #读取Excel
df.columns = ['stid','lon','lat','height','rain']
# df = df[(df['rain']>0)&(df['lat']>35)&(df['lon']>115)&(df['lat']<50)&(df['lon']<130)]  #筛选坐标在某个范围内，由于数据量少，直接在EXCEL中做处理
lon = df['lon']
lat = df['lat']
rain = df['rain']


# 绘图准备
olon = np.linspace (125,131,120) #经纬坐标，0.05°分辨率 118°到126°0.05分辨率是有160个格点
olat = np.linspace (44,47,60) #纬度坐标，0.05°分辨率
olon,olat = np.meshgrid(olon,olat) #生成坐标网格 meshgrid网格化
func = Rbf(lon,lat,rain,function='linear') #插值函数 调用Rbf插值函数中的 cubic 插值法linear
rain_data_new = func(olon,olat) #插值
rain_data_new[rain_data_new <0 ] = 0


#画布及绘图声明
fig = plt.figure(figsize = (16,9.6),facecolor = '#666666',edgecolor = 'Blue',frameon = False)  # 画布
ax = fig.add_subplot(111,projection=ccrs.PlateCarree()) #绘图区

#色彩定制：24小时降水量级色标
clevs = [0.1,10.,25.,50.,100.,250.,500] #自定义颜色列表
cdict = ['#A9F090','#40B73F','#63B7FF','#0000FE','#FF00FC','#850042'] #自定义颜色列表 '#A9F090','#40B73F','#63B7FF','#0000FE','#FF00FC','#850042'
my_cmap = colors.ListedColormap(cdict) # 自定义颜色映射 color-map
norm = mpl.colors.BoundaryNorm(clevs,my_cmap.N) # 基于离散区间生成颜色映射索引
#  绘制等值线、等值线填色
cf = ax.contourf(olon,olat,rain_data_new,clevs,transform = ccrs.PlateCarree(),cmap=my_cmap,norm = norm)
# ct = ax.contour(olon,olat,rain_data_new,clevs)   # 绘制等值线
# clabel = ax.clabel(ct,fmt = '%i')
position = fig.add_axes([0.82,0.2,0.05,0.2]) #位置【左，下，宽。高】
plt.colorbar(cf,cax=position)     # 颜色参照表
position.set_yticklabels((0,10,25,50,100,250,500))
ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=True))
ax.yaxis.set_major_formatter(LatitudeFormatter())
ax.set_xticks(np.arange(125,131,2),crs = ccrs.PlateCarree())    # x轴
ax.set_yticks(np.arange(44,47,2),crs = ccrs.PlateCarree())      # y轴
# ax.gridlines()  #显示背景线

# # # #裁切
# clip = maskout.shp2clip(cf,ax,'haerbin/hrb.shp',420000)
clip = maskout.shp2clip(cf,ax,'haerbin/黑龙江省_地级市行政边界.shp','哈尔滨市') #haerbin/shijie.shp  shp/黑龙江省/市界.shp

#从全国实际地图中获取辽宁省的市级边界并加载
shpname = r'haerbin/黑龙江省_地级市行政边界.shp'  # shp/country1.shp
adm1_shapes=list(shpreader.Reader(shpname).geometries())
ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='') #36:72东三省
plt.show()
plt.savefig('111.png')