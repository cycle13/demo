import time
import requests
import json
import xlwt
from decimal import Decimal


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





