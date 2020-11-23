import time
import requests
import json
import xlwt
from datetime import datetime
import pandas as pd
import datetime as datatime


session = requests.Session()
hour_local_std_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime={}+{}%3A00%3A00&dataType=1&flag=1&isControlPoint=2&stationType=1'
hour_station_prv_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=1&isControlPoint=2&stationType=1'
hour_station_sta_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=1&isControlPoint=1&stationType=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def realaqi(hour_local_std_url):
    res = session.get(hour_local_std_url,headers=headers).text
    data = json.loads(res)
    return data


def save_location_excel(url,excel_sixrank_dir):
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
        sheet.write(n, 4, k["co"])
        sheet.write(n, 5, k["o31"])
        sheet.write(n, 6, k["pm25"])
        sheet.write(n, 7, k["pm10"])
        sheet.write(n, 8, k["aqi"])
        sheet.write(n, 9, k["primaryPollutant"])
        sheet.write(n, 10, k['airQualityLevel'])
        sheet.write(n, 11, k['airQualityType'])
        n+=1
    book.save(excel_sixrank_dir)



def save_station_excel(url,url1,excel_starank_dir):
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
    book.save(excel_starank_dir)
    return now_datetime


def save_stationtable_excel(url,url1,excel_file_dir):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0, 1, '点位名称')
    sheet.write(0, 2, 'AQI')
    sheet.write(0, 3, '首要污染物')
    sheet.write(0, 4, '首要污染物浓度(μg/m3)')
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
        print(data)
        sheet.write(n, 1, k['name'])
        sheet.write(n, 2, k["aqi"])
        sheet.write(n, 3, k["primaryPollutant"])
        qua = []
        if 'PM10' in k["primaryPollutant"]:
            qua.append(k["pm10"])
        if 'PM2.5' in k["primaryPollutant"]:
            qua.append(k["pm25"])
        if 'SO2' in k["primaryPollutant"]:
            qua.append(k["so2"])
        if 'NO2' in k["primaryPollutant"]:
            qua.append(k["no2"])
        if 'CO' in k["primaryPollutant"]:
            qua.append(k["co"])
        if 'O3' in k["primaryPollutant"]:
            qua.append(k["o31"])
        if "无" in k["primaryPollutant"]:
            qua.append('-')
        sheet.write(n, 4, '、'.join(qua))

        # if k["primaryPollutant"] == 'PM10':
        #     sheet.write(n, 4, k["pm10"])
        # elif k["primaryPollutant"] == 'PM2.5':
        #     sheet.write(n, 4, k["pm25"])
        # elif k["primaryPollutant"] == 'SO2':
        #     sheet.write(n, 4, k["so2"])
        # elif k["primaryPollutant"] == 'NO2':
        #     sheet.write(n, 4, k["no2"])
        # elif k["primaryPollutant"] == 'CO':
        #     sheet.write(n, 4, k["co"])
        # elif k["primaryPollutant"] == 'O3':
        #     sheet.write(n, 4, k["o31"])
        # else:
        #     sheet.write(n, 4, '-')
        n += 1
    m = 0
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
        sheet.write(n, 2, k["aqi"])
        sheet.write(n, 3, k["primaryPollutant"])
        qua = []
        if 'PM10' in k["primaryPollutant"]:
            qua.append(k["pm10"])
        if 'PM2.5' in k["primaryPollutant"]:
            qua.append(k["pm25"])
        if 'SO2' in k["primaryPollutant"]:
            qua.append(k["so2"])
        if 'NO2' in k["primaryPollutant"]:
            qua.append(k["no2"])
        if 'CO' in k["primaryPollutant"]:
            qua.append(k["co"])
        if 'O3' in k["primaryPollutant"]:
            qua.append(k["o31"])
        if "无" in k["primaryPollutant"]:
            qua.append('-')
        sheet.write(n, 4, '、'.join(qua))
        n += 1
        now_datetime = k['dataTime']
    book.save(excel_file_dir)


def save_stationline_excel(url1,excel_file_dir):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '时间')
    sheet.write(0, 1, '点位名称')
    sheet.write(0, 2, 'SO2')
    sheet.write(0, 3, 'NO2')
    sheet.write(0, 4, 'CO')
    sheet.write(0, 5, 'O3')
    sheet.write(0, 6, 'PM2.5')
    sheet.write(0, 7, 'PM10')
    m = 0
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d %H")
    now_data = datetime.strftime(datetime.now(), "%Y-%m-%d %H")
    my_datatime = pd.date_range(start=yestoday, end=now_data, freq='1h')
    for i in my_datatime:
        now_data = i.strftime('%Y-%m-%d')
        now_time = i.strftime('%H')
        url = url1.format(now_data,now_time)
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
            if k['name'] in ['西山']:
                sheet.write(n, 0, k['dataTime'])
                sheet.write(n, 1, k['name'])
                sheet.write(n, 2, k["so2"])
                sheet.write(n, 3, k["no2"])
                sheet.write(n, 4, k["co"])
                sheet.write(n, 5, k["o31"])
                sheet.write(n, 6, k["pm25"])
                sheet.write(n, 7, k["pm10"])
                n += 1
    book.save(excel_file_dir)


