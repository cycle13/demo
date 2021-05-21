import cdsapi

c = cdsapi.Client()

c.retrieve(
    'derived-utci-historical',
    {
        'format': 'zip',
        'variable': [
            'mean_radiant_temperature', 'universal_thermal_climate_index',
        ],
        'product_type': 'intermediate_dataset',
        'year': '2021',
        'month': '04',
        'day': '01',
    },
    'download.zip')