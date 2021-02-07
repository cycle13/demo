import json
import xlwt
import requests


session = requests.Session()
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

urll = 'https://hepp.zc12369.com/api/airwise-api/{}%2000:00/{}%2023:00/{}/{}/hour-data'
start = '2021-01-01'
end = '2021-02-03'
lon = '112.550864'
lat = '37.890277'
url = urll.format(start,end,lon,lat)

def spider_qi():
    response = session.get(url,headers=headers).text
    print(response)
    data = json.loads(response)
    return data

def save_excel_all():
    book = xlwt.Workbook()
    sheet = book.add_sheet('气象数据')
    n = 1
    sheet.write(0,0,'时间')
    sheet.write(0,1,'经度')
    sheet.write(0,2,'纬度')
    sheet.write(0, 3, 'AQI')
    sheet.write(0, 4, 'CO')
    sheet.write(0, 5, 'NO2')
    sheet.write(0, 6, 'PM2_5')
    sheet.write(0, 7, 'PM10')
    sheet.write(0, 8, 'SO2')
    sheet.write(0, 9, 'O3')
    sheet.write(0, 10, 'VIS')
    sheet.write(0, 11, 'rh')
    sheet.write(0, 12, 'wind_dir')
    sheet.write(0, 13, 'wind_speed')
    sheet.write(0, 14, 'pslv')
    sheet.write(0, 15, 'temp')
    sheet.write(0, 16, 'mainPol')
    sheet.write(0, 17, 'swd')
    sheet.write(0, 18, 'rn')
    sheet.write(0, 19, 'level')
    sheet.write(0, 20, 'lowTemp')
    sheet.write(0, 21, 'highTemp')
    j = spider_qi()
    data = j['data']
    for k in data:
        sheet.write(n, 0, data[k]['data_time'])
        sheet.write(n, 1, lon)
        sheet.write(n, 2, lat)
        sheet.write(n, 3, data[k]['AQI'])
        sheet.write(n, 4, data[k]['CO'])
        sheet.write(n, 5, data[k]['NO2'])
        sheet.write(n, 6, data[k]['PM2_5'])
        sheet.write(n, 7, data[k]['PM10'])
        sheet.write(n, 8, data[k]['SO2'])
        sheet.write(n, 9, data[k]['O3'])
        sheet.write(n, 10, data[k]['VIS'])
        sheet.write(n, 11, data[k]['rh'])
        sheet.write(n, 12, data[k]['wind_dir'])
        sheet.write(n, 13, data[k]['wind_speed'])
        sheet.write(n, 14, data[k]['pslv'])
        sheet.write(n, 15, data[k]['temp'])
        sheet.write(n, 16, data[k]['mainPol'])
        sheet.write(n, 17, data[k]['swd'])
        sheet.write(n, 18, data[k]['rn'])
        sheet.write(n, 19, data[k]['level'])
        sheet.write(n, 20, data[k]['lowTemp'])
        sheet.write(n, 21, data[k]['highTemp'])
        n+=1
    book.save('all_data.xls')


def save_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('气象数据')
    n = 1
    sheet.write(0,0,'时间')
    sheet.write(0,1,'wind_x')
    sheet.write(0,2,'wind_s')
    j = spider_qi()
    data = j['data']
    for k in data:
        sheet.write(n, 0, data[k]['data_time'])
        sheet.write(n, 1, data[k]["wind_dir"])
        sheet.write(n, 2, data[k]['wind_speed'])
        n+=1
    book.save('data.xls')

save_excel()
# save_excel_all()