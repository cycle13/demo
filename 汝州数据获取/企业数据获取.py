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
first_url = 'http://192.168.12.207:8020/env-base-info/ent_info/getNewestData'

headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}


def qi(url,num):
    data = {
        'areaCode':'',
        'entName':'',
        'entCode':'',
        'industryClassify':'',
        'orderBy':'',
        'page':str(num),
        'limit': '80',
    }
    response = session.post(url=url, data= data,headers=headers,timeout=10).text
    return response


def save_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('淮阳县空气质量累积数据')
    n = 1
    sheet.write(0,0,'entCode')
    sheet.write(0,1,'entName')
    sheet.write(0,2,'经度')
    sheet.write(0,3,'纬度')
    sheet.write(0,4,'区域代码')
    sheet.write(0,5,'区域名称')
    sheet.write(0,6,'industryCode')
    sheet.write(0,7,'industryName')
    sheet.write(0, 8, 'isPollutionSource')
    sheet.write(0, 9, 'pollutionType')
    sheet.write(0, 10, 'lagelPeople')
    sheet.write(0, 11, 'entAddress')
    sheet.write(0, 12, 'startDate')
    sheet.write(0, 13, 'registeredCapital')
    sheet.write(0, 14, 'status')
    sheet.write(0, 15, 'formerName')
    sheet.write(0, 16, 'englishName')
    sheet.write(0, 17, 'businessTerm')
    sheet.write(0, 18, 'businessScope')
    sheet.write(0, 19, 'entPerson')
    sheet.write(0, 20, 'personPhoneTel')
    sheet.write(0, 21, 'attentionNum')
    sheet.write(0, 22, 'isSewage')
    sheet.write(0, 23, 'pollutionTypeName')
    time.sleep(5)
    for num in range(1,9):
        l = qi(first_url,num)
        data = json.loads(l)['data']
        for k in data:
            sheet.write(n, 0, k['entCode'])
            sheet.write(n, 1, k['entName'])
            sheet.write(n, 2, k['lon'])
            sheet.write(n, 3, k['lat'])
            sheet.write(n, 4, k['areaCode'])
            sheet.write(n, 5, k['areaName'])
            sheet.write(n, 6, k['industryCode'])
            sheet.write(n, 7, k['industryName'])
            sheet.write(n, 8, k['isPollutionSource'])
            sheet.write(n, 9, k['pollutionType'])
            sheet.write(n, 10, k['lagelPeople'])
            sheet.write(n, 11, k['entAddress'])
            sheet.write(n, 12, k['startDate'])
            sheet.write(n, 13, k['registeredCapital'])
            sheet.write(n, 14, k['status'])
            sheet.write(n, 15, k['formerName'])
            sheet.write(n, 16, k['englishName'])
            sheet.write(n, 17, k['businessTerm'])
            sheet.write(n, 18, k['businessScope'])
            sheet.write(n, 19, k['entPerson'])
            sheet.write(n, 20, k['personPhoneTel'])
            sheet.write(n, 21, k['attentionNum'])
            sheet.write(n, 22, k['isSewage'])
            sheet.write(n, 23, k['pollutionTypeName'])
            n+=1
    book.save('汝州企业.xls')

save_excel()