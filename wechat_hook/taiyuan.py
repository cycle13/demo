#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 16:18
# @Author  : Yanjun Wang
# @Site    : 
# @File    : taiyuan.py
# @Software: PyCharm

import requests
import json
import datetime


def station(name):
    station_aqi = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewByCityCode?RegionId=140101'
    session = requests.Session()
    res = session.get(station_aqi).text
    data = json.loads(res)
    for i in data:
        if i['PointName'] == name:
            return (i['SO2'],i['NO2'],i['PM10'],i['CO'],i['O3'],i['PM25'],i['AQIScore'],i['PollutionStatus'])



def local(name):
    if int(datetime.datetime.now().strftime("%M")) <30:
        yestoday = (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime("%Y%m%d %H")
        local_aqi = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'.format(yestoday[0:8],yestoday[9:11])
    else:
        yestoday = datetime.datetime.now().strftime("%Y%m%d %H")
        local_aqi = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'.format(yestoday[0:8], yestoday[9:11])
    session = requests.Session()
    res = session.get(local_aqi).text
    data = json.loads(res)
    for i in data:
        if i['name'] == name:
            return (i['so2'],i['no2'],i['pm10'],i['co'],i['o31'],i['pm25'],i['aqi'],i['airQualityType'])
