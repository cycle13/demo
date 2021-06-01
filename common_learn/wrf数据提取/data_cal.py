import os
import math
import pandas as pd


def station(station,year,month,day,hour):
    path = 'qixiang_data/{}0-99999-2020'.format(station)
    fs = open(path,'r')
    fl = fs.read()
    fl = fl.replace(' ',',')
    fl = fl.replace(',,',',')
    fl = fl.replace(',,',',')
    fl = fl.replace(',,',',')
    fl = fl.replace(',,',',')
    fl = fl.replace(',,',',')
    fs.close()
    path = os.path.join('qixiang_data/{}0-99999-2020.txt'.format(station))
    fobj = open(path,'w')
    fobj.write(fl)
    fobj.close()
    f = pd.read_table(path,sep=',', names=['year','month','day','hour','temp','dp_demp','Pressure','WindDirection','WindSpeed','SkyCode','LiquidOne','LiquidSix'])
    xl = f[(f['year'].isin([year]))&(f['month'].isin([month]))&(f['day'].isin([day]))&(f['hour'].isin([hour]))]
    return float(xl['temp'])/10,float(xl['dp_demp'])/10,float(xl['Pressure'])/10,float(xl['WindSpeed']/10)*math.sin((float(xl['WindDirection'])/180)*math.pi),float(xl['WindSpeed']/10)*math.cos((float(xl['WindDirection'])/180)*math.pi)



def station_l(year,month,day,hour):
    path = 'excel_csv/2020年1-2月.xls'
    f = pd.read_excel(path)
    xl = f[(f['时间'].isin([year+'-'+month+'-'+day+' '+hour+':00']))&(f['站点名称'].isin(['东寨港']))]
    return float(xl['气温']),float(xl['湿度']),float(xl['气压']),float(xl['风速'])*math.sin((float(xl['风向'])/180)*math.pi),float(xl['风速'])*math.cos((float(xl['风向'])/180)*math.pi)

def station_lp(lp):
    path = 'excel_csv/2020年1-2月.xls'
    f = pd.read_excel(path)
    xl = f[(f['时间'].isin([lp]))&(f['站点名称'].isin(['东寨港']))]
    return float(xl['气温']),float(xl['湿度']),float(xl['气压']),float(xl['风速'])*math.sin((float(xl['风向'])/180)*math.pi),float(xl['风速'])*math.cos((float(xl['风向'])/180)*math.pi)