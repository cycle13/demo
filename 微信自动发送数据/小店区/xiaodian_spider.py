import time
import requests
import json
import xlwt
from datetime import datetime


session = requests.Session()
hour_station_sta_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=1&isControlPoint=1&stationType=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def realaqi(hour_local_std_url):
    res = session.get(hour_local_std_url,headers=headers).text
    data = json.loads(res)
    return data


def save_aqi_excel(url):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0,0,'站点名称')
    sheet.write(0,1,'AQI')
    sheet.write(0,2,'排名')
    sheet.write(0,3,'首要污染物')
    m = 0
    while True:
        data = realaqi(url)
        if len(data) == 0:
            time.sleep(60)
            print(m)
            m += 1
            if m >= 10:
                break
        else:
            break
    for k in data:
        sheet.write(n, 0, k['name'])
        sheet.write(n, 1, k["aqi"])
        sheet.write(n, 3, k['primaryPollutant'])
        n+=1
        now_datetime = k['dataTime']
    book.save(r'excelfiles\小店区两站点AQI数据.xls')
    return now_datetime


def save_zong_excel(url):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0,0,'站点名称')
    sheet.write(0,1,'综合指数')
    sheet.write(0,2,'排名')
    sheet.write(0,3,'首要污染物')
    m = 0
    while True:
        data = realaqi(url)
        if len(data) == 0:
            time.sleep(60)
            print(m)
            m += 1
            if m >= 10:
                break
        else:
            break
    for k in data:
        sheet.write(n, 0, k['name'])
        sheet.write(n, 1, k["totalIndex"])
        sheet.write(n, 3, k['primaryPollutant'])
        n+=1
        now_datetime = k['dataTime']
    book.save(r'excelfiles\小店区两站点综合指数数据.xls')
    return now_datetime


def data(hour_local_std_url):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    x = save_zong_excel(hour_local_std_url)
    return x

def aqi_data(hour_local_std_url):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    x = save_aqi_excel(hour_local_std_url)
    return x


def zonghe():
    timeArray = aqi_data(hour_station_sta_url)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y') + '年' + datetime.strptime(timeArray,'%Y-%m-%d %H:%M:%S').strftime('%m') + '月' + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d') + "日" + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H') + '时'
    return time_now



def aqi():
    timeArray = data(hour_station_sta_url)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y') + '年' + datetime.strptime(timeArray,'%Y-%m-%d %H:%M:%S').strftime('%m') + '月' + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d') + "日" + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H') + '时'
    return time_now

