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


def save_aqi_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0,0,'站点名称')
    sheet.write(0,1,'AQI')
    sheet.write(0,2,'排名')
    sheet.write(0,3,'首要污染物')
    time.sleep(5)
    l = realaqi(hour_station_url)
    data = json.loads(l)
    for k in data:
        if k['PointName'] in ['上兰','桃园','金胜','南寨','尖草坪','巨轮','坞城','晋源','小店']:
            sheet.write(n, 0, k['PointName'])
            sheet.write(n, 1, k["AQIScore"])
            sheet.write(n, 3, k['TopPollution'])
            n+=1
            m = k['Time']
    book.save(r'excelfiles\小店区两站点AQI数据.xlsx')
    return m


def save_zong_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0,0,'站点名称')
    sheet.write(0,1,'综合指数')
    sheet.write(0,2,'排名')
    sheet.write(0,3,'首要污染物')
    time.sleep(5)
    l = realaqi(hour_station_url)
    data = json.loads(l)
    for k in data:
        if k['PointName'] in ['上兰','桃园','金胜','南寨','尖草坪','巨轮','坞城','晋源','小店']:
            sheet.write(n, 0, k['PointName'])
            sheet.write(n, 1, Decimal(k["SO2"]/60+k["NO2"]/40+k["PM10"]/70+k["CO"]/4+k["O3"]/160+k["PM25"]/35).quantize(Decimal("0.00")))
            sheet.write(n, 3, k['TopPollution'])
            n+=1
            m = k['Time']
    book.save(r'excelfiles\小店区两站点综合指数数据.xls')
    return m



def realaqi(url):
    response = session.get(url= url,headers = headers).text
    return response


def zonghe():
    timeArray = time.localtime(float(int(save_zong_excel()[6:-2])/1000))
    time_now = time.strftime('%Y',timeArray)+'年'+time.strftime('%m',timeArray)+'月'+time.strftime('%d',timeArray)+"日"+time.strftime('%H',timeArray)+'时'
    return time_now



def aqi():
    timeArray = time.localtime(float(int(save_aqi_excel()[6:-2]) / 1000))
    time_now = time.strftime('%Y', timeArray) + '年' + time.strftime('%m', timeArray) + '月' + time.strftime('%d',timeArray) + "日" + time.strftime('%H', timeArray) + '时'
    return time_now