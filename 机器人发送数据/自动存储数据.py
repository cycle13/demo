import requests
import json
import time
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime
import os



session = requests.Session()
def real(url):
    response = session.get(url= url_list,headers = headers).text
    return response


url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}


def save_date():
    my_datatime = datetime.strftime(datetime.now(),'%Y-%m-%d')
    print(my_datatime)
    l = real(url_list)
    data = json.loads(l)['detail']
    print(data)
    for k in data:
        if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
        # if k['CITY'] in ['淮阳县']:
            if not os.path.exists('excelfiles/'+my_datatime):
                os.makedirs('excelfiles/'+my_datatime)
            if not os.path.exists('excelfiles/'+my_datatime+'/'+k['CITY'] + my_datatime+".xls"):
                os.system('excelfiles/'+my_datatime+'/'+k['CITY'] + my_datatime+".xls")
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
                workbook.save('excelfiles/'+my_datatime+'/'+k['CITY'] + my_datatime+".xls")
            n = int(datetime.strftime(datetime.now(),'%H'))
            rb = xlrd.open_workbook('excelfiles/' + my_datatime + '/' + k['CITY'] + my_datatime + ".xls")
            wb = copy(rb)
            sheet = wb.get_sheet(0)
            sheet.write(n,0,label = k["MONIDATE"])
            sheet.write(n,1,label = k['SO2'])
            sheet.write(n,2,label = k['NO2'])
            sheet.write(n,3,label = k['PM25'])
            sheet.write(n,4,label = k['PM10'])
            sheet.write(n,5,label = k['CO'])
            sheet.write(n,6,label = k['O3'])
            sheet.write(n,7,label = k['AQI'])
            sheet.write(n,8,label = k['PRIMARYPOLLUTANT'])
            os.remove('excelfiles/'+my_datatime+'/'+k['CITY'] + my_datatime+".xls")
            wb.save('excelfiles/'+my_datatime+'/'+k['CITY'] + my_datatime+".xls")



save_date()
