#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 14:33
# @Author  : Yanjun Wang
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

import requests
import json
import xlwt
import xlrd


session = requests.Session()
book = xlwt.Workbook()
sheet = book.add_sheet('企业')
n = 1
sheet.write(0,0,'name')
sheet.write(0,1,'lon')
sheet.write(0,2,'lat')
sheet.write(0,3,'addr')
for i in range(1,100):
    try:
        res = session.get('https://restapi.amap.com/v3/place/text?keywords=化工企业&city=taiyuan&output=json&offset=100&page={}&key=8ca198a8ae0f83242d99062676df301f&extensions=all'.format(i))
        data = json.loads(res.text)
        print(data)
        if data['count'] == '0':
            break
        for dat in data['pois']:
            sheet.write(n, 0, dat['name'])
            sheet.write(n, 1, dat['location'].split(',')[0])
            sheet.write(n, 2, dat['location'].split(',')[1])
            sheet.write(n, 3, dat['address'])
            print(dat['name'],dat['location'],dat['address'])
            n+=1
    except:
        pass

book.save('太原市企业.xls')