import pandas as pd


def station_lon_lat(station):
    data = pd.read_excel('station/中国地面气象站基本气象要素观测资料台站表.xlsx')
    xl = data[(data['站名'].isin([station]))]
    station = xl['区站号']
    lon = xl['经度']
    lat = xl['纬度']
    return station,lon,lat

station_lon_lat('呼和浩特')
