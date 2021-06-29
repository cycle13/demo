import requests
import time
import os
import pandas as pd



session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
urls = 'http://weather.uwyo.edu/upperair/images/{0}{1}.{2}.b{3}.png'
urll = 'http://weather.uwyo.edu/cgi-bin/bufrraob.py?datetime={0}%20{1}:00:00&id={2}&type=PNG:{3}'
station = ['50527', '50557', '50774', '50953', '51076', '51431', '51463', '51644', '51709', '51777','51828', '51839', '52203', '52267', '52323', '52418', '52533', '52681', '52818', '52836', '52866', '52983', '53068', '53463', '53513', '53614', '53772', '53845', '53915', '54102', '54135', '54161', '54218', '54292', '54374', '54511', '54662', '54727', '54857', '55299', '55591', '56029', '56080', '56146', '56187', '56691', '56739', '56778', '56964', '56985', '57083', '57127', '57131', '57178', '57447', '57461', '57494', '57516', '57687', '57749', '57816', '57957', '57972', '57993', '58027', '58150', '58203', '58238', '58362', '58424', '58457', '58606', '58633', '58665', '58725', '58847', '59134', '59211', '59265', '59280', '59316', '59431', '59758']
dt = ['00','12']
png = ['SKEWT','STUVE','STUVE10']
begin = '2020-01-01'
end = '2021-03-10'
time_range = [x.strftime('%Y%m%d') for x in list(pd.date_range(start=begin, end=end))]

for i in time_range:
    for k in station:
        for j in dt:
            for n in png:
                try:
                    url = urls.format(i, j, k,n.lower())
                    urlss = urll.format(i[0:4] + '-' + i[4:6] + '-' + i[6:8], j, k, n)
                    res = session.get(urlss, headers=headers).text
                    time.sleep(1)
                    res = session.get(url, headers=headers)
                    print(res)
                    if not os.path.exists('data/'+i[0:4]+'/'+i[4:6]+'/'+k+'/'+n):
                        os.makedirs('data/'+i[0:4]+'/'+i[4:6]+'/'+k+'/'+n)
                    with open('data/'+i[0:4]+'/'+i[4:6]+'/'+k+'/'+n+'/'+ i[6:8]+'-'+j+'-'+k + '.png', 'wb') as f:
                        f.write(res.content)
                    time.sleep(1)
                except:
                    time.sleep(3)




