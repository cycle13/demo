import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
first_url = 'https://hepp.zc12369.com/api/pollute_map/air_quality_city?time='
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'hepp.zc12369.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}

time_range = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start='2021-01-11', end='2021-01-11'))]
book = xlwt.Workbook()
sheet = book.add_sheet('周口市各区县数据')
n = 1
sheet.write(0,0,'ID')
sheet.write(0,1,'时间')
sheet.write(0,2,'PM10')
sheet.write(0,3,'PM2.5')
sheet.write(0,4,'SO2')
sheet.write(0,5,'NO2')
sheet.write(0,6,'CO')
sheet.write(0,7,'O3')
sheet.write(0,8,'AQI')
sheet.write(0,9,'首要污染物')
sheet.write(0,10,'综合指数')
sheet.write(0,11,'空气质量等级')

for i in time_range:
    for j in range(0,17):
        try:
            time.sleep(5)
            url = first_url+str(i)+'+'+str(j)+ '%3A00'
            response = session.get(url,headers = headers).text
            data = json.loads(response)
            res = data['data']
            for k in res:
                if k['id'] in ['411626','411628','411627','411681','411624','411622','411621','411625','411602','411623',]:
                    sheet.write(n, 0, k['areaAllName'])
                    sheet.write(n, 1, k['updateTime'])
                    sheet.write(n, 2, k['pm10'])
                    sheet.write(n, 3, k['pm25'])
                    sheet.write(n, 4, k['so2'])
                    sheet.write(n, 5, k['no2'])
                    sheet.write(n, 6, k['co'])
                    sheet.write(n, 7, k['o3'])
                    sheet.write(n, 8, k['aqi'])
                    sheet.write(n, 9, k['mainPol'])
                    sheet.write(n, 10, k['zonghezhishu'])
                    sheet.write(n, 11, k['dataLevel'])
                    n+=1
                    print(k)
            # print(res)
        except:
            print('数据异常')
            time.sleep(30)

book.save('2021年1月11日小时数据.xls')