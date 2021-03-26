from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import demo
import matplotlib.cm as cm
import datetime
import matplotlib.colors as col
import maskout
import make_pic
# from moviepy.editor import ImageSequenceClip
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



data = Dataset(r'data/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_20210321.nc', mode='r')
data1 = pd.read_csv('data/Export_Output_7.csv',encoding='utf-8')
ROW = data.dimensions['ROW'].size
COL = data.dimensions['COL'].size
num = len(data.variables['PM25AC'])
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



for i in range(num):
    PM25 = data.variables['PM25AC'][i][0]+data.variables['PM25AT'][i][0]+data.variables['PM25CO'][i][0]
    pb = PM25
    maxx = np.max(PM25)
    minx = np.min(PM25)
    proj = ccrs.LambertConformal(central_latitude=37.75, central_longitude=112.35)
    fig, ax = plt.subplots(figsize=(5, 10), subplot_kw=dict(projection=proj))  # 建立页面
    ax.set_extent([110, 114.5, 34.5, 41], ccrs.PlateCarree())  # 设置经纬度范围
    yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=3*i)).strftime("%Y/%m/%d/%H/")
    color1 = '#00E400'  # 优
    color2 = '#FFFF00'  # 良
    color3 = '#FF7E00'  # 轻
    color4 = '#FF0000'  # 中
    color5 = '#99004C'  # 重
    color6 = '#7E0023'  # 严重
    cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3, color4, color5, color6])
    cm.register_cmap(cmap=cmap2)
    # levels = np.array([0.00000000001, 35, 75, 115, 150, 250, 350])
    levels = np.array([0.00000000001, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    # cf = plt.contourf(lon,lat, pb,transform=ccrs.PlateCarree(),cmap=cm.get_cmap('own2'), levels=levels)
    cf = plt.contourf(lon, lat, pb, transform=ccrs.PlateCarree(), cmap="jet", levels=levels)
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
    plt.title('太原市'+yestodayl[0:4]+'年'+yestodayl[5:7]+'月'+yestodayl[8:10]+'日'+yestodayl[11:13]+'时'+'PM2.5浓度',fontsize=12)
        # clip = maskout.shp2clip(cf,ax,r'shanxi/shanxi.shp',1)
    shpname = r'shanxi3/Export_Output_5.shp'
    adm1_shapes=list(shpreader.Reader(shpname).geometries())
    ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
    # plt.show()
    plt.savefig('pic/{0}.png'.format(str(i)))



img_names = ['pic/'+str(i)+'.png' for i in range(0,num)]
make_pic.create_gif(img_names,'pic/山西省PM25.gif', duration=0.5)
