import numpy as np
import os
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import pandas as pd
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import demo
import cartopy.feature as cfeat


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


proj= ccrs.PlateCarree()  # 简写投影
fig = plt.figure(figsize=(10,10))
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 创建子图
extent=[70, 135, 15, 55]#限定绘图范围
ax.set_extent(extent,crs=proj)
ax.set_xticks(np.arange(extent[0],extent[1]+1,3),crs=proj)
ax.set_yticks(np.arange(extent[-2],extent[-1]+1,2),crs=proj)



def get_file_path(root_path, file_list, dir_list):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)


root_path = r"data"
file_list = []
dir_list = []
get_file_path(root_path, file_list, dir_list)
for i in file_list:
    df = pd.read_csv(i,skiprows=1)
    print(df)
    plt.scatter(df['Lon'].values,df['Lat'].values,marker='o',s=0.5,color ="r")
    fig.canvas.draw()

olon=list(range(-180, 180, 10))
olat=list(range(-90, 90, 10))
ax.xaxis.set_major_formatter(LONGITUDE_FORMATTER)
ax.yaxis.set_major_formatter(LATITUDE_FORMATTER)
demo.lambert_xticks(ax, olon)
demo.lambert_yticks(ax, olat)
shpname = r'lact/中国.shp'
adm1_shapes=list(shpreader.Reader(shpname).geometries())
ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
left, bottom, width, height = 0.13, 0.27, 0.1, 0.12
ax2 = fig.add_axes([left, bottom, width, height],projection=ccrs.PlateCarree())
provinces = cfeat.ShapelyFeature(shpreader.Reader(shpname).geometries(),ccrs.PlateCarree(),edgecolor='k',facecolor='gray',)
ax2.add_feature(provinces, linewidth=0.6, zorder=2)
ax2.set_extent([105, 125, 0, 25], crs=ccrs.PlateCarree())
plt.savefig('123.png')
plt.show()


