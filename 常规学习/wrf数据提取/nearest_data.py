import numpy as np
import dp_temp
from netCDF4 import Dataset


def nearest_position( stn_lat, stn_lon, xlat, xlon,data):
    difflat = stn_lat - xlat
    difflon = stn_lon - xlon
    rad = np.multiply(difflat,difflat)+np.multiply(difflon , difflon)
    aa=np.where(rad==np.min(rad))
    ind=np.squeeze(np.array(aa))
    t2 = []
    # t2= data.variables['T2'][23][ind[0]][ind[1]]
    # p = data.variables['PSFC'][23][ind[0]][ind[1]]
    # t2 = data.variables['T2'][23][ind[0]][ind[1]]
    # t2 = data.variables['T2'][23][ind[0]][ind[1]]
    rh = data.variables['Q2'][23][ind[0]][ind[1]]
    for i in range(len(data.variables['T2'])):
        t2.append((data.variables['T2'][i][ind[0]][ind[1]]-272.15,dp_temp.temp2dptemp(data.variables['T2'][i][ind[0]][ind[1]]-272.15,dp_temp.calrh(data.variables['Q2'][i][ind[0]][ind[1]],data.variables['T2'][i][ind[0]][ind[1]]-272.15,data.variables['PSFC'][i][ind[0]][ind[1]]/1000)),data.variables['PSFC'][i][ind[0]][ind[1]]/100,data.variables['U'][i][0][ind[0]][ind[1]],data.variables['V'][i][0][ind[0]][ind[1]]))
        # t2.append(data.variables['T2'][i][ind[0]][ind[1]] - 272.15)
    return t2





