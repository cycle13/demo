import requests
import datetime
import os
import time



session = requests.Session()
weatherchart_h1000_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_{1}0000000.jpg'
weatherchart_h925_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L92_P9_{1}0000000.jpg'
weatherchart_h850_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L85_P9_{1}0000000.jpg'
weatherchart_h700_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L70_P9_{1}0000000.jpg'
weatherchart_h500_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L50_P9_{1}0000000.jpg'
weatherchart_h200_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L20_P9_{1}0000000.jpg'
weatherchart_h100_url = 'http://image.nmc.cn/product/{0}/WESA/SEVP_NMC_WESA_SFER_EGH_ACWP_L10_P9_{1}0000000.jpg'

urlls = [weatherchart_h925_url,weatherchart_h850_url,weatherchart_h700_url,weatherchart_h500_url,weatherchart_h200_url,weatherchart_h100_url]
names = ['weatherchart_h925','weatherchart_h850','weatherchart_h700','weatherchart_h500','weatherchart_h200','weatherchart_h100']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def weatherchart_h1000():
    yestoday = (datetime.datetime.now() + datetime.timedelta(hours=-3)).strftime("%Y/%m/%d/%H")
    yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-11)).strftime("%Y/%m/%d/%H")
    url = weatherchart_h1000_url.format(yestodayl[0:10],yestodayl.replace('/',''))
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'weatherchart_h1000'):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'weatherchart_h1000')
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+'weatherchart_h1000'+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'.jpg', 'wb') as f:
        f.write(res.content)

def weatherchart_h925(urls,name):
    yestoday = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
    yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-17)).strftime("%Y/%m/%d/%H")
    url = urls.format(yestodayl[0:10], yestodayl.replace('/', ''))
    res = session.get(url, headers=headers)
    if not os.path.exists('data/' + yestoday[0:4] + '/' + yestoday[5:7] +  '/' + name):
        os.makedirs('data/' + yestoday[0:4] + '/' + yestoday[5:7] +  '/' + name)
    with open('data/' + yestoday[0:4] + '/' + yestoday[5:7] + '/' + name + '/' + yestoday[8:10]+"_"+yestoday[11:13] + '.jpg','wb') as f:
        f.write(res.content)



if __name__ == '__main__':
    date_time1 = ['02', '05', '08', '11', '14', '17', '20', '23']
    date_time2 = ['05', '17']
    while True:
        try:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H')
            if now_time in date_time1:
                print(now_time)
                weatherchart_h1000()
            if now_time in date_time2:
                for i in range(len(urlls)):
                    weatherchart_h925(urlls[i],names[i])
            time.sleep(3500)
        except:
            time.sleep(60)

