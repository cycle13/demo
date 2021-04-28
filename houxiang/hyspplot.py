import os
import pandas as pd
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
from matplotlib.collections import LineCollection
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


fn = os.path.join('D:\Program Files\pycharm\houxiang\Temp\HYSPLIT', 'traj_20210426.txt')
fs = open(fn,'r')
fl = fs.read()
fl = fl.replace('  ',',')
fl = fl.replace(',,',',')
fl = fl.replace(',,',',')
fs.close()
path = os.path.join('D:\Program Files\pycharm\houxiang\Temp\HYSPLIT', 'anc.txt')
fobj = open(path,'w')
fobj.write(fl)
fobj.close()
h100 = pd.DataFrame()
h500 = pd.DataFrame()
h1000 = pd.DataFrame()
f = pd.read_table(path,skiprows=7,sep=',', names=['na','ID','b','year','month','day','hour','a','c','bac_hour','lat','lon','height','pah','message'])
f= f.drop('na', 1)
for i in range(len(f)):
    x = f.loc[[i]]
    if i%3==0:
        h100 = pd.concat([h100,x])
    elif i%3==1:
        h500 = pd.concat([h500,x])
    elif i%3==2:
        h1000 = pd.concat([h1000,x])
#地图设置
proj = ccrs.PlateCarree(central_longitude=105)
leftlon, rightlon, lowerlat, upperlat = (70,135,18,55)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
lon_formatter = cticker.LongitudeFormatter()
lat_formatter = cticker.LatitudeFormatter()
fig = plt.figure(figsize=(10,10))
f_ax = fig.add_axes([0.1, 0.3, 0.8, 0.6],projection = proj)
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
# color1 = '#00E400'
# color3 = '#FF7E00'
# color6 = '#7E0023'

color1 = 'green'
color3 = 'blue'
color6 = 'red'
cmap1 = col.LinearSegmentedColormap.from_list('own1', [color1,color1])
cm.register_cmap(cmap=cmap1)
cmap2 = col.LinearSegmentedColormap.from_list('own2', [color3,color3])
cm.register_cmap(cmap=cmap2)
cmap3 = col.LinearSegmentedColormap.from_list('own3', [color6,color6])
cm.register_cmap(cmap=cmap3)
h = h100['height']
points = np.array([h100['lon'], h100['lat']]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
#设置颜色线条
lc = LineCollection(segments, cmap=cm.get_cmap('own1'), color = color1,transform=ccrs.PlateCarree(),label = '100m')
lc.set_array(h)
f_ax.add_collection(lc)
h = h500['height']
points = np.array([h500['lon'], h500['lat']]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
#设置颜色线条
lc = LineCollection(segments, cmap=cm.get_cmap('own2'), color = color3,transform=ccrs.PlateCarree(),label = '500m')
lc.set_array(h)
f_ax.add_collection(lc)
h = h1000['height']
points = np.array([h1000['lon'], h1000['lat']]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
#设置颜色线条
lc = LineCollection(segments, cmap=cm.get_cmap('own3'), color = color6,transform=ccrs.PlateCarree(),label = '1000m')
lc.set_array(h)
#绘制线条
f_ax.add_collection(lc)
f_ax.scatter(h100['lon'][0], h100['lat'][0],color = 'black', s=10)
plt.title(str(h100['year'][0])+'年'+str(h100['month'][0])+'月'+str(h100['day'][0])+'日'+str(h100['hour'][0])+'时的'+str(int(h1000['bac_hour'][len(f)-1]))+'小时后向轨迹图')
plt.legend()
# f_ax = fig.add_axes([0.1, 0.5, 0.8, 0.4],projection = proj)
ff_ax = fig.add_axes([0.1, 0.1, 0.8, 0.22])
axx = range(-len(h100)+1,1)
ff_ax.plot(axx,h100['height'],color=color1)
ff_ax.plot(axx,h500['height'],color=color3)
ff_ax.plot(axx,h1000['height'],color=color6)
td = []
for i in range(len(h100['hour'])):
    l = str(h100['day'].tolist()[i]).replace(' ','') + '日' +str(h100['hour'].tolist()[i]).replace(' ','')+ '时'
    td.append(l)
plt.xticks(axx, td, rotation=60)
plt.xlabel('时间')
plt.ylabel('高度：m')
plt.savefig('aaa.png')
plt.show()