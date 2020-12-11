import time
import requests
import json
import xlwt
from decimal import *
from datetime import datetime


def save_location_excel():
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

    for i in range(10):
        sheet.write(n, 1, 2)
        sheet.write(n, 2, 2)

        sheet.write(n, 5, str(Decimal(1.00).quantize(Decimal('0.00'))))
        n+=1
    book.save(r'迎泽小时推送数据.xls')


save_location_excel()