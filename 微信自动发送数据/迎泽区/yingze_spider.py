import time
import requests
import json
import xlwt
from decimal import *
from datetime import datetime
from lxml import etree


session = requests.Session()
qi_url = 'https://tianqi.moji.com/weather/china/shanxi/yingze-district'
aqi_url = 'https://tianqi.moji.com/aqi/china/shanxi/yingze-district'
hour_local_std_url = 'http://www.ty.daqi110.com/tyAirService/pust/postData?areaCode=1401&areaType=2&dataTime={}+{}%3A00%3A00&dataType=1&flag=3&isControlPoint=2&stationType=1'
hour_station_url = 'http://183.203.223.83:85/ReleaseMap/GetListAndViewByCityCode?RegionId=140101'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def realaqi(hour_local_std_url):
    res = session.get(hour_local_std_url,headers=headers).text
    res = res.replace('NA', '-')
    data = json.loads(res)
    # if '小店区' not in data:
    #     realaqi(hour_local_std_url)
    return data


def save_location_excel(url):
    book = xlwt.Workbook()
    sheet = book.add_sheet('太原市六城区空气质量数据')
    n = 1
    sheet.write(0, 0, '排名')
    sheet.write(0, 1, '点位名称')
    sheet.write(0, 2, '综合指数')
    sheet.write(0, 3, 'SO2')
    sheet.write(0, 4, 'NO2')
    sheet.write(0, 5, 'CO')
    sheet.write(0, 6, 'O3')
    sheet.write(0, 7, 'PM2.5')
    sheet.write(0, 8, 'PM10')
    sheet.write(0, 9, 'AQI')
    sheet.write(0, 10, '首要污染物')
    sheet.write(0, 11, '类别')
    sheet.write(0, 12, '优良')
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
        if ((k["so2"] == '-') or (k["no2"] == '-') or (k["co"] == '-') or (k["o31"] == '-') or (k["pm25"] == '-') or (k["pm10"] == '-')):
            sheet.write(n, 2, None)
        else:
            sheet.write(n, 2, str(Decimal(k["totalIndex"]).quantize(Decimal('0.00'))))
        sheet.write(n, 3, k["so2"])
        sheet.write(n, 4, k["no2"])
        sheet.write(n, 5, str(Decimal(k["co"]).quantize(Decimal('0.0'))))
        sheet.write(n, 6, k["o31"])
        sheet.write(n, 7, k["pm25"])
        sheet.write(n, 8, k["pm10"])
        if k["aqi"] == '-':
            sheet.write(n, 9, None)
        else:
            sheet.write(n, 9, k["aqi"])
        sheet.write(n, 10, k["primaryPollutant"])
        sheet.write(n, 11, k['airQualityLevel'])
        sheet.write(n, 12, k['airQualityType'])
        n += 1
        now_datetime = k['dataTime']
    book.save(r'excelfiles\迎泽小时推送数据.xls')
    return now_datetime


def data(hour_local_std_url):
    now_data = datetime.strftime(datetime.now(),'%Y-%m-%d')
    now_time = datetime.strftime(datetime.now(),'%H')
    hour_local_std_url = hour_local_std_url.format(now_data,now_time)
    x = save_location_excel(hour_local_std_url)
    return x


def location():
    timeArray = data(hour_local_std_url)
    time_now = datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%Y')+'年'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%m')+'月'+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%d')+"日"+datetime.strptime(timeArray, '%Y-%m-%d %H:%M:%S').strftime('%H')+'时'
    return time_now


def qixiang():
    response = session.get(url=qi_url, headers=headers)
    response.encoding = "utf-8"
    res = response.text
    html = etree.HTML(res)
    shidu = html.xpath('//div[@class="wea_about clearfix"]/span/text()')[0]
    fengji = html.xpath('//div[@class="wea_about clearfix"]/em/text()')[0]
    response = session.get(url=aqi_url, headers=headers)
    response.encoding = "utf-8"
    res = response.text
    html = etree.HTML(res)
    aqi = html.xpath('//div[@class="aqi_info_detail"]/span/text()')[0]
    if aqi == '优':
        aqi = '一级'+aqi
    if aqi == '良':
        aqi = '二级'+aqi
    if aqi == '轻度污染':
        aqi = '三级'+aqi
    if aqi == '中度污染':
        aqi = '四级'+aqi
    if aqi == '中度污染':
        aqi = '五级'+aqi
    if aqi == '严重污染':
        aqi = '六级'+aqi
    return shidu,fengji,aqi

