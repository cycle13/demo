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



def save_zong_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0,1,'站点名称')
    sheet.write(0,2,'综合指数')
    sheet.write(0,3,'SO2')
    sheet.write(0, 4, 'NO2')
    sheet.write(0, 5, 'CO')
    sheet.write(0, 6, 'O3')
    sheet.write(0, 7, 'PM2.5')
    sheet.write(0, 8, 'PM10')
    sheet.write(0, 9, 'AQI')
    sheet.write(0,10,'首要污染物')
    sheet.write(0, 11, '类别')
    time.sleep(5)
    l = realaqi(hour_local_url)
    data = json.loads(l)
    for k in data:
        if k['RegionName'] in ['迎泽区','万柏林区','晋源区','杏花岭区','小店区','尖草坪区']:
            sheet.write(n, 1, k['RegionName'])
            sheet.write(n, 2, Decimal(k["SO2"] / 60 + k["NO2"] / 40 + k["PM10"] / 70 + k["CO"] / 4 + k["O3"] / 160 + k["PM25"] / 35).quantize(Decimal("0.00")))
            sheet.write(n, 3, k["SO2"])
            sheet.write(n, 4, k["NO2"])
            sheet.write(n, 5, Decimal(k["CO"]).quantize(Decimal("0.0")))
            sheet.write(n, 6, k["O3"])
            sheet.write(n, 7, k["PM25"])
            sheet.write(n, 8, k["PM10"])
            sheet.write(n, 9, k["AQIScore"])
            sheet.write(n, 10, k["TopPollution"])
            sheet.write(n, 11, k['PollutionLevelBig']+'级')
            n+=1
            m = k['Time']
    book.save(r'excelfiles\迎泽小时推送数据.xlsx')
    return m



def realaqi(url):
    response = session.get(url= url,headers = headers).text
    return response


def zonghe():
    timeArray = time.localtime(float(int(save_zong_excel()[6:-2])/1000))
    time_now = time.strftime('%Y',timeArray)+'年'+time.strftime('%m',timeArray)+'月'+time.strftime('%d',timeArray)+"日"+time.strftime('%H',timeArray)+'时'
    return time_now


