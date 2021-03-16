import requests
import datetime
import os
import time


session = requests.Session()

#14
ncep_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_NCEP_NWPR_SNCEP_ECONC_ASIA_L88_PB_{1}000000000.gif'
# 15
jma_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_JMA_NWPR_ASDS_ECONC_ASIA_L88_PB_{1}120000000.gif'
ecmwf_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_ECMWF_NWPR_ASDS_ECONC_ASIA_L88_PB_{1}000000000.gif'
ens_url = 'http://image.nmc.cn/product/{0}/DDMA/SEVP_NMC_DDMA_SMMEF_ESSW_ASIA_L88_PB_{1}000000000.gif'
# 16
cma_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_NMC_NWPR_ASDS_ECONC_ASIA_L88_PB_{1}000000000.gif'
kma_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_KMA_NWPR_ASDS_ECONC_ASIA_L88_PB_{1}000000000.gif'
fmi_url = 'http://image.nmc.cn/product/{0}/NWPR/SEVP_FMI_NWPR_ASDS_ECONC_ASIA_L88_PB_{1}000000000.gif'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def solid(urll,name,yestoday):
    url = urll.format(yestoday[0:10],yestoday.replace('/',''),name)
    print(url)
    res = session.get(url,headers=headers)
    if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name):
        os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name)
    with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name+'/'+yestoday[8:10]+'.gif', 'wb') as f:
        f.write(res.content)


while True:
    name = ['ncep','jma','ecmwf','ensemble','cma','kma','fmi']
    url = [ncep_url,jma_url,ecmwf_url,ens_url,cma_url,kma_url,fmi_url]
    for i in range(len(url)):
        if name[i] == 'ncep':
            yestoday = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y/%m/%d")
            solid(url[i], name[i], yestoday)
        elif name[i] in ['jma','ecmwf','ensemble']:
            yestoday = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y/%m/%d")
            solid(url[i], name[i], yestoday)
        elif name[i] in ['cma','kma','fmi']:
            yestoday = datetime.datetime.now().strftime("%Y/%m/%d")
            solid(kma_url,name[i],yestoday)
        else:
            pass
    time.sleep(86400)