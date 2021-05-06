import time
import requests
import json
import xlwt
from decimal import *
from datetime import datetime



def save_to_excel(res):
    book = xlwt.Workbook()
    sheet = book.add_sheet('探空数据')
    lx = ['vt', 'lat', 'lon', 'ELEV_0', 'TMP_2', 'RH_2', 'UGRD_10', 'VGRD_10', 'PRES_0', 'LFTX_0', 'CAPE_0', 'PWAT_0','HLCY_3000', 'USTM_6000', 'VSTM_6000', 'CAPE_180', 'CAPE_255',
          'HGT_1000', 'TMP_1000', 'RH_1000', 'UGRD_1000','VGRD_1000',
          'HGT_975', 'UGRD_975', 'VGRD_975', 'TMP_975', 'RH_975',
          'HGT_950', 'UGRD_950', 'VGRD_950', 'TMP_950','RH_950',
          'HGT_925', 'UGRD_925', 'VGRD_925', 'TMP_925', 'RH_925',
          'HGT_900', 'UGRD_900', 'VGRD_900', 'TMP_900','RH_900',
          'HGT_875', 'UGRD_875', 'VGRD_875', 'TMP_875', 'RH_875',
          'HGT_850', 'UGRD_850', 'VGRD_850', 'TMP_850','RH_850',
          'HGT_825', 'UGRD_825', 'VGRD_825', 'TMP_825', 'RH_825',
          'HGT_800', 'UGRD_800', 'VGRD_800', 'TMP_800','RH_800',
          'HGT_775', 'UGRD_775', 'VGRD_775', 'TMP_775', 'RH_775',
          'HGT_750', 'UGRD_750', 'VGRD_750', 'TMP_750','RH_750',
          'HGT_725', 'UGRD_725', 'VGRD_725', 'TMP_725', 'RH_725',
          'HGT_700', 'UGRD_700', 'VGRD_700', 'TMP_700','RH_700',
          'HGT_675', 'UGRD_675', 'VGRD_675', 'TMP_675', 'RH_675',
          'HGT_650', 'UGRD_650', 'VGRD_650', 'TMP_650','RH_650',
          'HGT_625', 'UGRD_625', 'VGRD_625', 'TMP_625', 'RH_625',
          'HGT_600', 'UGRD_600', 'VGRD_600', 'TMP_600','RH_600',
          'HGT_575', 'UGRD_575', 'VGRD_575', 'TMP_575', 'RH_575',
          'HGT_550', 'UGRD_550', 'VGRD_550', 'TMP_550','RH_550',
          'HGT_525', 'UGRD_525', 'VGRD_525', 'TMP_525', 'RH_525',
          'HGT_500', 'UGRD_500', 'VGRD_500', 'TMP_500','RH_500',
          'HGT_475', 'UGRD_475', 'VGRD_475', 'TMP_475', 'RH_475',
          'HGT_450', 'UGRD_450', 'VGRD_450', 'TMP_450','RH_450',
          'HGT_425', 'UGRD_425', 'VGRD_425', 'TMP_425', 'RH_425',
          'HGT_400', 'UGRD_400', 'VGRD_400', 'TMP_400','RH_400',
          'HGT_375', 'UGRD_375', 'VGRD_375', 'TMP_375', 'RH_375',
          'HGT_350', 'UGRD_350', 'VGRD_350', 'TMP_350','RH_350',
          'HGT_325', 'UGRD_325', 'VGRD_325', 'TMP_325', 'RH_325',
          'HGT_300', 'UGRD_300', 'VGRD_300', 'TMP_300','RH_300',
          'HGT_275', 'UGRD_275', 'VGRD_275', 'TMP_275', 'RH_275',
          'HGT_250', 'UGRD_250', 'VGRD_250', 'TMP_250','RH_250',
          'HGT_225', 'UGRD_225', 'VGRD_225', 'TMP_225', 'RH_225',
          'HGT_200', 'UGRD_200', 'VGRD_200', 'TMP_200','RH_200',
          'HGT_175', 'UGRD_175', 'VGRD_175', 'TMP_175', 'RH_175',
          'HGT_150', 'UGRD_150', 'VGRD_150', 'TMP_150','RH_150',
          'HGT_125', 'UGRD_125', 'VGRD_125', 'TMP_125', 'RH_125',
          'HGT_100', 'UGRD_100', 'VGRD_100', 'TMP_100', 'RH_100',]
    n = 1
    ll = len(lx)
    for l in range(ll):
        sheet.write(0, l, lx[l])
    m = 0
    for k in res:
        for l in range(ll):
            sheet.write(n, l, k[lx[l]])
        n+=1
    book.save(r'探空数据1.xls')




def save_to_excelqi(res):
    book = xlwt.Workbook()
    sheet = book.add_sheet('探空数据')
    lx = ['APCP_0','CAPE_0','CSNOW_0','DPT_2','ELEV_0','GUST_0','PRMSL_0','SNOD_0','TCDC_boundary','TCDC_high','TCDC_low','TCDC_mid','TCDC_total','TMP_2','TMP_850','UGRD_10','UNIX_TIMESTAMP(vt)','VGRD_10']
    n = 1
    ll = len(lx)
    for l in range(ll):
        sheet.write(0, l, lx[l])
    m = 0
    for k in res:
        for l in range(ll):
            if lx[l]=='UNIX_TIMESTAMP(vt)':
                xx = time.localtime(int(k[lx[l]]))
                timell = time.strftime("%Y-%m-%d %H:%M:%S",xx)
                sheet.write(n, l, timell)
            else:
                sheet.write(n, l, k[lx[l]])
        n+=1
    book.save(r'气象数据1.xls')
