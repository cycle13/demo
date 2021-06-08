import requests
import datetime
import os
import time


session = requests.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
data = ['mslp_pcpn']
data1 = ['mslp_uv850','z500a','z500_mslp']
datatime = ['00','06','12','18']
urls = 'https://www.tropicaltidbits.com/analysis/models/navgem/{0}{2}/navgem_{1}_ea_{3}.png'
yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")


def navgem(data,datatime,num,yes):
    for j in data:
        for k in datatime:
            for i in range(1,num):
                url = urls.format(yes,j,k,str(i))
                print(url)
                res = session.get(url, headers=headers)
                if res.status_code == 200:
                    if not os.path.exists('navgem/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]):
                        os.makedirs('navgem/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8])
                    with open('navgem/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]+ '/' + yestoday[6:8] +k+'_'+str(i) + '.png','wb') as f:
                        f.write(res.content)


while True:
    try:
        navgem(data,datatime,25,yestoday)
    except:
        time.sleep(59)
    try:
        navgem(data1,datatime,26,yestoday)
    except:
        time.sleep(59)
    time.sleep(86280)