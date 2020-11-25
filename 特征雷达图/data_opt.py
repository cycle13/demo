import pandas as pd



def tezheng(file_dir,newfile_dir,now_time):
    df = pd.read_excel(file_dir)
    # 计算占比
    df['CO_sum'] = df['CO']/(df['SO2']+df['NO2']+df['PM2.5']+df['PM10']+df['CO'])
    df['SO2_sum'] = df['SO2']/(df['SO2']+df['NO2']+df['PM2.5']+df['PM10']+df['CO'])
    df['NO2_sum'] = df['NO2']/(df['SO2']+df['NO2']+df['PM2.5']+df['PM10']+df['CO'])
    df['PM2.5_sum'] = df['PM2.5']/(df['SO2']+df['NO2']+df['PM2.5']+df['PM10']+df['CO'])
    df['PM10_sum'] = df['PM10']/(df['SO2']+df['NO2']+df['PM2.5']+df['PM10']+df['CO'])
    # 计算占比均值
    co_mean = df['CO_sum'].mean()
    so2_mean = df['SO2_sum'].mean()
    no2_mean = df['NO2_sum'].mean()
    pm25_mean = df['PM2.5_sum'].mean()
    pm10_mean = df['PM10_sum'].mean()
    # 计算占比标准差
    co_std = df['CO_sum'].std()
    so2_std = df['SO2_sum'].std()
    no2_std = df['NO2_sum'].std()
    pm25_std = df['PM2.5_sum'].std()
    pm10_std = df['PM10_sum'].std()
    # 计算占比上限
    co_mean_up = (co_mean+co_std)/co_mean
    so2_mean_up = (so2_mean+so2_std)/so2_mean
    no2_mean_up = (no2_mean+no2_std)/no2_mean
    pm25_mean_up = (pm25_mean+pm25_std)/pm25_mean
    pm10_mean_up = (pm10_mean+pm10_std)/pm10_mean
    # 计算占比下限
    co_mean_down = (co_mean-co_std)/co_mean
    so2_mean_down = (so2_mean-so2_std)/so2_mean
    no2_mean_down = (no2_mean-no2_std)/no2_mean
    pm25_mean_down = (pm25_mean-pm25_std)/pm25_mean
    pm10_mean_down = (pm10_mean-pm10_std)/pm10_mean
    # 计算要绘制图对应日期的占比
    CO_sum = df[df.时间 == now_time]['CO_sum']/co_mean
    SO2_sum= df[df.时间 == now_time]['SO2_sum']/so2_mean
    NO2_sum = df[df.时间 == now_time]['NO2_sum']/no2_mean
    PM25_sum = df[df.时间 == now_time]['PM2.5_sum']/pm25_mean
    PM10_sum = df[df.时间 == now_time]['PM10_sum']/pm10_mean
    # 写成列表准备写入excel文件
    # a = [[so2_mean,no2_mean,co_mean,pm25_mean,pm10_mean],
    #  [so2_std,no2_std,co_std,pm25_std,pm10_std],
    #  [so2_mean_up,no2_mean_up,co_mean_up,pm25_mean_up,pm10_mean_up],
    #  [so2_mean_down,no2_mean_down,co_mean_down,pm25_mean_down,pm10_mean_down ],
    #  [float(SO2_sum),float(NO2_sum),float(CO_sum) ,float(PM25_sum),float(PM10_sum)],
    #      [1,1,1,1,1]]
    a = [
     [so2_mean_up,pm10_mean_up,pm25_mean_up,co_mean_up,no2_mean_up],
     [so2_mean_down,pm10_mean_down,pm25_mean_down,co_mean_down,no2_mean_down ],
     [float(SO2_sum),float(PM10_sum),float(PM25_sum),float(CO_sum) ,float(NO2_sum)],
     [1,1,1,1,1]]
    # 构造dataframe并写入excel文件
    # df1 = pd.DataFrame(a, columns=['SO2', 'NO2', 'CO', 'PM2.5', 'PM10'],index=['均值','标偏','上标','下标','特征值','标准值'])
    df1 = pd.DataFrame(a, columns=['SO2', 'PM10', 'PM2.5', 'CO', 'NO2'],index=['上标','下标','特征值','标准值'])
    df1.to_excel(newfile_dir)
    if((float(SO2_sum)<so2_mean_up) and (float(PM10_sum)<pm10_mean_up) and (float(PM25_sum)<pm25_mean_up) and (float(CO_sum)<co_mean_up) and (float(NO2_sum)<no2_mean_up)):
        name = '偏标准型'
        color = '#00E400'
    elif(float(PM25_sum)>pm25_mean_up):
        name = '偏二次型'
        color = '#FFFF00'
    elif (float(SO2_sum)>so2_mean_up):
        name = '偏燃煤型'
        color = '#FF7E00'
    elif (float(PM10_sum)>pm10_mean_up):
        name = '偏粗颗粒型'
        color = '#FF0000'
    elif ((float(SO2_sum)>so2_mean_up)  and (float(PM25_sum)>pm25_mean_up)):
        name = '偏烟花型'
        color = '#99004C'
    elif ((float(SO2_sum)>so2_mean_up)  and (float(CO_sum)>co_mean_up) and (float(NO2_sum)>no2_mean_up)):
        name = '偏钢铁型'
        color = '#7E0023'
    elif ((float(PM25_sum)>pm25_mean_up)  and (float(CO_sum)>co_mean_up) and (float(NO2_sum)>no2_mean_up)):
        name = '偏机动车型'
        color = '#7E2223'
    else:
        name = '偏其它型'
        color = '#772223'
    return name,color




