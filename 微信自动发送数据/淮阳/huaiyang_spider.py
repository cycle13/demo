import requests
import json
import time
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime
import os


session = requests.Session()
first_url = 'http://service.envicloud.cn:8082/v2/weatherhistory/ZGVTBZE0NDI5MDM0MJAZNDC=/'
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
url_aqi = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/realtimeAqiOfPT '
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}


def qi(station,datatime_n):
    url = first_url + station + '/' + datatime_n
    response = session.get(url=url, headers=headers).text
    return response


def realaqi(url):
    data = {
        '' : '',
        'sort': 'asc',
        'order': 'AQI',
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response


def real(url):
    response = session.get(url= url_list,headers = headers).text
    return response

def saveleiji_excel(excel_file_dir):
    book = xlwt.Workbook()
    sheet = book.add_sheet('淮阳县空气质量累积数据')
    n = 1
    sheet.write(0,0,'区县')
    sheet.write(0,1,'时间')
    sheet.write(0,2,'CO')
    sheet.write(0,3,'O3')
    sheet.write(0,4,'SO2')
    sheet.write(0,5,'NO2')
    sheet.write(0,6,'PM10')
    sheet.write(0,7,'PM2.5')
    time.sleep(5)
    l = realaqi(url_aqi)
    data = json.loads(l)['data']
    for k in data:
        if k['CITY'] in ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市']:
            sheet.write(n, 0, k['CITY'])
            try:
                sheet.write(n, 1, k["MONIDATE"].split(" ")[1])
            except:
                sheet.write(n, 1, "无")
            sheet.write(n, 2, k['AVGCO'])
            sheet.write(n, 3, k['AVGO3'])
            sheet.write(n, 4, k['AVGSO2'])
            sheet.write(n, 5, k['AVGNO2'])
            sheet.write(n, 6, k['AVGPM10'])
            sheet.write(n, 7, k['AVGPM25'])
            n+=1
    book.save(excel_file_dir)


def save_excel(excel_file_dir):
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
    time.sleep(5)
    l = real(url_list)
    data = json.loads(l)['detail']
    for k in data:
        if k['CITY'] in ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市']:
            sheet.write(n, 0, k['CITY'])
            try:
                sheet.write(n, 1, k["MONIDATE"].split(" ")[1])
            except:
                sheet.write(n, 1, "无")
            sheet.write(n, 2, k['CO'])
            sheet.write(n, 3, k['O3'])
            sheet.write(n, 4, k['SO2'])
            sheet.write(n, 5, k['NO2'])
            sheet.write(n, 6, k['PM10'])
            sheet.write(n, 7, k['PM25'])
            sheet.write(n, 8, k['AQI'])
            sheet.write(n, 9, k['PRIMARYPOLLUTANT'])
            n+=1
    book.save(excel_file_dir)


def save_date(line_date):
    my_datatime = datetime.strftime(datetime.now(),'%Y-%m-%d')
    print(my_datatime)
    l = real(url_list)
    data = json.loads(l)['detail']
    print(data)
    for k in data:
        if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
        # if k['CITY'] in ['淮阳县']:
            if not os.path.exists(line_date):
                os.makedirs(line_date)
            if not os.path.exists(line_date+'/'+k['CITY'] + my_datatime+".xls"):
                os.system(line_date+'/'+k['CITY'] + my_datatime+".xls")
                workbook = xlwt.Workbook(encoding='utf-8')
                worksheet = workbook.add_sheet('数据')
                worksheet.write(0,0,label = '日期')
                worksheet.write(0,1,label = 'SO2')
                worksheet.write(0,2,label = 'NO2')
                worksheet.write(0,3,label = 'PM2.5')
                worksheet.write(0,4,label = 'PM10')
                worksheet.write(0,5,label = 'CO')
                worksheet.write(0,6,label = 'O3')
                worksheet.write(0,7,label = 'AQI')
                worksheet.write(0,8,label = '首要污染物')
                workbook.save(line_date+'/'+k['CITY'] + my_datatime+".xls")
            n = int(datetime.strftime(datetime.now(),'%H'))
            rb = xlrd.open_workbook(line_date + '/' + k['CITY'] + my_datatime + ".xls")
            wb = copy(rb)
            sheet = wb.get_sheet(0)
            sheet.write(n+1,0,label = k["MONIDATE"])
            sheet.write(n+1,1,label = k['SO2'])
            sheet.write(n+1,2,label = k['NO2'])
            sheet.write(n+1,3,label = k['PM25'])
            sheet.write(n+1,4,label = k['PM10'])
            sheet.write(n+1,5,label = k['CO'])
            sheet.write(n+1,6,label = k['O3'])
            sheet.write(n+1,7,label = k['AQI'])
            sheet.write(n+1,8,label = k['PRIMARYPOLLUTANT'])
            excel_dir = line_date+'/'+k['CITY'] + my_datatime+".xls"
            os.remove(excel_dir)
            wb.save(excel_dir)

