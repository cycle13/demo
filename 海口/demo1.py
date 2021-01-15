import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
data = Dataset('data/gistemp250.nc')
from netCDF4 import date2index
from datetime import datetime
timeindex = date2index(datetime(2020,1,15),data.variables['time'])


lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
lon,lat = np.meshgrid(lon,lat)
temp_anomaly = data.variables['tempanomaly'][timeindex]
fig = plt.figure(figsize=(10,8))
m = Basemap(projection = 'lcc',resolution = 'c',width = 8E6,height = 8E6,lat_0 = 19,lon_0 = 119)
m.shadedrelief(scale = 0.5)
m.pcolormesh(lon,lat,temp_anomaly,latlon=True,cmap='RdBu_r')
plt.clim(-8,8)
plt.rcParams['font.sans-serif'] = ['SimHei']
m.drawcoastlines(color='lightgray')
plt.title('海口市地表温度')
plt.colorbar(label='temperature anomaly (度 C)')
plt.show()