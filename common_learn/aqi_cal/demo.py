import pandas as pd

def ll(num,name):
    k = 0
    data = pd.read_excel('aqi_help.xlsx')
    for i in range(len(data)):
        if num<=data[name].tolist()[i]:
            k = i
            break
    iaqi = (data['cal'].tolist()[k]-data['cal'].tolist()[k-1])*(num-data[name].tolist()[k-1])/(data[name].tolist()[k]-data[name].tolist()[k-1])+data['cal'].tolist()[k-1]
    return round(iaqi)

def cal_aqi(path):
    data = pd.read_excel(path)
    datafile = pd.DataFrame()
    for name in ['O3','NO2','SO2','PM10','PM2.5','CO']:
        datafile[name] = data[name].apply(ll,args=(name,))
    data['AQI'] = datafile.max(axis=1)
    data.to_excel('demo.xlsx',index=False)

cal_aqi('demo.xls')