import requests
import datetime
import os
import time



session = requests.Session()
seaplatform_url = 'http://image.nmc.cn/product/{0}/APWF/medium/SEVP_NMC_APWF_SOB_EQ2_ACHN_L89_P9_{1}0000000.jpg'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def seaplatform():
    yestoday = datetime.datetime.now().strftime("%Y/%m/%d/%H")
    print(yestoday)
    url = seaplatform_url.format(yestoday[0:10],yestoday.replace('/',''))
    print(url)
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'seaplatform'):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'seaplatform')
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'seaplatform'+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'.jpg', 'wb') as f:
        f.write(res.content)





while True:
    try:
        seaplatform()
        time.sleep(3600)
    except:
        time.sleep(60)