def save_stationleiji_excel(url1,excel_file_dir):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '时间')
    sheet.write(0, 1, '点位名称')
    sheet.write(0, 2, 'SO2')
    sheet.write(0, 3, 'NO2')
    sheet.write(0, 4, 'CO')
    sheet.write(0, 5, 'O3')
    sheet.write(0, 6, 'PM2.5')
    sheet.write(0, 7, 'PM10')
    m = 0
    now_time = datetime.strftime(datetime.now(), "%H")
    if now_time == '00':
        yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
        for i in range(1, 24):
            url = url1.format(yestoday, str(i))
            data = realaqi(url)
            for k in data:
                if k['name'] in ['西山']:
                    sheet.write(n, 0, k['dataTime'])
                    sheet.write(n, 1, k['name'])
                    sheet.write(n, 2, k["so2"])
                    sheet.write(n, 3, k["no2"])
                    sheet.write(n, 4, k["co"])
                    sheet.write(n, 5, k["o31"])
                    sheet.write(n, 6, k["pm25"])
                    sheet.write(n, 7, k["pm10"])
                    n += 1
        now_time = datetime.now().strftime("%Y-%m-%d")
        url = url1.format(now_time, str(i))
        data = realaqi(url)
        for k in data:
            if k['name'] in ['西山']:
                sheet.write(n, 0, k['dataTime'])
                sheet.write(n, 1, k['name'])
                sheet.write(n, 2, k["so2"])
                sheet.write(n, 3, k["no2"])
                sheet.write(n, 4, k["co"])
                sheet.write(n, 5, k["o31"])
                sheet.write(n, 6, k["pm25"])
                sheet.write(n, 7, k["pm10"])
                n += 1
        now_time = 24
    else:
        now_data = datetime.now().strftime("%Y-%m-%d")
        now_time = datetime.strftime(datetime.now(), "%H")
        for i in range(1, int(now_time) + 1):
            print(now_data, str(i))
            url = url1.format(now_data,str(i))
            data = realaqi(url)
            for k in data:
                if k['name'] in ['西山']:
                    sheet.write(n, 0, k['dataTime'])
                    sheet.write(n, 1, k['name'])
                    sheet.write(n, 2, k["so2"])
                    sheet.write(n, 3, k["no2"])
                    sheet.write(n, 4, k["co"])
                    sheet.write(n, 5, k["o31"])
                    sheet.write(n, 6, k["pm25"])
                    sheet.write(n, 7, k["pm10"])
                    n += 1
    book.save(excel_file_dir)
    return now_time


def data(hour_local_std_url,excel_sixrank_dir):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    save_location_excel(hour_local_std_url,excel_sixrank_dir)


def station_data(hour_local_std_url,hour_station_prv_url,excel_starank_dir):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    hour_station_prv_url = hour_station_prv_url.format(now_data,now_time)
    x = save_station_excel(hour_local_std_url,hour_station_prv_url,excel_starank_dir)
    return x

def table_data(hour_station_sta_url,hour_station_prv_url,excel_file_dir):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_station_sta_url.format(now_data, now_time)
    hour_station_prv_url = hour_station_prv_url.format(now_data, now_time)
    save_stationtable_excel(hour_local_std_url,hour_station_prv_url,excel_file_dir)


def location(excel_sixrank_dir):
    data(hour_local_std_url,excel_sixrank_dir)


def station(excel_starank_dir):
    timeArray = station_data(hour_station_sta_url,hour_station_prv_url,excel_starank_dir)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y') + '年' + datetime.strptime(timeArray,'%Y-%m-%d %H:%M:%S').strftime('%m') + '月' + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d') + "日" + datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H') + '时'
    return time_now


def line_station(excel_file_dir):
    save_stationline_excel(hour_station_prv_url,excel_file_dir)

def table_excel(excel_file_dir):
    table_data(hour_station_sta_url,hour_station_prv_url,excel_file_dir)


def leiji(excel_xishanleiji_dir):
    now_time = save_stationleiji_excel(hour_station_prv_url,excel_xishanleiji_dir)
    return now_time


