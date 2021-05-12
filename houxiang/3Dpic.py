import os
import pandas as pd
import shapefile
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import numpy as np
from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import random
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


fn = os.path.join('D:\Program Files\pycharm\houxiang\Temp\HYSPLIT', 'traj_20210507.txt')
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

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(h100['lon'],h100['lat'],h100['height'],'g',label = '100m')
ax.plot(h500['lon'],h500['lat'],h500['height'],'b',label = '500m')
ax.plot(h1000['lon'],h1000['lat'],h1000['height'],'r',label = '1000m')
ax.set_xlabel('经度')
ax.set_ylabel('纬度')
ax.set_zlabel('高度：m')
ax.plot(h100['lon'],h100['lat'],'g--',label = '100m投影')
ax.plot(h500['lon'],h500['lat'],'b--',label = '500m投影')
ax.plot(h1000['lon'],h1000['lat'],'r--',label = '1000m投影')
plt.legend()
china = shapefile.Reader('data/bou2_4l.dbf')
for shape_rec in china.shapeRecords():
    lon = []
    lat = []
    for k in shape_rec.shape.points:
        lon.append(k[0])
        lat.append(k[1])
    ax.plot(lon,lat,'black')
plt.savefig('zaaa.png')
plt.show()