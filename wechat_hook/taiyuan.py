#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 16:18
# @Author  : Yanjun Wang
# @Site    : 
# @File    : taiyuan.py
# @Software: PyCharm

import requests
import json
import time


def station(name):
    local_aqi = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime=20210603+22%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'
    station_aqi = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewByCityCode?RegionId=140101'
    session = requests.Session()
    res = session.get(station_aqi).text
    data = json.loads(res)
    for i in data:
        if i['PointName'] == name:
            return (i['SO2'],i['NO2'],i['PM10'],i['CO'],i['O3'],i['PM25'],i['AQIScore'],i['PollutionStatus'])



