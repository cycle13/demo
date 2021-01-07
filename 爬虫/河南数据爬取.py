import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
url_aqi = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/realtimeAqiOfPT'
headers = {
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/LIO-AN00)',
    'Content-Length': '19',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Host': '1.192.88.18:8115'

}

def year(url):
    data = {
        'end':'2019-12-31',
        'sort':'asc',
        'start':'2019-06-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    print(response)
    return response

def month(url):
    data = {
        'sort':'asc',
        'month':'2019-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

def day(url):
    data = {
        'sort':'asc',
        'time':'2020-09-27'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

def real(url):
    response = session.get(url= url_list,headers = headers).text
    return response
    # data = json.loads(l)['detail']
    # for i in data:
    #     print(i)

def realaqi(url):
    data = {
        '' : '',
        'sort': 'asc',
        'order': 'AQI',
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response
    # data = json.loads(l)['detail']
    # for i in data:
    #     print(i)

l = year(first_url_year)
data = json.loads(l)['data']
book = xlwt.Workbook()
sheet = book.add_sheet('周口市各区县数据')
n = 1
sheet.write(0,0,'区县')
sheet.write(0,1,'CO')
sheet.write(0,2,'O3')
sheet.write(0,3,'SO2')
sheet.write(0,4,'NO2')
sheet.write(0,5,'PM10')
sheet.write(0,6,'PM2.5')
sheet.write(0,7,'综合指数')
for k in data:
    if k['city'] in ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市','港区',]:
        sheet.write(n, 0, k['city'])
        sheet.write(n, 1, k['co'])
        sheet.write(n, 2, k['o3'])
        sheet.write(n, 3, k['so2'])
        sheet.write(n, 4, k['no2'])
        sheet.write(n, 5, k['pm10'])
        sheet.write(n, 6, k['pm25'])
        sheet.write(n, 7, k['zong'])
        n+=1

book.save('全年2019年考核期年数据.xls')

print(data)

