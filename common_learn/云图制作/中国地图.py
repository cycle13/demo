import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


with open('data/CN-border-La.dat') as src:
    context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]

# Set figure size
fig = plt.figure(figsize=[10, 8])
# Set projection and plot the main figure
ax = plt.axes(projection=ccrs.LambertConformal(central_latitude=90,
                                               central_longitude=105))
# Add ocean, land, rivers and lakes
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.RIVERS.with_scale('50m'))
ax.add_feature(cfeature.LAKES.with_scale('50m'))
# Plot border lines
for line in borders:
    ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
            transform=ccrs.Geodetic())
# Plot gridlines
ax.gridlines(linestyle='--')
# Set figure extent
ax.set_extent([80, 130, 13, 55])

# Plot South China Sea as a subfigure
sub_ax = fig.add_axes([0.741, 0.11, 0.14, 0.155],
                      projection=ccrs.LambertConformal(central_latitude=90,
                                                       central_longitude=115))
# Add ocean, land, rivers and lakes
sub_ax.add_feature(cfeature.OCEAN.with_scale('50m'))
sub_ax.add_feature(cfeature.LAND.with_scale('50m'))
sub_ax.add_feature(cfeature.RIVERS.with_scale('50m'))
sub_ax.add_feature(cfeature.LAKES.with_scale('50m'))
# Plot border lines
for line in borders:
    sub_ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                transform=ccrs.Geodetic())
# Set figure extent
sub_ax.set_extent([105, 125, 0, 25])

with open('data/1st-tecmap.dat') as src:
    data = [line for line in src if not line.endswith('LAT/LON1/LON2/DLON/H\n')]
    print(data)
    tec = np.fromstring(''.join(data), dtype=float, sep=' ')
    print(tec)

# Generate a geodetic grid
nlats, nlons = 71, 73

lats = np.linspace(0, 60, nlats)
lons = np.linspace(60, 140, nlons)
lons, lats = np.meshgrid(lons, lats)

tec.shape = nlats, nlons
print(tec)
# fig = plt.figure(figsize=(16, 6))
# Set projection
# ax = plt.axes(projection=ccrs.PlateCarree())
# Plot contour
cp = ax.contourf(lons, lats, tec, transform=ccrs.PlateCarree(), cmap=plt.cm.jet)
ax.coastlines()
ax.gridlines(linestyle='--', draw_labels=True)
# Add a color bar
plt.colorbar(cp)
# Show figure
plt.show()