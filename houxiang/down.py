from ftplib import FTP
import os

ftp= FTP('arlftp.arlhq.noaa.gov')
ftp.login()
ftp.cwd('/archives/gdas1')
localdir = r'D:\Program Files\pycharm\houxiang\Temp\arl'
fns = ['current7days.t00z','current7days.t06z','current7days.t12z','current7days.t18z']
for fn in fns:
    print('正在下载：'+fn)
    ftp.retrbinary('RETR %s' % fn,open(os.path.join(localdir,fn),'wb').write)

ftp.quit()
print('完成')