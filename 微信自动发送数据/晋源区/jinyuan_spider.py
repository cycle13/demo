import time
import requests
import json
import xlwt
from decimal import *
from datetime import datetime


session = requests.Session()
hour_local_std_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'
hour_station_prv_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'
hour_station_sta_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=1&stationType=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def realaqi(hour_local_std_url):
    res = session.get(hour_local_std_url,headers=headers).text
    # res = res.replace('NA','-')
    data = json.loads(res)
    return data


def save_location_excel(url):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0,1,'点位名称')
    sheet.write(0,2,'SO2')
    sheet.write(0, 3, 'NO2')
    sheet.write(0, 4, 'CO')
    sheet.write(0, 5, 'O3')
    sheet.write(0, 6, 'PM2.5')
    sheet.write(0, 7, 'PM10')
    sheet.write(0, 8, 'AQI')
    sheet.write(0,9,'首要污染物')
    sheet.write(0, 10, '类别')
    sheet.write(0, 11, '优良')
    m = 0
    while True:
        data = realaqi(url)
        if len(data) == 0:
            time.sleep(60)
            print(m)
            m+=1
            if m>=10:
                break
        else:
            break
    for k in data:
        sheet.write(n, 1, k['name'])
        sheet.write(n, 2, k["so2"])
        sheet.write(n, 3, k["no2"])
        sheet.write(n, 4, str(Decimal(k["co"]).quantize(Decimal('0.0'))))
        sheet.write(n, 5, k["o31"])
        sheet.write(n, 6, k["pm25"])
        sheet.write(n, 7, k["pm10"])
        sheet.write(n, 8, k["aqi"])
        sheet.write(n, 9, k["primaryPollutant"])
        sheet.write(n, 10, k['airQualityLevel'])
        sheet.write(n, 11, k['airQualityType'])
        n+=1
        now_datetime = k['dataTime']
    book.save(r'excelfiles\太原市六城区空气质量日报.xls')
    return now_datetime




def save_station_excel(url,url1):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0, 1, '点位名称')
    sheet.write(0, 2, 'SO2')
    sheet.write(0, 3, 'NO2')
    sheet.write(0, 4, 'CO')
    sheet.write(0, 5, 'O3')
    sheet.write(0, 6, 'PM2.5')
    sheet.write(0, 7, 'PM10')
    sheet.write(0, 8, 'AQI')
    sheet.write(0, 9, '首要污染物')
    sheet.write(0, 10, '类别')
    sheet.write(0, 11, '优良')
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
        sheet.write(n, 1, k['name'])
        sheet.write(n, 2, k["so2"])
        sheet.write(n, 3, k["no2"])
        sheet.write(n, 4, k["co"])
        sheet.write(n, 5, k["o31"])
        sheet.write(n, 6, k["pm25"])
        sheet.write(n, 7, k["pm10"])
        sheet.write(n, 8, k["aqi"])
        sheet.write(n, 9, k["primaryPollutant"])
        sheet.write(n, 10, k['airQualityLevel'])
        sheet.write(n, 11, k['airQualityType'])
        n += 1
        now_datetime = k['dataTime']
    while True:
        data = realaqi(url1)
        if len(data) == 0:
            time.sleep(60)
            print(m)
            m += 1
            if m >= 10:
                break
        else:
            break
    for k in data:
        sheet.write(n, 1, k['name'])
        sheet.write(n, 2, k["so2"])
        sheet.write(n, 3, k["no2"])
        sheet.write(n, 4, k["co"])
        sheet.write(n, 5, k["o31"])
        sheet.write(n, 6, k["pm25"])
        sheet.write(n, 7, k["pm10"])
        sheet.write(n, 8, k["aqi"])
        sheet.write(n, 9, k["primaryPollutant"])
        sheet.write(n, 10, k['airQualityLevel'])
        sheet.write(n, 11, k['airQualityType'])
        n += 1
    book.save(r'excelfiles\太原市六城区标站空气质量日报.xls')
    return now_datetime



def data(hour_local_std_url):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    x = save_location_excel(hour_local_std_url)
    return x

def station_data(hour_local_std_url,hour_station_prv_url):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    hour_station_prv_url = hour_station_prv_url.format(now_data,now_time)
    x = save_station_excel(hour_local_std_url,hour_station_prv_url)
    return x


def location():
    timeArray = data(hour_local_std_url)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y')+'年'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%m')+'月'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d')+"日"+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H')+'时'
    return (time_now,datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H'))

def station():
    timeArray = station_data(hour_station_sta_url,hour_station_prv_url)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y') + '年' + datetime.strptime(timeArray,'%Y-%m-%d %H:%M:%S').strftime('%m') + '月' + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d') + "日" + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H') + '时'
    return time_now


