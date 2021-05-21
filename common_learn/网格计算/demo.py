import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd
import os
from pandas import DataFrame as df
import numpy as np

file_path = '~/nc/'
# nc文件输出位置


# 下面进入批量处理
for file_name in filenames:
    nc_pro = Dataset(file_path + file_nc + '.nc', 'w', format='NETCDF4')
    # 使用Dataset创建nc文件

    nc_pro.createDimension('al', None)
    nc_pro.createDimension('temp', None)
    nc_pro.createDimension('RH', None)
    nc_pro.createDimension('pha', None)
    # 命名nc文件变量，None，为自由维度


    al = nc_pro.createVariable('al', np.float64, ('al'))
    temp = nc_pro.createVariable('temp', np.float64, ('temp'))
    rh = nc_pro.createVariable('RH', np.float64, ('RH'))
    pha = nc_pro.createVariable('pha', np.float64, ('pha'))
    # 设置nc文件中变量类型，这里使用的是float64

    al.units = 'm'
    rh.units = '%'
    temp.units = 'K'
    pha.units = 'pha'
    # 定义变量单位


    data = pd.read_csv(filepath + file_name)
    # 使用panda中的read_csv读取txt文件
    data_df = data['height\tPha\ttemp\tRH'].str.split('\t', expand=True)
    # 由于我读取的txt文件只输入到了一个columns，所以我使用这个语句进
    # 行了分列
    nc_df = df(data_df.values, columns=['al', 'pha', 'temp', 'RH'])
    # 将分列后的dataframe文件columns重新命名
    nc_pro['al'][:] = nc_df['al'].values
    nc_pro['RH'][:] = nc_df['RH'].values
    nc_pro['pha'][:] = nc_df['pha'].values
    nc_pro['temp'][:] = nc_df['temp'].values
    # 将数值输入到nc文件中
    nc_pro.close()
    # 为避免内存的占用，写完一个关闭一个
