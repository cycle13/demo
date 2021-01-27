import requests
import json
import pandas as pd
import xlwt
import time

session = requests.Session()
first_url = 'http://service.envicloud.cn:8082/v2/weatherhistory/ZGVTBZE0NDI5MDM0MJAZNDC=/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def qi(station,datatime_n,url):
    url = url + station + '/' + datatime_n
    response = session.get(url=url, headers=headers).text
    return response


def time_range(start_dat,end_day):
    # start = '2020-11-02-00', end = '2020-11-02-23'
    time_range = [x.strftime('%Y%m%d/%H') for x in list(pd.date_range(start=start_dat, end=end_day,freq="H"))]
    return time_range


def save_excel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('淮阳县气象数据')
    n = 1
    sheet.write(0,0,'updatetime')
    sheet.write(0,1,'phenomena')
    sheet.write(0,2,'humidity')
    sheet.write(0,3,'airpressure')
    sheet.write(0,4,'windpower')
    sheet.write(0,5,'feelst')
    sheet.write(0,6,'winddirect')
    sheet.write(0,7,'rain')
    sheet.write(0,8,'temperature')
    time.sleep(5)
    for i in time_range('2021-01-01-00', '2021-01-27-09'):
        l = qi("101181404", i, first_url)
        print(l)
        try:
            data = json.loads(l)
            sheet.write(n, 0, data['updatetime'])
            sheet.write(n, 1, data['phenomena'])
            sheet.write(n, 2, data['humidity'])
            sheet.write(n, 3, data['airpressure'])
            sheet.write(n, 4, data['windpower'])
            sheet.write(n, 5, data['feelst'])
            sheet.write(n, 6, data['winddirect'])
            sheet.write(n, 7, data['rain'])
            sheet.write(n, 8, data['temperature'])
            n+=1
        except:
            n += 1
            pass
    book.save('淮阳区气象数据.xls')

save_excel()

