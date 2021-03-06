import time
import requests
import json
import xlwt
from decimal import *
from datetime import datetime
import datetime as datatime


session = requests.Session()
hour_local_url = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewGroupByRegion'
# day_station_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}&dataType=2&flag=3&isControlPoint=1&stationType=1'
day_station_url = 'http://www.ty.daqi110.com/tyAirService/pust/postAccumulativeData?areaCode=1401&areaType=4&dataType=2&etime={}&flag=3&isControlPoint=&stationType=1&stime={}'
hour_station_sta_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=4&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=1&stationType=1'
hour_station_lj_url ='http://www.ty.daqi110.com/tyAirService/pust/postAccumulativeData?areaCode=1401&areaType=4&dataType=1&etime={}+{}%3A00%3A00&flag=3&isControlPoint=&stationType=1&stime={}+01%3A00%3A00'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}



def save_station_excel(yestoday):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0,1,'点位')
    sheet.write(0,2,'浓度值1')
    sheet.write(0, 3, '排名1')
    sheet.write(0, 4, '浓度值2')
    sheet.write(0, 5, '排名2')
    sheet.write(0, 6, '浓度值3')
    sheet.write(0, 7, '排名3')
    sheet.write(0, 8, '浓度值4')
    sheet.write(0, 9, '排名4')
    sheet.write(0, 10, '浓度值5')
    sheet.write(0, 11, '排名5')
    sheet.write(0, 12, '浓度值6')
    sheet.write(0, 13, '排名6')
    sheet.write(0, 14, '综合指数')
    data = realaqi(day_station_url.format(yestoday,yestoday))
    now_datetime = data[0]['dataTime']
    for k in data:
        if k['name'] in ['桃园','金胜','南寨','尖草坪','巨轮','坞城','晋源','小店']:
            sheet.write(n, 1, k['name'])
            if k["so2"] == '0' or k["so2"] == '-':
                sheet.write(n, 2, None)
            else:
                sheet.write(n, 2, k["so2"])
            # sheet.write(n, 2, k["so2"])
            if k["no2"] == '0' or k["no2"] == '-':
                sheet.write(n, 4, None)
            else:
                sheet.write(n, 4, k["no2"])
            # sheet.write(n, 4, k["no2"])
            if k["co"] == '0' or k["co"] == '-':
                sheet.write(n, 6, None)
            else:
                sheet.write(n, 6, k["co"])
            # sheet.write(n, 6, k["co"])
            if k["o38"] == '0' or k["o38"] == '-':
                sheet.write(n, 8, None)
            else:
                sheet.write(n, 8, k["o38"])
            # sheet.write(n, 10, k["pm25"])
            if k["pm25"] == '0' or k["pm25"] == '-':
                sheet.write(n, 10, None)
            else:
                sheet.write(n, 10, k["pm25"])
            # sheet.write(n, 12, k["pm10"])
            if k["pm10"] == '0' or k["pm10"] == '-':
                sheet.write(n, 12, None)
            else:
                sheet.write(n, 12, k["pm10"])
            # sheet.write(n, 14, k["totalIndex"])
            if ((k["so2"] == '-' or k["so2"] == '0') or (k["no2"] == '-' or k["no2"] == '0') or (k["co"] == '-' or k["co"] == '0') or (k["o38"] == '-' or k["o38"] == '0') or (k["pm25"] == '-' or k["pm25"] == '0') or (k["pm10"] == '-' or k["pm10"] == '0')):
                sheet.write(n, 14, None)
            else:
                sheet.write(n, 14, k["totalIndex"])
            n+=1
    book.save(r'excelfiles\杏花岭小时推送数据.xls')
    return now_datetime


