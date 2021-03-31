from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
import os
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import demo
import matplotlib.cm as cm
import datetime
import matplotlib.colors as col
import maskout
import make_pic
import data_cal
# from moviepy.editor import ImageSequenceClip
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

for x in list(pd.date_range(start='2021-01-31', end='2021-02-02')):
    dt = x.strftime('%Y%m%d')
    # dir = r'/disk/Build_WRF/CMAQ_DATA/output.'+dt
    dir = r'data'
    dir1 = dir+r'/CCTM_ACONC_v531_gcc9.1.0_Bench_2020_SX_'+dt+'.nc'
    dir2 = dir+r'/CCTM_APMDIAG_v531_gcc9.1.0_Bench_2020_SX_'+dt+'.nc'
    data = Dataset(dir2, mode='r')
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

    numlevel = {'PM25':[0.00000000001,35,75,115,150,250,350],'PM10':[0.00000000001,50,150,250,350,420,500],'SO2':[0.00000000001,50,150,475,800,1600,2100],'NO2':[0.00000000001,40,80,180,280,565,750],'O3':[0.00000000001,100,160,215,265,800,1000]}


    level = ['PM25','PM10','SO2','NO2','O3']

    for i in range(num):
        PM25 = data_cal.data(i,dir1,dir2)
        for j in range(len(PM25)):
            pb = PM25[j]
            xls = level[j]
            # 保存到csv
            # ns = pd.DataFrame(pb)
            # ns.to_csv(xls + '_' + str(i) + '.csv')
            maxx = np.max(PM25)
            minx = np.min(PM25)
            print(maxx)
            proj = ccrs.LambertConformal(central_latitude=37.75, central_longitude=112.35)
            fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection=proj))  # 建立页面
            ax.set_extent([110, 114.5, 34.5, 41], ccrs.PlateCarree())  # 设置经纬度范围
            # yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=3 * i)).strftime("%Y/%m/%d/%H/")
            yestodayl = (datetime.datetime(2021,1,31) + datetime.timedelta(hours=3*i)).strftime("%Y/%m/%d/%H/")
            color1 = '#00E400'  # 优
            color2 = '#FFFF00'  # 良
            color3 = '#FF7E00'  # 轻
            color4 = '#FF0000'  # 中
            color5 = '#99004C'  # 重
            color6 = '#7E0023'  # 严重
            cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3, color4, color5, color6])
            cm.register_cmap(cmap=cmap2)
            # levels = np.array([0.00000000001, 35, 75, 115, 150, 250, 350])
            levels = np.array(numlevel[xls])
            cf = plt.contourf(lon,lat, pb,transform=ccrs.PlateCarree(),cmap=cm.get_cmap('own2'), levels=levels)
            # cf = plt.contourf(lon, lat, pb, transform=ccrs.PlateCarree(), cmap="jet", levels=levels)
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
            fig.text(0.71, 0.30, '佳华科技生态环境研究院', fontsize=40, rotation=45, color='gray', ha='right', va='bottom', alpha=0.4)
            plt.title('山西省'+yestodayl[0:4]+'年'+yestodayl[5:7]+'月'+yestodayl[8:10]+'日'+yestodayl[11:13]+'时'+'{}浓度'.format(xls),fontsize=12)
                # clip = maskout.shp2clip(cf,ax,r'shanxi/shanxi.shp',1)
            shpname = r'shanxi3/Export_Output_5.shp'
            adm1_shapes=list(shpreader.Reader(shpname).geometries())
            ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
            # plt.show()
            if not os.path.exists('pic/{0}/{1}'.format(xls,dt)):
                os.makedirs('pic/{0}/{1}'.format(xls,dt))
            plt.savefig('pic/{0}/{1}/{2}.png'.format(xls,dt,str(i)))
            plt.close('all')


    for k in level:
        img_names = ['pic/{0}/{1}'.format(k,dt)+'/'+str(i)+'.png' for i in range(0,num)]
        if not os.path.exists('gif/{}'.format(k)):
            os.makedirs('gif/{}'.format(k))
        make_pic.create_gif(img_names,'gif/{}/山西省{}.gif'.format(k,dt), duration=0.5)
