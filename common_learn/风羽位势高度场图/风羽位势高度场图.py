import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter
datav=nc.Dataset('data/wndz500.nc')
datau=nc.Dataset('data/wndz500.nc')
g500=nc.Dataset('data/wndz500.nc')
time=datau.variables['time'][:]
vwnd=datav.variables['v'][1,60:200,180:350]
uwnd=datau.variables['u'][1,60:200,180:350]
lon=datau.variables['longitude'][180:350]
lat=datau.variables['latitude'][60:200]
geo500=g500.variables['z'][1,60:200,180:350]
geo500=geo500/10
LON,LAT=np.meshgrid(lon,lat)
fig=plt.figure(figsize=(12,6))
ax=plt.axes([0.1,0.1,0.8,0.8],projection=ccrs.PlateCarree())
chinamap=shpreader.Reader('data/bou2_4l.shp').geometries()#读取地图数据
ax.set_extent([80,135,15,50], crs=ccrs.PlateCarree())#设置绘图范围
ax.add_geometries(chinamap, ccrs.PlateCarree(),facecolor='none', edgecolor='black')#设置边界样式
ax.coastlines('50m')#添加海岸线
vmin=5000
vmax=5900
n=(vmax-vmin)/30
n=int(n)
levels = np.linspace(vmin, vmax,n+1)
cont=ax.contourf(LON,LAT,geo500[:,:],alpha=0.6,color='b',levels=levels,cmap='jet',transform=ccrs.PlateCarree())
ax.barbs(LON, LAT, uwnd, vwnd, pivot='middle',
         color='black', regrid_shape=12,  transform=ccrs.PlateCarree())#风羽图
#aui=plt.quiver(LON[::2,::2],LAT[::2,::2],uwnd[::2,::2],vwnd[::2,::2],scale=45,scale_units='inches',transform=ccrs.PlateCarree())
#plt.quiverkey(aui,0.9,1.05,45,'45m/s',labelpos='E')#设置箭头属性
ax.set_xticks(np.arange(80,135,5),crs=ccrs.PlateCarree())
#后面是为了坐标轴符合位置要求
ax.set_yticks(np.arange(15,51,5),crs=ccrs.PlateCarree())
lon_formatter=LongitudeFormatter(number_format='.0f',degree_symbol='°',dateline_direction_label=True)
lat_formatter=LatitudeFormatter(number_format='.0f',degree_symbol='°')
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
cb=fig.colorbar(cont,shrink=0.8)
cb.set_label("geopotential meter",fontsize=15)
cb.ax.tick_params(direction='out',length=5)
plt.clabel(cont, inline=True, colors=['k'], fmt='%1.0f')
plt.title('Mean 500hPa Wind and 500hPa height for Jan 2008',fontsize=16)
