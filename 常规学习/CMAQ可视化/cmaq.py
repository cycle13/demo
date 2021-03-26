from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import demo
import matplotlib.cm as cm
import matplotlib.colors as col
import maskout
import imageio
# from moviepy.editor import ImageSequenceClip
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



data = Dataset(r'data/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_20210321.nc', mode='r')
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
# for i in range(71):
PM25 = data.variables['PM25AC'][1][0]+data.variables['PM25AT'][1][0]+data.variables['PM25CO'][1][0]
pb = PM25
maxx = np.max(PM25)
minx = np.min(PM25)
proj = ccrs.LambertConformal(central_latitude=37.75, central_longitude=112.35)
fig, ax = plt.subplots(figsize=(5, 10), subplot_kw=dict(projection=proj))  # 建立页面
ax.set_extent([110, 114.5, 34.5, 41], ccrs.PlateCarree())  # 设置经纬度范围

color1 = '#00E400'  # 优
color2 = '#FFFF00'  # 良
color3 = '#FF7E00'  # 轻
color4 = '#FF0000'  # 中
color5 = '#99004C'  # 重
color6 = '#7E0023'  # 严重
cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3, color4, color5, color6])
cm.register_cmap(cmap=cmap2)
levels = np.array([0.00000000001, 35, 75, 115, 150, 250, 350])
cf = plt.contourf(lon,lat, pb,transform=ccrs.PlateCarree(),cmap=cm.get_cmap('own2'), levels=levels)
plt.scatter(112, 37, marker='o', s=6, color="k")
fig.canvas.draw()
xticks = list(range(-180, 180, 1))
yticks = list(range(-90, 90, 1))
ax.gridlines(xlocs=xticks, ylocs=yticks, linewidth=1, linestyle='--',color = 'r')
ax.xaxis.set_major_formatter(LONGITUDE_FORMATTER)
ax.yaxis.set_major_formatter(LATITUDE_FORMATTER)
demo.lambert_xticks(ax, xticks)
demo.lambert_yticks(ax, yticks)
cb=fig.colorbar(cf,ax=ax,pad=0.1)
cb.set_label("单位："+r"$\rm \mu g \cdot m^{-3}$",fontsize=10)
cb.ax.tick_params(direction='out',length=5)
plt.title('PM2.5浓度',fontsize=12)
    # clip = maskout.shp2clip(cf,ax,r'shanxi/shanxi.shp',1)
shpname = r'shanxi3/Export_Output_5.shp'
    # shpname = r'sx_shp/county_pophu.shp'
adm1_shapes=list(shpreader.Reader(shpname).geometries())
ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
plt.show()
# plt.savefig('pic/{0}.png'.format(str(i)))



def create_gif(image_list, gif_name, duration = 1.0):
    '''
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

#
# img_names = ['pic/'+str(i)+'.png' for i in range(0,71)]
# print(img_names)
# create_gif(img_names,'pic/山西省PM25.gif', duration=0.5)
