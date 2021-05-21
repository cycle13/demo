import requests
import datetime
import os
import time



session = requests.Session()
solid_url = 'http://image.nmc.cn/product/{0}/AMSM/medium/SEVP_NMC_AMSM_CAGMSS_ESRH_ACHN_L{2}CM_PS_{1}000000000.jpg'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def solid(name):
    yestoday = datetime.datetime.now().strftime("%Y/%m/%d")
    print(yestoday)
    url = solid_url.format(yestoday[0:10],yestoday.replace('/',''),name)
    print(url)
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'solid'+'_'+name):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'solid'+'_'+name)
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'solid'+'_'+name+'/'+yestoday[8:10]+"_"+"08"+'.jpg', 'wb') as f:
        f.write(res.content)





while True:
    try:
        for name in ['10','20','30','40','50']:
            solid(name)
        time.sleep(86400)
    except:
        pass