from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import imageio
# from moviepy.editor import ImageSequenceClip
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import maskout


data = Dataset('data/wrfout_d03_2021-02-18_00_00_0', mode='r')
lons = data.variables['XLONG'][0]
lats = data.variables['XLAT'][0]
lon, lat = np.meshgrid(lons, lats)
for i in range(0,24):
    # pb = data.variables['PB'][2][28][122][158]
    pb = data.variables['PBLH'][i]
    print(len(lons),len(lats))
    print(pb)
    fig = plt.figure(figsize=(9,5))
    ax = plt.axes(projection=ccrs.PlateCarree())
    cf = plt.contourf(lons, lats, pb,transform=ccrs.PlateCarree())
    ax.set_xticks(np.arange(111.5,113,0.5),crs = ccrs.PlateCarree())    # x轴
    ax.set_yticks(np.arange(37.5,38.5,0.5),crs = ccrs.PlateCarree())
    cb=fig.colorbar(cf,shrink=0.8)
    cb.set_label("单位：Pa",fontsize=15)
    cb.ax.tick_params(direction='out',length=5)
    plt.title('平均气压',fontsize=16)
    clip = maskout.shp2clip(cf,ax,r'lact/taiyuan.shp',0)
    shpname = r'lact/taiyuan.shp'
    adm1_shapes=list(shpreader.Reader(shpname).geometries())
    ax.add_geometries(adm1_shapes[:],ccrs.PlateCarree(),edgecolor='k',facecolor='')
    plt.savefig('county_image/{0}.png'.format(str(i)))
    # plt.show()

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


img_names = ['county_image/'+str(i)+'.png' for i in range(0,24)]
print(img_names)
create_gif(img_names,'county_image/太原市气压图.gif', duration=1.0)
