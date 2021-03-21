import requests
import datetime
import os
import time



session = requests.Session()


chinaall_url = 'http://image.nmc.cn/product/{0}/WXBL/medium/SEVP_NSMC_WXBL_FY4A_ETCC_ACHN_LNO_PY_{1}{2}00000.JPG'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def FY4A_true_color():
    yestoday = (datetime.datetime.now() + datetime.timedelta(minutes=-20)).strftime("%Y/%m/%d/%H/%M")
    if yestoday[-2:] == '45' or '49' or '53':
        yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
    else:
        yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-8)).strftime("%Y/%m/%d/%H")
    print(yestoday)
    url = chinaall_url.format(yestodayl[0:10],yestodayl.replace('/',''),yestoday[-2:])
    print(url)
    res = session.get(url,headers=headers)
    print(type(res.status_code))
    if res.status_code == 200:
        if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'FY4A_true_color'):
            os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'FY4A_true_color')
        with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'FY4A_true_color'+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'_'+yestoday[14:]+'.jpg', 'wb') as f:
            f.write(res.content)





while True:
    data_time = ['05','09','13','20','35','39','43','50','54','58']
    try:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%M')
        if now_time in data_time:
            print(now_time)
            FY4A_true_color()
        time.sleep(59)
    except:
        time.sleep(59)