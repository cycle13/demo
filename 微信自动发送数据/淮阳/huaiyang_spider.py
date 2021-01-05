import requests
import json
import time
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime
import os
import datetime as datatime
from lxml import etree


session = requests.Session()
qi_url = 'https://tianqi.moji.com/weather/china/henan/huaiyangdistrict'
aqi_url = 'https://tianqi.moji.com/aqi/china/henan/huaiyangdistrict'
hour24 = 'http://1.192.88.18:8007/api/v1/ChinaAir/get24History/411627'
first_url = 'http://service.envicloud.cn:8082/v2/weatherhistory/ZGVTBZE0NDI5MDM0MJAZNDC=/'
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
url_aqi = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/realtimeAqiOfPT'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}


def qi(station,datatime_n):
    url = first_url + station + '/' + datatime_n
    response = session.get(url=url, headers=headers,timeout=10).text
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


# 更换数据源后的数据
def save_excel1(excel_file_dir):
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
    sheet.write(0, 8, 'AQI')
    sheet.write(0, 9, '首要污染物')
    sheet.write(0, 10, 'PM2.5排名')
    sheet.write(0, 11, 'PM10排名')
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





# 之前的数据
# def save_excel(excel_file_dir):
#     book = xlwt.Workbook()
#     sheet = book.add_sheet('淮阳县空气质量数据')
#     n = 1
#     sheet.write(0,0,'区县')
#     sheet.write(0,1,'时间')
#     sheet.write(0,2,'CO')
#     sheet.write(0,3,'O3')
#     sheet.write(0,4,'SO2')
#     sheet.write(0,5,'NO2')
#     sheet.write(0,6,'PM10')
#     sheet.write(0,7,'PM2.5')
#     sheet.write(0,8,'AQI')
#     sheet.write(0,9,'首要污染物')
#     sheet.write(0, 10, 'PM2.5排名')
#     sheet.write(0, 11, 'PM10排名')
#     time.sleep(5)
#     l = real(url_list)
#     data = json.loads(l)['detail']
#     for k in data:
#         if k['CITY'] in ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市']:
#             sheet.write(n, 0, k['CITY'])
#             try:
#                 sheet.write(n, 1, k["MONIDATE"].split(" ")[1])
#             except:
#                 sheet.write(n, 1, "无")
#             sheet.write(n, 2, k['CO'])
#             sheet.write(n, 3, k['O3'])
#             sheet.write(n, 4, k['SO2'])
#             sheet.write(n, 5, k['NO2'])
#             sheet.write(n, 6, k['PM10'])
#             sheet.write(n, 7, k['PM25'])
#             sheet.write(n, 8, k['AQI'])
#             sheet.write(n, 9, k['PRIMARYPOLLUTANT'])
#
#             if k['CITY'] =='淮阳县':
#                 x = 0
#                 for l in k['STATIONS']:
#                     sheet.write(n, 12+x, l['STATIONNAME'])
#                     sheet.write(n, 13+x, l['PM10'])
#                     sheet.write(n, 14+x, l['PM25'])
#                     x+=3
#             n += 1
#     book.save(excel_file_dir)


def save_date1(line_date):
    my_datatime = (datetime.now() + datatime.timedelta(hours=-1)).strftime("%Y-%m-%d")
    print(my_datatime)
    l = realaqi(url_aqi)
    data = json.loads(l)['data']
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
                worksheet.write(0, 9, label='时间')
                workbook.save(line_date+'/'+k['CITY'] + my_datatime+".xls")
            # n = int(datetime.strftime(datetime.now(),'%H'))
            n = int((datetime.now() + datatime.timedelta(hours=-1)).strftime("%H"))
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
            for i in range(0,n+1):
                sheet.write(i+1, 9, label=str(i)+'时')
            excel_dir = line_date+'/'+k['CITY'] + my_datatime+".xls"
            os.remove(excel_dir)
            wb.save(excel_dir)

