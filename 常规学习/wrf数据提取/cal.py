import numpy as np
from datetime import datetime
from netCDF4 import Dataset
import nearest_data
import sele_station_data
import data_cal
import wrf_data


layer,year,month,day = '02','2020','01','01'
path = 'data/wrfout_d{0}_{1}-{2}-{3}_00_00_00'.format(layer,year,month,day)
data = wrf_data.wrf_data(path)
l = sele_station_data.station_lon_lat('呼和浩特')
ind=nearest_data.nearest_position(float(l[1]) , float(l[2]),data[1], data[2],data[0])
print(ind)
station_data = []
for i in range(24):
    station_data.append(data_cal.station(str(int(l[0])),year,str(int(month)),str(int(day)),str(i)))
print(station_data)