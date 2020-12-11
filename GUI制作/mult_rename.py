import data_visual
import data_opt
import spider_data
import pic_bar
from datetime import datetime
import datetime as datatime
import pandas as pd


def time_roll_data(start_time):
    # start_time = '12/10/2020'
    my_datatime = pd.date_range(start_time, '12/31/2020')
    result = my_datatime.strftime('%Y-%m-%d')
    print(result[0])
    yestoday = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
    print(yestoday)
    file_dir = 'excelfile/淮阳县整年数据.xls'
    file_cen_dir = 'excelfile/淮阳县整年数据中间.xls'
    newfile_dir = 'excelfile/淮阳县整年数据.xlsx'
    df = pd.read_excel(file_dir)
    df.index = df['时间']
    df = df[yestoday:result[0]]
    df.to_excel(file_cen_dir,index=False)
    name = data_opt.tezheng(file_cen_dir,newfile_dir,result[0])
    data_visual.plot_radar_time(newfile_dir,result[0],name[0])