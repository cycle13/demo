#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 16:32
# @Author  : Yanjun Wang
# @Site    : 
# @File    : down1.py
# @Software: PyCharm

import os
import sys
import click
import ftplib
import ntpath
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta

def files_list(d1, d2, tstep, product):
    files = []
    step = timedelta(minutes=tstep)
    seconds = (d2-d1).total_seconds()
    # generate basenames
    for i in range(0, int(seconds), int(step.total_seconds())):
        files.append(d1 + timedelta(seconds=i))
    # get all files from sdate to edate by tstep
    files = [date.strftime('%Y%m/%d/%H/') +
             f'*H08_{date.strftime("%Y%m%d_%H%M")}_*_FLDK*nc'
             for date in files]
    return files

def downloadFiles(ftp, source, product, file, destination, debug):
    # omit 'bet' version
    files = [os.path.basename(f) for f in ftp.nlst(source+product) if os.path.basename(f).isdigit()]
    # get the newest version
    version = sorted(files, key=lambda x: float(x))[-1]
    try:
        ftp.cwd(os.path.dirname(source+product+'/'+version+'/'+file))
    except OSError:
        pass
    except ftplib.error_perm:
        print('Error: could not change to ' + os.path.dirname(source+product+'/'+version+'/'+file))
        return 0
    filename = ntpath.basename(file)
    try:
        filename = ftp.nlst(filename)[0]
        ftp.sendcmd('TYPE I')
        filesize = ftp.size(filename)
        # create directory
        if not os.path.exists(os.path.dirname(destination)):
            os.makedirs(os.path.dirname(destination))
        # download data
        with open(os.path.dirname(destination)+'/'+filename, 'wb') as f:
            # set progress bar
            def file_write(data):
                f.write(data)
            ftp.retrbinary('RETR ' + filename, file_write)
            if debug > 0:
                print('Downloaded')
    except:
        print('Error: File could not be downloaded ' + filename)
        return 0
    return 1

def main(save_path, sdate, edate, tstep, product, username, password, debug):
    server = 'ftp.ptree.jaxa.jp'  # JAXA data server
    source = '/pub/himawari/L2/'
    save_path = os.path.join(save_path, "")
    # get the list of datetime from sdate to edate by day
    d1 = datetime.strptime(sdate, '%Y-%m-%d_%H:%M')
    d2 = datetime.strptime(edate, '%Y-%m-%d_%H:%M')
    # get filenames based on dates
    files = files_list(d1, d2, tstep, product)
    ftp = ftplib.FTP(server)
    ftp.login(username, password)
    for file in tqdm(files, desc='total progress'):
        # iterate and download files
        filename = ntpath.basename(file)
        destination = os.path.join(save_path+file)
        if debug > 0:
            print('Downloading ' + filename + ' ...')
        file_exist = downloadFiles(ftp, source, product, file, destination, debug)
        # skip following steps if file isn't found
        if not file_exist:
            continue



# 下载Cloud Property (CLP)产品
if __name__ == '__main__':
    main('./data','2021-07-02_00:00','2021-07-02_23:50',10,'ARP','pumpsim_163.com','SP+wari8',1)
