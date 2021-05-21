#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 15:53
# @Author  : Yanjun Wang
# @Site    : 
# @File    : data_down.py
# @Software: PyCharm

from siphon.catalog import TDSCatalog

from datetime import datetime, timedelta
from xarray.backends import NetCDF4DataStore
import xarray as xr
import shutil
import metpy
import xarray as xr



best_gfs = TDSCatalog('http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/'
                      'Global_0p25deg/catalog.xml?dataset=grib/NCEP/GFS/Global_0p25deg/Best')
best_ds = list(best_gfs.datasets.values())[0]
ncss = best_ds.subset()
query = ncss.query()
mytime = datetime.strptime('2021-05-25T00:00:00Z','%Y-%m-%dT%H:%M:%Sz')
query.lonlat_box(north=55, south=0, east=140, west=70).time(mytime)
print(query.variables)
query.variables('Temperature_surface','Dewpoint_temperature_height_above_ground',
                'Relative_humidity_height_above_ground','Temperature_tropopause')
query.accept('netcdf4')
nc = ncss.get_data(query)
data = xr.open_dataset(NetCDF4DataStore(nc))
data.to_netcdf('GFS_2021052500.nc','w')
shutil.move('GFS_2021052500.nc','./work')

