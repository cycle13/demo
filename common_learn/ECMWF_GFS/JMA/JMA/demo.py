import requests
import datetime
import os
import time


session = requests.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
data = ['z500_mslp','mslp_uv850','T850','T850a']
data1 = ['apcpn']
data2 = ['uv250','z500a','z500_vort']
datatime = ['00','12']
urls = 'https://www.tropicaltidbits.com/analysis/models/jma/{0}{2}/jma_{1}_ea_{3}.png'
yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")

def jma(data,datatime,num,yes):
    for j in data:
        for k in datatime:
            for i in range(1,num):
                url = urls.format(yes,j,k,str(i))
                print(url)
                res = session.get(url, headers=headers)
                if res.status_code == 200:
                    if not os.path.exists('jma/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]):
                        os.makedirs('jma/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8])
                    with open('jma/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]+ '/' + yestoday[6:8] +k+'_'+str(i) + '.png','wb') as f:
                        f.write(res.content)



while True:
    try:
        jma(data,datatime,10,yestoday)
    except:
        time.sleep(59)
    try:
        jma(data1,datatime,9,yestoday)
    except:
        time.sleep(59)
    try:
        jma(data2,datatime,7,yestoday)
    except:
        time.sleep(59)
    time.sleep(86280)