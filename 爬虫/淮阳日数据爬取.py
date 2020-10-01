import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

def day(url,timess):
    data = {
        'sort':'asc',
        'time':timess
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

time_range = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start='2020-09-25', end='2020-9-26'))]
book = xlwt.Workbook()
sheet = book.add_sheet('淮阳县空气质量数据')
n = 1
sheet.write(0,0,'区县')
sheet.write(0,1,'时间')
sheet.write(0,2,'CO')
sheet.write(0,3,'O3')
sheet.write(0,4,'SO2')
sheet.write(0,5,'NO2')
sheet.write(0,6,'PM10')
sheet.write(0,7,'PM2.5')
sheet.write(0,8,'AQI')
sheet.write(0,9,'首要污染物')

for i in time_range:
    time.sleep(5)
    l = day(first_url_day,str(i))
    data = json.loads(l)['data']
    for k in data:
        if k['city'] in ['淮阳县']:
            sheet.write(n, 0, k['city'])
            sheet.write(n, 1, str(i))
            sheet.write(n, 2, k['co'])
            sheet.write(n, 3, k['o3'])
            sheet.write(n, 4, k['so2'])
            sheet.write(n, 5, k['no2'])
            sheet.write(n, 6, k['pm10'])
            sheet.write(n, 7, k['pm25'])
            sheet.write(n, 8, k['aqi'])
            sheet.write(n, 9, k['primary'])
            n+=1
            print(str(i),k)
    print(l)

book.save('data.xls')