# 用的之前数据源
# def save_date(line_date):
#     my_datatime = datetime.strftime(datetime.now(),'%Y-%m-%d')
#     print(my_datatime)
#     l = real(url_list)
#     data = json.loads(l)['detail']
#     print(data)
#     for k in data:
#         if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
#         # if k['CITY'] in ['淮阳县']:
#             if not os.path.exists(line_date):
#                 os.makedirs(line_date)
#             if not os.path.exists(line_date+'/'+k['CITY'] + my_datatime+".xls"):
#                 os.system(line_date+'/'+k['CITY'] + my_datatime+".xls")
#                 workbook = xlwt.Workbook(encoding='utf-8')
#                 worksheet = workbook.add_sheet('数据')
#                 worksheet.write(0,0,label = '日期')
#                 worksheet.write(0,1,label = 'SO2')
#                 worksheet.write(0,2,label = 'NO2')
#                 worksheet.write(0,3,label = 'PM2.5')
#                 worksheet.write(0,4,label = 'PM10')
#                 worksheet.write(0,5,label = 'CO')
#                 worksheet.write(0,6,label = 'O3')
#                 worksheet.write(0,7,label = 'AQI')
#                 worksheet.write(0,8,label = '首要污染物')
#                 worksheet.write(0, 9, label='时间')
#                 workbook.save(line_date+'/'+k['CITY'] + my_datatime+".xls")
#             n = int(datetime.strftime(datetime.now(),'%H'))
#             rb = xlrd.open_workbook(line_date + '/' + k['CITY'] + my_datatime + ".xls")
#             wb = copy(rb)
#             sheet = wb.get_sheet(0)
#             sheet.write(n+1,0,label = k["MONIDATE"])
#             sheet.write(n+1,1,label = k['SO2'])
#             sheet.write(n+1,2,label = k['NO2'])
#             sheet.write(n+1,3,label = k['PM25'])
#             sheet.write(n+1,4,label = k['PM10'])
#             sheet.write(n+1,5,label = k['CO'])
#             sheet.write(n+1,6,label = k['O3'])
#             sheet.write(n+1,7,label = k['AQI'])
#             sheet.write(n+1,8,label = k['PRIMARYPOLLUTANT'])
#             for i in range(0,n+1):
#                 sheet.write(i+1, 9, label=str(i)+'时')
#             excel_dir = line_date+'/'+k['CITY'] + my_datatime+".xls"
#             os.remove(excel_dir)
#             wb.save(excel_dir)



