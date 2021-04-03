import requests
import json
import csv
import time
time_stamp = int(time.time())
url = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?convert=USD&slug=bitcoin&time_end={time_stamp}&time_start=1367107200"
rd = requests.get(url = url)
# 返回的数据是 JSON 格式，使用 json 模块解析
co = json.loads(rd.content)
list1 = co['data']['quotes']

with open('data/BTC.csv','w' ,encoding='utf8',newline='') as f:
    csvi = csv.writer(f)
    csv_head = ["date","price","volume"]
    csvi.writerow(csv_head)

    for i in list1:
        quote_date = i["time_open"][:10]
        quote_price = "{:.2f}".format(i["quote"]["USD"]["close"])
        quote_volume = "{:.2f}".format(i["quote"]["USD"]["volume"])
        csvi.writerow([quote_date, quote_price, quote_volume])