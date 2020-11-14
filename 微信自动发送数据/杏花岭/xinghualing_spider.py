import time
import requests
import json
import xlwt
from decimal import Decimal


session = requests.Session()
hour_local_url = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewGroupByRegion'
hour_station_url = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewByCityCode?RegionId=140101'
headers = {
    'Host': '183.203.223.83:85',
    'Referer': 'http://183.203.223.83:85/ReleaseHome/IndexTy',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}



def save_station_excel():
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
    l = realaqi(hour_station_url)
    data = json.loads(l)
    for k in data:
        if k['PointName'] in ['桃园','金胜','南寨','尖草坪','巨轮','坞城','晋源','小店']:
            sheet.write(n, 1, k['PointName'])
            sheet.write(n, 2, k["SO2"])
            sheet.write(n, 4, k["NO2"])
            sheet.write(n, 6, Decimal(k["CO"]).quantize(Decimal("0.0")))
            sheet.write(n, 8, k["O3"])
            sheet.write(n, 10, k["PM25"])
            sheet.write(n, 12, k["PM10"])
            sheet.write(n, 14, Decimal(k["SO2"]/60+k["NO2"]/40+k["PM10"]/70+k["CO"]/4+k["O3"]/160+k["PM25"]/35).quantize(Decimal("0.00")))
            n+=1
            m = k['Time']
    book.save(r'excelfiles\杏花岭小时推送数据.xls')
    return m

def save_station1_excel():
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
    l = realaqi(hour_station_url)
    data = json.loads(l)
    for k in data:
        if k['PointName'] in ['桃园','金胜','南寨','尖草坪','巨轮','坞城','晋源','小店']:
            sheet.write(n, 1, k['PointName'])
            sheet.write(n, 2, k["SO2"])
            sheet.write(n, 4, k["NO2"])
            sheet.write(n, 6, Decimal(k["CO"]).quantize(Decimal("0.0")))
            sheet.write(n, 8, k["O3"])
            sheet.write(n, 10, k["PM25"])
            sheet.write(n, 12, k["PM10"])
            sheet.write(n, 14, Decimal(k["SO2"]/60+k["NO2"]/40+k["PM10"]/70+k["CO"]/4+k["O3"]/160+k["PM25"]/35).quantize(Decimal("0.00")))
            n+=1
            m = k['Time']
    book.save(r'excelfiles\杏花岭今日小时推送数据.xls')
    return m


def realaqi(url):
    response = session.get(url= url,headers = headers).text
    return response


def station():
    timeArray = time.localtime(float(int(save_station_excel()[6:-2])/1000))
    time_now = time.strftime('%Y',timeArray)+'年'+time.strftime('%m',timeArray)+'月'+time.strftime('%d',timeArray)+"日"+time.strftime('%H',timeArray)+'时'
    return time_now


def station1():
    timeArray = time.localtime(float(int(save_station1_excel()[6:-2])/1000))
    time_now = time.strftime('%Y',timeArray)+'年'+time.strftime('%m',timeArray)+'月'+time.strftime('%d',timeArray)+"日"+time.strftime('%H',timeArray)+'时'
    return time_now

