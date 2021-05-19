from netCDF4 import Dataset


def wrf_data(path):
    data = Dataset(path, mode='r')
    lons = data.variables['XLONG'][0]
    lats = data.variables['XLAT'][0]
    return data,lons,lats


