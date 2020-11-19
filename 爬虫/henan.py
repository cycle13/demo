import requests
import pandas as pd
import json
import xlwt
import time


session = requests.Session()
headers = {
    'Host': 'page.henan.gov.cn',
    'Origin': 'http://sthjt.henan.gov.cn',
    'Referer': 'http://sthjt.henan.gov.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'

}



url = 'https://page.henan.gov.cn/api/stt-weather'


def year(url):
    data = {
        'time':'2020-11-19 17:00 ',
    }
    response = session.post(url= url,data=data,headers = headers).text
    print(response)
    return response

year(url)