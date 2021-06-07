#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 15:49
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo_no.py
# @Software: PyCharm

import requests
import os
import re
import time
import datetime
import shuiyin

day1 = datetime.datetime(2022,6,1)
day2 = datetime.datetime.now()
d = (day1-day2).days
if d < 0:
    print('授权已过期！')
    exit()

url1 = r'https://www.ready.noaa.gov/hypub-bin/trajsrc.pl'
url2 = r'https://www.ready.noaa.gov/hypub-bin/trajsrcm.pl'
url3 = r'https://www.ready.noaa.gov/hypub-bin/traj1.pl'
url4 = r'https://www.ready.noaa.gov/hypub-bin/traj2.pl'
url5 = r'https://www.ready.noaa.gov/hypub-bin/trajresults.pl?jobidno={}'
url6 = r'https://www.ready.noaa.gov/hypubout/{}_trj001.gif'
urljs1 = 'https://www.ready.noaa.gov/hypub/hysplit.js'
urljs2 = 'https://www.ready.noaa.gov/hypub/fnlmap.js'
urljs3 = 'https://www.ready.noaa.gov/hypub/jquery-3.2.1.js'
urlgis = 'https://www.ready.noaa.gov/hypubout/HYSPLITtraj_{}.kmz'
urlgis1 = 'https://www.ready.noaa.gov/hypubout/gis_{}.zip'


header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'_ga=GA1.2.1989884762.1619342232; nmstat=6c6f8292-8e42-1a01-68f8-f0106f063d98; oneTimePop=used; CGISESSID=fc94b9b49f02dac16e3f9093493547bd',
    'Host':'www.ready.noaa.gov',
    'Referer':'https://www.ready.noaa.gov/hypub-bin/traj2.pl',
    'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile':'?0',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}

direction = input('请输入前向轨迹还是后向轨迹，前向：Forward，后向：Backward：')
lon = input('请输入经度E：')
lat = input('请输入纬度N：')

metcyc = input('请输入气象预报周期，如：00 20210601：')
start_year = input('请输入开始年，如：21：')
start_month = input('请输入开始月，如：06：')
start_day = input('请输入开始日，如：01：')
start_hour = input('请输入开始时，如：4：')
duration = input('请输入预测时间长度，如：120，数值为小时：')
source_hunit = input('请输入高度情况，相对地面高度请输入0，相对海拔高度请输入1：')
hgt1=input('请输入第一个高度，如：100：')
hgt2=input('请输入第二个高度，如：500：')
hgt3=input('请输入第三个高度，如：1000：')
gis=input('是否输出gis文件，不输出请输入0，输出shape文件输入1，输出kmz文件输入3，如：3：')
lonew = 'E'
latns = 'N'
print('正在计算......')
session = requests.Session()
res1 = session.get(url1)
data2 = {
        'metdata':'GFS',
        'SOURCELOC': 'decdegree',
        'Lat': lat,
        'Latns': 'N',
        'Lon': lon,
        'Lonew': lonew,
        'Latd': '',
        'Latm': '',
        'Lats': '',
        'Latdns':latns,
        'Lond': '',
        'Lonm': '',
        'Lons': '',
        'Londew':'W',
        'CITYNAME': '',
        'WMO': '',
}
res2 = session.post(url2,data=data2)
data3 = {
        'metcyc':metcyc,
}
res3 = session.post(url3,data = data3)

data4 = {
    'direction': direction,
    'vertical':'0',
    'Start year':start_year,
    'Start month':start_month,
    'Start day':start_day,
    'Start hour':start_hour,
    'duration':duration,
    'repeatsrc':'0',
    'ntrajs':'24',
    'Source lat':lat,
    'Source lon':lon,
    'Source lat2': '',
    'Source lon2':'' ,
   ' Source lat3':'' ,
    'Source lon3': '',
    'Midlayer height':'No',
    'Source hgt1':hgt1,
    'Source hunit':source_hunit,
    'Source hgt2':hgt2,
    'Source hgt3':hgt3,
    'gis':gis,
    'gsize':'96',
    'Zoom Factor':'70',
    'projection':'0',
    'Vertical Unit':'1',
    'Label Interval':'6',
    'color':'Yes',
    'colortype':'Yes',
    'pltsrc':'1',
    'circle':'-1',
    'county':'arlmap',
    'psfile':'No',
    'pdffile':'Yes',
    'mplot':'NO',
}

res4 = session.post(url4,data = data4)
patton = re.compile(r'jobidno=(.*?)">')
resu = re.findall(patton,res4.text)[0]
for i in range(2):
    time.sleep(10)
    res5 = session.get(url5.format(resu),headers = header)
    session.get(urljs1)
    session.get(urljs2)
    session.get(urljs3)
res6 = session.get(url6.format(resu))
if not os.path.exists('pic'):
    os.makedirs('pic')
with open('county_image/picture_{}_{}_{}.png'.format(lon,lat,metcyc[3:]),'wb') as f:
    f.write(res6.content)
if gis == '3':
    resgis = session.get(urlgis.format(resu))
    with open('county_image/gis_{}_{}_{}.kmz'.format(lon, lat, metcyc[3:]), 'wb') as f:
        f.write(resgis.content)
if gis == '1':
    resgis = session.get(urlgis1.format(resu))
    with open('county_image/gis_{}_{}_{}.zip'.format(lon, lat, metcyc[3:]), 'wb') as f:
        f.write(resgis.content)
print('计算完成！')

shuiyin.shuiyin('picture_{}_{}_{}.png'.format(lon,lat,metcyc[3:]))
print('添加水印完成！')