def save_station1_excel(yestoday,now_data,now_time):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0, 1, '点位')
    sheet.write(0, 2, '浓度值1')
    sheet.write(0, 3, '排名1')
    sheet.write(0, 4, '浓度值2')
    sheet.write(0, 5, '排名2')
    sheet.write(0, 6, '浓度值3')
    sheet.write(0, 7, '排名3')
    sheet.write(0, 8, '浓度值4')
    sheet.write(0, 9, '排名4')
    sheet.write(0, 10, '浓度值5')
    sheet.write(0, 11, '排名5')
    sheet.write(0, 12, '浓度值6')
    sheet.write(0, 13, '排名6')
    sheet.write(0, 14, '综合指数')
    data = realaqi(hour_station_lj_url.format(now_data,now_time,yestoday))
    now_datetime = data[0]['dataTime']
    for k in data:
        if k['name'] in ['桃园', '金胜', '南寨', '尖草坪', '巨轮', '坞城', '晋源', '小店']:
            sheet.write(n, 1, k['name'])
            if k["so2"] == '0' or k["so2"] == '-':
                sheet.write(n, 2, None)
            else:
                sheet.write(n, 2, k["so2"])
            # sheet.write(n, 2, k["so2"])
            # sheet.write(n, 4, k["no2"])
            if k["no2"] == '0' or k["no2"] == '-':
                sheet.write(n, 4, None)
            else:
                sheet.write(n, 4, k["no2"])
            # sheet.write(n, 6, str(Decimal(k["co"]).quantize(Decimal('0.0'))))
            if k["co"] == '0' or k["co"] == '-':
                sheet.write(n, 6, None)
            else:
                sheet.write(n, 6, str(Decimal(k["co"]).quantize(Decimal('0.0'))))
            if k["o38"] == '0' or k["o38"] == '-':
                sheet.write(n, 8, None)
            else:
                sheet.write(n, 8, k["o38"])
            # sheet.write(n, 10, k["pm25"])
            if k["pm25"] == '0' or k["pm25"] == '-':
                sheet.write(n, 10, None)
            else:
                sheet.write(n, 10, k["pm25"])
            # sheet.write(n, 12, k["pm10"])
            if k["pm10"] == '0' or k["pm10"] == '-':
                sheet.write(n, 12, None)
            else:
                sheet.write(n, 12, k["pm10"])
            # sheet.write(n, 14, k["totalIndex"])
            if ((k["so2"] == '-' or k["so2"] == '0') or (k["no2"] == '-' or k["no2"] == '0') or (k["co"] == '-' or k["co"] == '0') or (k["o38"] == '-' or k["o38"] == '0') or (k["pm25"] == '-' or k["pm25"] == '0') or (k["pm10"] == '-' or k["pm10"] == '0')):
                sheet.write(n, 14, None)
            else:
                sheet.write(n, 14, k["totalIndex"])
            n += 1
    book.save(r'excelfiles\杏花岭今日小时推送数据.xls')
    return now_datetime


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
            data = realaqi1(url)
            for k in data:
                if k['name'] in ['巨轮']:
                    sheet.write(n, 0, k['dataTime'][5:])
                    sheet.write(n, 1, k['name'])
                    sheet.write(n, 2, k["so2"])
                    sheet.write(n, 3, k["no2"])
                    sheet.write(n, 4, k["co"])
                    sheet.write(n, 5, k["o31"])
                    sheet.write(n, 6, k["pm25"])
                    sheet.write(n, 7, k["pm10"])
                    n += 1
        now_time = datetime.now().strftime("%Y-%m-%d")
        url = url1.format(now_time, "00")
        data = realaqi1(url)
        for k in data:
            if k['name'] in ['巨轮']:
                sheet.write(n, 0, k['dataTime'][5:])
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
            data = realaqi1(url)
            for k in data:
                if k['name'] in ['巨轮']:
                    sheet.write(n, 0, k['dataTime'][5:])
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


def realaqi(day_station_url):
    res = session.get(day_station_url,headers=headers).text
    res = res.replace('NA', '-')
    data = json.loads(res)
    return data

def realaqi1(day_station_url):
    res = session.get(day_station_url,headers=headers).text
    data = json.loads(res)
    return data


def station():
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    timeArray = save_station_excel(yestoday)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d').strftime('%Y')+'年'+datetime.strptime(timeArray, '%Y-%m-%d').strftime('%m')+'月'+datetime.strptime(timeArray, '%Y-%m-%d').strftime('%d')+"日"
    return time_now


def station1():
    if datetime.strftime(datetime.now(), '%H') == '00':
        yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    else:
        yestoday = datetime.strftime(datetime.now(), '%Y-%m-%d')
    now_data = datetime.strftime(datetime.now(), '%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(), '%H')
    timeArray = save_station1_excel(yestoday,now_data,now_time)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y')+'年'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%m')+'月'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d')+"日"
    my_datatime = datetime.strftime(datetime.now(), '%H')
    time_now1 = '01-' + my_datatime + '时'
    return time_now,time_now1
#
# def station1():
#     timeArray = time.localtime(float(int(save_station1_excel()[6:-2])/1000))
#     time_now = time.strftime('%Y',timeArray)+'年'+time.strftime('%m',timeArray)+'月'+time.strftime('%d',timeArray)+"日"
#     time_now1 = '1-'+time.strftime('%H',timeArray)+'时'
#     return (time_now,time_now1)


def leiji(excel_xishanleiji_dir):
    now_time = save_stationleiji_excel(hour_station_sta_url,excel_xishanleiji_dir)
    return now_time