def year(url,yestoday):
    data = {
        'end':yestoday,
        'sort':'asc',
        'start':'2021-01-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    print(response)
    return response


def yearleiji(excel_file_dir):
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    l = year(first_url_year,yestoday)
    data = json.loads(l)['data']
    print(data)
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
        if k['city'] in ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市']:
            sheet.write(n, 0, k['city'])
            sheet.write(n, 1, k['co'])
            sheet.write(n, 2, k['o3'])
            sheet.write(n, 3, k['so2'])
            sheet.write(n, 4, k['no2'])
            sheet.write(n, 5, k['pm10'])
            sheet.write(n, 6, k['pm25'])
            sheet.write(n, 7, k['zong'])
            n+=1
    book.save(excel_file_dir)


def save_hn_date1(line_date):
    my_datatime = (datetime.now() + datatime.timedelta(hours=-1)).strftime("%Y-%m-%d")
    print(my_datatime)
    l = realaqi(url_aqi)
    data = json.loads(l)['data']
    print(data)
    for k in data:
        try:
            # if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
            # if k['CITY'] in ['淮阳县']:
            if not os.path.exists(line_date):
                os.makedirs(line_date)
            if not os.path.exists(line_date+'/'+k['CITY'] + ".xls"):
                os.system(line_date+'/'+k['CITY'] + ".xls")
                print(k['CITY'])
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
                worksheet.write(0, 9, label='时间')
                workbook.save(line_date+'/'+k['CITY'] + ".xls")
            # n = int(datetime.strftime(datetime.now(),'%H'))
            n = int((datetime.now() + datatime.timedelta(hours=-1)).strftime("%H"))
            rb = xlrd.open_workbook(line_date + '/' + k['CITY'] + ".xls")
            wb = copy(rb)
            sheet = wb.get_sheet(0)
            sheet.write(n+1,0,label = k['MONIDATE'])
            sheet.write(n+1,1,label = k['SO2'])
            sheet.write(n+1,2,label = k['NO2'])
            sheet.write(n+1,3,label = k['PM25'])
            sheet.write(n+1,4,label = k['PM10'])
            sheet.write(n+1,5,label = k['CO'])
            sheet.write(n+1,6,label = k['O3'])
            sheet.write(n+1,7,label = k['AQI'])
            sheet.write(n+1,8,label = k['PRIMARYPOLLUTANT'])
            for i in range(0,n+1):
                sheet.write(i+1, 9, label=str(i)+'时')
            excel_dir = line_date+'/'+k['CITY'] +".xls"
            os.remove(excel_dir)
            wb.save(excel_dir)
        except:
            pass


# save_hn_date1("line_date")
# def save_hn_date(line_date):
#     my_datatime = datetime.strftime(datetime.now(),'%Y-%m-%d')
#     print(my_datatime)
#     l = real(url_list)
#     data = json.loads(l)['detail']
#     print(data)
#     for k in data:
#         # if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
#         # if k['CITY'] in ['淮阳县']:
#         if not os.path.exists(line_date):
#             os.makedirs(line_date)
#         if not os.path.exists(line_date+'/'+k['CITY'] + ".xls"):
#             os.system(line_date+'/'+k['CITY'] + ".xls")
#             workbook = xlwt.Workbook(encoding='utf-8')
#             worksheet = workbook.add_sheet('数据')
#             worksheet.write(0,0,label = '日期')
#             worksheet.write(0,1,label = 'SO2')
#             worksheet.write(0,2,label = 'NO2')
#             worksheet.write(0,3,label = 'PM2.5')
#             worksheet.write(0,4,label = 'PM10')
#             worksheet.write(0,5,label = 'CO')
#             worksheet.write(0,6,label = 'O3')
#             worksheet.write(0,7,label = 'AQI')
#             worksheet.write(0,8,label = '首要污染物')
#             worksheet.write(0, 9, label='时间')
#             workbook.save(line_date+'/'+k['CITY'] + ".xls")
#         n = int(datetime.strftime(datetime.now(),'%H'))
#         rb = xlrd.open_workbook(line_date + '/' + k['CITY'] + ".xls")
#         wb = copy(rb)
#         sheet = wb.get_sheet(0)
#         sheet.write(n+1,0,label = k["MONIDATE"])
#         sheet.write(n+1,1,label = k['SO2'])
#         sheet.write(n+1,2,label = k['NO2'])
#         sheet.write(n+1,3,label = k['PM25'])
#         sheet.write(n+1,4,label = k['PM10'])
#         sheet.write(n+1,5,label = k['CO'])
#         sheet.write(n+1,6,label = k['O3'])
#         sheet.write(n+1,7,label = k['AQI'])
#         sheet.write(n+1,8,label = k['PRIMARYPOLLUTANT'])
#         for i in range(0,n+1):
#             sheet.write(i+1, 9, label=str(i)+'时')
#         excel_dir = line_date+'/'+k['CITY'] +".xls"
#         os.remove(excel_dir)
#         wb.save(excel_dir)


def qixiang():
    response = session.get(url=qi_url, headers=headers)
    response.encoding = "utf-8"
    res = response.text
    html = etree.HTML(res)
    shidu = html.xpath('//div[@class="wea_about clearfix"]/span/text()')[0]
    fengji = html.xpath('//div[@class="wea_about clearfix"]/em/text()')[0]
    wendu = html.xpath('//div[@class="wea_weather clearfix"]/em/text()')[0]
    return shidu,fengji,wendu


# url = 'https://page.henan.gov.cn/api/stt-weather'
# res = session.post(url).text
# print(res)