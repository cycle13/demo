import requests
import datetime
import os
import time



session = requests.Session()
temperature_url = 'http://image.nmc.cn/product/{0}/STFC/medium/SEVP_NMC_STFC_SFER_ET0_ACHN_L88_PB_{1}0000000.jpg'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def temperature():
    yestoday = datetime.datetime.now().strftime("%Y/%m/%d/%H")
    yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-8)).strftime("%Y/%m/%d/%H")
    print(yestoday)
    url = temperature_url.format(yestodayl[0:10],yestodayl.replace('/',''))
    print(url)
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'temperature'):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'temperature')
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'temperature'+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'.jpg', 'wb') as f:
        f.write(res.content)




temperature()
# while True:
#     try:
#         now_time = datetime.datetime.strftime(datetime.datetime.now(),'%M')
#         if now_time == '50':
#             print(now_time)
#             temperature()
#         time.sleep(60)
#     except:
#         time.sleep(60)