import os
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
    # return float(xl['temp'])/10,float(xl['dp_demp'])/10,float(xl['Pressure'])/10,float(xl['WindDirection']),float(xl['WindSpeed']/10)
    return float(xl['temp'])/10