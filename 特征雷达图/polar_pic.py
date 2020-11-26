import data_visual
import data_opt
import spider_data
import pic_bar
from datetime import datetime
import datetime as datatime
import pandas as pd



# 区域特征雷达图
def area_data():
    yestoday = (datetime.now() + datatime.timedelta(days=0)).strftime("%Y-%m-%d %H")
    file_dir = 'excelfile/' + yestoday + '.xls'
    newfile_dir = 'excelfile/' + yestoday + '.xlsx'
    # 获取数据
    spider_data.save_excel(file_dir)
    df = pd.read_excel(file_dir)
    for now_time in df['时间']:
        name = data_opt.tezheng(file_dir,newfile_dir,now_time)
        data_visual.plot_radar(newfile_dir,now_time,name[0])


# 整体考虑一段时间的特征雷达图
def time_data():
    # yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d %H")
    file_dir = 'excelfile/太康县.xls'
    newfile_dir = 'excelfile/太康县.xlsx'
    color = []
    # 获取数据
    # spider_data.save_excel(file_dir)
    my_datatime = pd.date_range('11/01/2020', '11/24/2020')
    result = my_datatime.strftime('%Y-%m-%d')
    for now_time in result:
        name = data_opt.tezheng(file_dir,newfile_dir,now_time)
        data_visual.plot_radar_time(newfile_dir,now_time,name[0])
        if name in color:
            color.append(('',name[1]))
        else:
            color.append(name)
    print(color)
    pic_bar.line_pic(file_dir,"image_file",color)


# 滚动计算每一天的特征雷达图
def time_roll_data():
    start_time = '11/09/2020'
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


# 滚动计算每一天的区域特征雷达图
def area_roll_data():
    start_time = '11/01/2020'
    area_name = '淮阳县'
    my_datatime = pd.date_range(start_time, '12/31/2020')
    result = my_datatime.strftime('%Y-%m-%d')
    print(result[0])
    yestoday = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
    print(yestoday)
    file_dir = 'excelfile/周口市区县全年日数据.xls'
    file_cen_dir = 'excelfile/周口市区县全年日数据中间.xls'
    newfile_dir = 'excelfile/周口市区县全年日数据.xlsx'
    df = pd.read_excel(file_dir)
    df.index = df['时间']
    df = df[yestoday:result[0]]
    df.to_excel(file_cen_dir)
    name = data_opt.tezheng_area(file_cen_dir,newfile_dir,result[0],area_name)
    data_visual.plot_radar_time(newfile_dir,result[0],name[0])


# 滚动计算每一天的时间累计特征雷达图
def time_acc_data():
    color = []
    file_dir = 'excelfile/淮阳县整年数据.xls'
    file_cen_dir = 'excelfile/淮阳县整年数据中间.xls'
    newfile_dir = 'excelfile/淮阳县整年数据.xlsx'
    newfile_acc_dir = 'excelfile/淮阳县整年截取数据.xlsx'
    my_datatime = pd.date_range('10/22/2020', '11/22/2020')
    start_time = my_datatime[0].strftime('%Y-%m-%d')
    stop_time = my_datatime[-1].strftime('%Y-%m-%d')
    df = pd.read_excel(file_dir)
    df.index = df['时间']
    df = df[start_time:stop_time]
    df.to_excel(newfile_acc_dir, index=False)
    for start_time in my_datatime:
        my_datatime = pd.date_range(start_time, '12/31/2020')
        result = my_datatime.strftime('%Y-%m-%d')
        print(result[0])
        yestoday = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        print(yestoday)
        df = pd.read_excel(file_dir)
        df.index = df['时间']
        df = df[yestoday:result[0]]
        df.to_excel(file_cen_dir, index=False)
        name = data_opt.tezheng(file_cen_dir, newfile_dir, result[0])
        data_visual.plot_radar_time(newfile_dir, result[0], name[0])
        if name in color:
            color.append(('', name[1]))
        else:
            color.append(name)
    print(color)
    pic_bar.line_pic(newfile_acc_dir, "image_file", color)




# time_acc_data()
# area_roll_data()
# area_data()
# time_data()
# time_roll_data()
