import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': 'specific_humidity',
        'pressure_level': '1000',
        'year': '2021',
        'month': '05',
        'day': '26',
        'time': '00:00',
    },
    'download.nc')