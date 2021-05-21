import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Read VTEC data from a file
with open('data/1st-tecmap.dat') as src:
    data = [line for line in src if not line.endswith('LAT/LON1/LON2/DLON/H\n')]
    tec = np.fromstring(''.join(data), dtype=float, sep=' ')

# Generate a geodetic grid
nlats, nlons = 71, 73

lats = np.linspace(0, 60, nlats)
lons = np.linspace(60, 140, nlons)
lons, lats = np.meshgrid(lons, lats)

tec.shape = nlats, nlons

fig = plt.figure(figsize=(16, 6))
# Set projection
ax = plt.axes(projection=ccrs.PlateCarree())
# Plot contour
cp = ax.contourf(lons, lats, tec, transform=ccrs.PlateCarree(), cmap=plt.cm.jet)
ax.coastlines()
ax.gridlines(linestyle='--', draw_labels=True)
# Add a color bar
plt.colorbar(cp)

plt.show()