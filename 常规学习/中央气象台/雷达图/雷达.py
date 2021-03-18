import requests
import datetime
import os
import time



session = requests.Session()
chinaall_url = 'http://image.nmc.cn/product/{0}/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_ACHN_L88_PI_{1}{2}00001.PNG'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def chinaall():
    yestoday = (datetime.datetime.now() + datetime.timedelta(minutes=-10)).strftime("%Y/%m/%d/%H/%M")
    if yestoday[-2:] == '54':
        yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
    else:
        yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-8)).strftime("%Y/%m/%d/%H")
    print(yestoday)
    url = chinaall_url.format(yestodayl[0:10],yestodayl.replace('/',''),yestoday[-2:])
    print(url)
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'chinaall'):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'chinaall')
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'chinaall'+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'_'+yestoday[14:]+'.jpg', 'wb') as f:
        f.write(res.content)





while True:
    data_time = ['04','10','16','22','28','34','40','46','52','58']
    try:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%M')
        if now_time in data_time:
            print(now_time)
            chinaall()
        time.sleep(59)
    except:
        time.sleep(59)