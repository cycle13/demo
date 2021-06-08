import requests
import datetime
import os
import time


session = requests.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
data = ['mslp_pcpn','mslp_pcpn_frzn','apcpn','asnow']
data1 = ['asnow24']
data2 = ['uv850','mslp_wind','uv250','z500a','z500_vort','z500_mslp','ir','T850','T850a','T2m','T2ma']
datatime = ['00','12']
urls = 'https://www.tropicaltidbits.com/analysis/models/gem/{0}{2}/gem_{1}_ea_{3}.png'
yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")


def cmc(data,datatime,num,yes):
    for j in data:
        for k in datatime:
            for i in range(1,num):
                url = urls.format(yes,j,k,str(i))
                print(url)
                res = session.get(url, headers=headers)
                if res.status_code == 200:
                    if not os.path.exists('cmc/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]):
                        os.makedirs('cmc/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8])
                    with open('cmc/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]+ '/' + yestoday[6:8] +k+'_'+str(i) + '.png','wb') as f:
                        f.write(res.content)


while True:
    try:
        cmc(data,datatime,41,yestoday)
    except:
        time.sleep(59)
    try:
        cmc(data1,datatime,38,yestoday)
    except:
        time.sleep(59)
    try:
        cmc(data2,datatime,42,yestoday)
    except:
        time.sleep(59)
    time.sleep(86280)