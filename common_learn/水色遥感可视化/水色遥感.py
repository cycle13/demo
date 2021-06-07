import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import cmaps



#read nc dataset
obj=nc.Dataset('data/A201006.L3m_MO_SST_sst_4km.nc')


#read variables
lat = obj.variables['lat'][:]
lon = obj.variables['lon'][:]
sst = obj.variables['sst'][:]


latindex = np.arange(len(lat))
lonindex = np.arange(len(lon))
latindex2 = np.max(latindex[lat >= 12])
latindex22 = np.min(latindex[lat <= 24])
lonindex2 = np.min(lonindex[lon >= 105])
lonindex22 = np.min(lonindex[lon >= 122])

#Extract  scope of variable
sst2 = sst[latindex22:latindex2, lonindex2:lonindex22]
sst3 = sst2[::-1, :]
lat2 = lat[latindex22:latindex2]
lat2 = lat2[::-1]
lon2 = lon[lonindex2:lonindex22]

#set grid
x, y = np.meshgrid(lon2, lat2)

#basemap
m = Basemap(projection = 'cyl',llcrnrlat = 12,urcrnrlat = 24,llcrnrlon = 105,urcrnrlon = 122,resolution='l')

fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
im = m.pcolormesh(x, y, sst3, vmin = 24, vmax = 33, shading='flat',cmap = cmaps.BkBlAqGrYeOrReViWh200,latlon=True)

m.fillcontinents(color='grey')
m.drawparallels(np.arange(12.,24.,4.),labels=[1,0,0,0]) # draw parallels
m.drawmeridians(np.arange(105.,122.,4.),labels=[0,0,0,1]) # draw meridians
m.drawcoastlines()
m.drawcountries()



#set sclae of colorbar
cbar = m.colorbar(im)
cbar.set_clim(24,33)
cbar.set_ticks(np.linspace(24,32,9))
cbar.set_ticklabels(('24', '26', '27','28','29','30','31','32','32'))

#add title
plt.title('SST')

#output.nc
plt.savefig('county_image/sst.png', dpi=100, bbox_inches='tight')

plt.show()