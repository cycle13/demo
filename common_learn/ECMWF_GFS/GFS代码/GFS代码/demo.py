import requests
import datetime
import os
import time



session = requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}


data = ['mslp_pcpn','mslp_pcpn_frzn','ref_frzn','apcpn']
data1 = ['apcpn24','asnow24','asnowd24']
data2 = ['asnow','asnowd','mslp_uv850','mslp_wind','T2ma','T2m','T850a','T850','cape']
data3 = ['wavehgt','waveper','pv330K','uv250','z500a','z500_vort','z500_mslp']
data4 = ['ir']
datatime = ['00','06','12','18']
urls = 'https://www.tropicaltidbits.com/analysis/models/gfs/{0}{2}/gfs_{1}_ea_{3}.png'

yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
today = datetime.datetime.now().strftime("%Y%m%d")


def gfs(data,datatime,num,yes):
    for j in data:
        for k in datatime:
            for i in range(1,num):
                url = urls.format(yes,j,k,str(i))
                print(url)
                res = session.get(url, headers=headers)
                if res.status_code == 200:
                    if not os.path.exists('gfs/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]):
                        os.makedirs('gfs/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8])
                    with open('gfs/' + yestoday[0:4] + '/' + yestoday[4:6] + '/' + j+ '/'+ yestoday[6:8]+ '/' + yestoday[6:8] +k+'_'+str(i) + '.png','wb') as f:
                        f.write(res.content)




gfs(data,datatime,65,yestoday)
gfs(data1,datatime,62,yestoday)
gfs(data2,datatime,66,yestoday)
gfs(data3,datatime,64,yestoday)
gfs(data4,datatime,21,yestoday)

while True:
    try:
        gfs(data,datatime,65,yestoday)
    except:
        time.sleep(59)
    try:
        gfs(data1,datatime,62,yestoday)
    except:
        time.sleep(59)
    try:
        gfs(data2,datatime,66,yestoday)
    except:
        time.sleep(59)
    try:
        gfs(data3,datatime,64,yestoday)
    except:
        time.sleep(59)
    try:
        gfs(data4,datatime,21,yestoday)
    except:
        time.sleep(59)
    time.sleep(86280)