from ftplib import FTP
import os
import pandas as pd
import datetime


ftp= FTP('ftp.ptree.jaxa.jp')
ftp.login('pumpsim_163.com','SP+wari8')
localdir = r'D:\Program Files\pycharm\常规学习\葵花卫星AOD\data'
ln = ['00','10','20','30','40','50']
for x in list(pd.date_range(start='2021-05-22', end='2021-05-24',freq='H')):
    fns = []
    dt = x.strftime('%Y%m%d')
    dll = x.strftime('%Y%m')
    dl = x.strftime('%d')
    d = x.strftime('%H')
    ftp.cwd('/pub/himawari/L2/ARP/030/{}/{}/{}'.format(dll,dl,d))
    for k in ln:
        fns.append('NC_H08_{}_{}{}_L2ARP030_FLDK.02401_02401.nc'.format(dt,d,k))
    for fn in fns:
        print('正在下载：'+fn)
        try:
            ftp.retrbinary('RETR %s' % fn,open(os.path.join(localdir,fn),'wb').write)
        except:
            print('error')

ftp.quit()
print('完成')