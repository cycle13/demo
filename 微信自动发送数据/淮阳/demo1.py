import requests
import json
import time
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime
import os
import datetime as datatime


session = requests.Session()
hour24_t = 'http://1.192.88.18:8007/api/v1/ChinaAir/get24History/411627'
hour24_h = 'http://1.192.88.18:8007/api/v1/ChinaAir/get24History/411626'

headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}


def qi(url):
    response = session.get(url=url, headers=headers).text
    return response


def save_excel(excel_file_dir,hour24_h,name):
    if not os.path.exists(excel_file_dir):
        os.makedirs(excel_file_dir)
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
    sheet.write(0,8,'AQI')
    sheet.write(0,9,'空气质量等级')
    sheet.write(0,10,'星期')
    time.sleep(5)
    l = qi(hour24_h)
    data = json.loads(l)
    for k in data:
        sheet.write(n, 0, k['city'])
        sheet.write(n, 1, k["update_time"][8:-6].replace('T','日')+'时')
        sheet.write(n, 2, k['co'])
        sheet.write(n, 3, k['o3'])
        sheet.write(n, 4, k['so2'])
        sheet.write(n, 5, k['no2'])
        sheet.write(n, 6, k['pm10'])
        sheet.write(n, 7, k['pm25'])
        sheet.write(n, 8, k['aqi'])
        sheet.write(n, 9, k['level'])
        sheet.write(n, 10, k['weekDay'])
        n+=1
    book.save(excel_file_dir+'/'+name)



def data_h(excel_file_dir):
    save_excel(excel_file_dir,hour24_h, '淮阳县.xls')

def data_t(excel_file_dir):
    save_excel(excel_file_dir,hour24_t, '太康县.xls')

# data_h(excel_file_dir)