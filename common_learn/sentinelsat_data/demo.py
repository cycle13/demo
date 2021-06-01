#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 15:10
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo_no.py
# @Software: PyCharm

from sentinelsat.sentinel import SentinelAPI,read_geojson,geojson_to_wkt
from collections import OrderedDict


api = SentinelAPI('wyj901020','WANGYANJUN28','https://scihub.copernicus.eu/dhus/')
roi = 'POLYGON((38.345 29.827,38.356 29.827,38.356 29.836,38.345 29.836,38.345 29.827))'
start_date = '20190524'
end_date = '20190530'

product_type = 'S2MSI2A'
cloud_cover = [0,50]

products = api.query(area=roi,date=(start_date,end_date),producttype = product_type,cloudcoverpercentage=cloud_cover)
downfiles = OrderedDict()
for i in products:
    product = products[i]
    filename = product['filename']
    print(filename)

successfile = api.download_all(products,directory_path=r'D:\Program Files\pycharm\common_learn\sentinelsat_data\data')