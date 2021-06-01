#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 15:18
# @Author  : Yanjun Wang
# @Site    : 
# @File    : down.py
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
mytime = datetime.strptime('2021-05-27T00:00:00Z','%Y-%m-%dT%H:%M:%Sz')
query.lonlat_box(north=55, south=0, east=140, west=70).time(mytime)
# query.lonlat_box(north=55, south=0, east=140, west=70)
# query.all_times()
print(query.variables)
query.variables('Geopotential_height_isobaric','Temperature_isobaric',
                'u-component_of_wind_isobaric','v-component_of_wind_isobaric')
query.accept('netcdf4')
nc = ncss.get_data(query)
data = xr.open_dataset(NetCDF4DataStore(nc))
data.to_netcdf('work/GFS_2021052501.nc','w')

