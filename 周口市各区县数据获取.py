import requests
import pandas as pd
import time


session = requests.Session()
# first_url = 'https://hepp.zc12369.com/api/pollute_map/air_quality_city?time=2020-01-21+11%3A00'
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

time_range = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start='2019-9-11', end='2019-9-12'))]
# response = session.get(first_url).text
# print(response)

for i in time_range:
    for j in range(0,24):
        time.sleep(5)
        url = first_url+str(i)+'+'+str(j)+ '%3A00'
        response = session.get(url,headers = headers).text
        print(response)