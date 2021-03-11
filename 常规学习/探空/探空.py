import requests
import time
import os
import pandas as pd



session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
urls = 'http://weather.uwyo.edu/upperair/images/{0}{1}.{2}.bskewt.png'
urll = 'http://weather.uwyo.edu/cgi-bin/bufrraob.py?datetime={0}%20{1}:00:00&id={2}&type=PNG:SKEWT'
station = ['54511','57516','59758']
dt = ['00','12']
begin = '2018-01-01'
end = '2021-03-10'
time_range = [x.strftime('%Y%m%d') for x in list(pd.date_range(start=begin, end=end))]
try:
    for i in time_range:
        for k in station:
            time.sleep(3)
            for j in dt:
                url = urls.format(i,j,k)
                print(url)
                urlss = urll.format(i[0:4]+'-'+i[4:6]+'-'+i[6:8],j,k)
                res = session.get(urlss, headers=headers).text
                time.sleep(3)
                res = session.get(url,headers=headers)
                print(res)
                if not os.path.exists('data/'+i[0:4]+'/'+i[4:6]+'/'+k):
                    os.makedirs('data/'+i[0:4]+'/'+i[4:6]+'/'+k)
                with open('data/'+i[0:4]+'/'+i[4:6]+'/'+k+'/'+ i[6:8]+j+'-'+k + '.png', 'wb') as f:
                    f.write(res.content)
except:
    time.sleep(3)




