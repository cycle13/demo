from ftplib import FTP
import sys
import os
import re

def ftpconnet(ftpserver,port,username,password):#连接ftp服务器
    ftp = FTP()
    try:
        ftp.connect(ftpserver,port)
    except:
        print('FTP connect failed!')

    try:
        ftp.login(username,password)
    except:
        print('FTP login failed!')
    else:
        return ftp

def ftpdownload(ftp,ori_path,dest_path):
    for each in ftp.nlst(ori_path):
        try:
            ftp.cwd(each)                                                   #检测该目录是否还含有下级目录，若有，将该路径设为新路径重复操作
        except:
            print('aaa')
            filename = re.search('\S+\/(\S+)',each).group(1) #获取文件名，这是将each与【一个或多个非空字符+\+（一个或多个非空字符）】的形式                                                                                       #匹配并返回括号内形式的内容，search只返回第一个符合的结果
            local_file = dest_path + '/' + filename
            if os.path.exists(local_file):
                lsize = os.stat(local_file).st_size
                rsize = ftp.size(each)
                if lsize > rsize:
                    sys.stderr.write('the local file %s is bigger than the remote!\n'%local_file)
                    return False
                elif lsize == rsize:
                    sys.stderr.write('the file %s has been completed!\n'%local_file)
                bufsize = 1024 * 1024
                fp = open(local_file,'ab')
                ftp.retrbinary('RETR '+each,fp.write,bufsize,rest=lsize)
            else:
                bufsize = 1024 * 1024
                fp = open(local_file,'wb')
                ftp.retrbinary('RETR '+each,fp.write,bufsize)
        else:
            dirname = re.search('\S+\/(\S+)',each).group(1) #当检测到还有下级目录时也创建相应的目录
            dirname = dest_path + '/' + dirname + '/'
            os.system('mkdir -p %s'%dirname)
            ftpdownload(ftp,each,dirname)

def ftpclose(ftp):
    ftp.quit()

if __name__ == '__main__':
    ftp = ftpconnet('arlftp.arlhq.noaa.gov',21,'','')
    ftpdownload(ftp,'/pub/archives/gdas1','data') #样例是下载noaa的风暴路径数据
    ftpclose(ftp)