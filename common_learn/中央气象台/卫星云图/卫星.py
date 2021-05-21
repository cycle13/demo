import requests
import datetime
import os
import time



session = requests.Session()


FY4A_ETCC = 'http://image.nmc.cn/product/{0}/WXBL/medium/SEVP_NSMC_WXBL_{3}_ACHN_LNO_PY_{1}{2}00000.JPG'
FY4A_EC012 = 'http://image.nmc.cn/product/{0}/WXBL/medium/SEVP_NSMC_WXBL_{3}_ACHN_LNO_PY_{1}{2}00000.JPG'
FY4A_EC001 = 'http://image.nmc.cn/product/{0}/WXBL/medium/SEVP_NSMC_WXBL_{3}_ACHN_LNO_PY_{1}{2}00000.JPG'
FY4A_EC009 = 'http://image.nmc.cn/product/{0}/WXBL/medium/SEVP_NSMC_WXBL_{3}_ACHN_LNO_PY_{1}{2}00000.JPG'
names = {'FY4A_ETCC':FY4A_ETCC,'FY4A_EC012':FY4A_EC012,'FY4A_EC001':FY4A_EC001,'FY4A_EC009':FY4A_EC009}

CORN_FY2G_EVL = 'http://image.nmc.cn/product/{0}/CORN/medium/SEVP_NSMC_{3}_ACHN_LNO_PY_{1}{2}00000.JPG'

namesss = {'CORN_FY2G_EVL':CORN_FY2G_EVL}

FY2G_url = 'http://image.nmc.cn/product/{0}/{3}/medium/SEVP_NSMC_{2}_ACHN_LNO_PY_{1}0000000.JPG'

namess = ['WXCL_FY2G_EWVP','WXCL_FY2G_EIR1','WXCL_FY2G_EIR2','WXCL_FY2G_EVL','WXCL_FY2G_EMIR','WXBL_FY2G_ECN','WXBL_FY2G_EIR1','WXBL_FY2G_EIR2','WXBL_FY2G_EMIR','WXBL_FY2G_EWVP','WXBL_FY2G_EVL']


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
def FY4A_true_color(name,yestoday,yestodayl):
    url = names[name].format(yestodayl[0:10],yestodayl.replace('/',''),yestoday[-2:],name)
    print(url)
    res = session.get(url,headers=headers)
    print(type(res.status_code))
    if res.status_code == 200:
        if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name):
            os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name)
        with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'_'+yestoday[14:]+'.jpg', 'wb') as f:
            f.write(res.content)


def WXCL_FY2G(name,yestodayl,yestoday):
    url = FY2G_url.format(yestodayl[0:10],yestodayl.replace('/',''),name,name[0:4])
    print(url)
    res = session.get(url,headers=headers)
    print(type(res.status_code))
    if res.status_code == 200:
        if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name):
            os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name)
        with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'_'+yestoday[14:]+'.jpg', 'wb') as f:
            f.write(res.content)



def CORN_FY2G_EVL(name,yestoday,yestodayl):
    url = namesss[name].format(yestodayl[0:10],yestodayl.replace('/',''),yestoday[-2:],name)
    print(url)
    res = session.get(url,headers=headers)
    print(type(res.status_code))
    if res.status_code == 200:
        if not os.path.exists('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name):
            os.makedirs('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name)
        with open('data/'+yestoday[0:4]+'/'+yestoday[5:7]+'/'+name+'/'+yestoday[8:10]+"_"+yestoday[11:13]+'_'+yestoday[14:]+'.jpg', 'wb') as f:
            f.write(res.content)



while True:
    data_time = ['00','04','08','15','19','23','30','45','49','53']
    try:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%M')
        if now_time in data_time:
            print(now_time)
            yestoday = (datetime.datetime.now() + datetime.timedelta(minutes=-30)).strftime("%Y/%m/%d/%H/%M")
            if yestoday[-2:] == '30' or '34' or '38' or '45' or '49' or '53':
                yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
            else:
                yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-8)).strftime("%Y/%m/%d/%H")
            for i in names:
                print(names[i])
                FY4A_true_color(i,yestoday,yestodayl)
        if now_time == '00':
            for i in namess:
                yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
                yestoday = (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime("%Y/%m/%d/%H")
                WXCL_FY2G(i, yestodayl, yestoday)

        if now_time in ['15','45']:
            yestoday = (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime("%Y/%m/%d/%H/%M")
            yestodayl = (datetime.datetime.now() + datetime.timedelta(hours=-9)).strftime("%Y/%m/%d/%H")
            for i in namesss:
                print(namesss[i])
                CORN_FY2G_EVL(i, yestoday, yestodayl)
        time.sleep(59)
    except:
        time.sleep(59)