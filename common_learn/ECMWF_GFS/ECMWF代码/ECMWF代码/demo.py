import requests
import datetime
import os
import time



session = requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}


data = ['mslp_uv850','z500a','z500_mslp','T850','T850a']
data2 = ['z500aMean']
data1 = ['mslpaNormMean']
datatime = ['00','12']
datatime1 = ['00']
urls = 'https://www.tropicaltidbits.com/analysis/models/ecmwf/{0}{2}/ecmwf_{1}_ea_{3}.png'

yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
today = datetime.datetime.now().strftime("%Y%m%d")


def ecmwf(data,datatime,num,yes):
    for j in data:
        for k in datatime:
            for i in range(1,num):
                url = urls.format(yes,j,k,str(i))
                print(url)
                res = session.get(url, headers=headers)
                if res.status_code == 200:
                    if not os.path.exists('ecmwf/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j):
                        os.makedirs('ecmwf/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j)
                    with open('ecmwf/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/' + yestoday[6:8] +k+'_'+str(i) + '.png','wb') as f:
                        f.write(res.content)


while True:
    try:
        ecmwf(data,datatime,12,yestoday)
    except:
        time.sleep(59)
    try:
        ecmwf(data1,datatime1,7,today)
    except:
        time.sleep(59)
    try:
        ecmwf(data2,datatime,7,yestoday)
    except:
        time.sleep(59)
    time.sleep(86300)