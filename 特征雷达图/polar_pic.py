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
    start_time = '12/10/2020'
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
    start_time = '01/11/2021'
    area_name = '淮阳县'
    my_datatime = pd.date_range(start_time, '12/31/2021')
    result = my_datatime.strftime('%Y-%m-%d')
    print(result[0])
    yestoday = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
    print(yestoday)
    file_dir = 'excelfile/周口市2020年区县全年日数据 .xls'
    file_cen_dir = 'excelfile/周口市2020年区县全年日数据中间.xls'
    newfile_dir = 'excelfile/周口市2020年区县全年日数据.xlsx'
    df = pd.read_excel(file_dir)
    df.index = df['时间']
    df = df[yestoday:result[0]]
    df.to_excel(file_cen_dir)
    name = data_opt.tezheng_area(file_cen_dir,newfile_dir,result[0],area_name)
    data_visual.plot_radar_time(newfile_dir,result[0],name[0])


# 滚动计算每一天的时间累计特征雷达图
def time_acc_data():
    color = []
    file_dir = 'excelfile/合川区数据.xlsx'
    file_cen_dir = 'excelfile/合川区数据中间.xls'
    newfile_dir = 'excelfile/合川区数据数据.xlsx'
    newfile_acc_dir = 'excelfile/合川区数据截取数据.xlsx'
    my_datatime = pd.date_range('01/01/2020', '12/31/2020')
    start_time = my_datatime[0].strftime('%Y-%m-%d')
    stop_time = my_datatime[-1].strftime('%Y-%m-%d')
    df = pd.read_excel(file_dir)
    df.index = df['时间']
    df = df[start_time:stop_time]
    df.to_excel(newfile_acc_dir, index=False)
    for start_time in my_datatime:
        my_datatime = pd.date_range(start_time, '12/31/2021')
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
    pic_bar.line_pic10(newfile_acc_dir, "image_file", color)
    pic_bar.line_picco(newfile_acc_dir, "image_file", color)
    pic_bar.line_picso2(newfile_acc_dir, "image_file", color)
    pic_bar.line_picno2(newfile_acc_dir, "image_file", color)
    pic_bar.line_pico3(newfile_acc_dir, "image_file", color)


# 滚动计算每一小时的时间累计特征雷达图
def time_hour_acc_data():
    color = []
    end_date_time = '02/12/2021'
    start_time = '00:00:00'
    end_time = '12:00:00'
    my_datatime = pd.date_range(end_date_time, '12/31/2021')
    result = my_datatime[0].strftime('%Y-%m-%d')
    start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
    end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    file_dir = 'excelfile/合川区.xls'
    file_cen_dir = 'excelfile/合川区中间.xls'
    newfile_dir = 'excelfile/合川区.xlsx'
    newfile_acc_dir = 'excelfile/合川区截取.xlsx'

    print(start_date,end_date,result,start_time,end_time)
    df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
    df1.index = df1['时间']
    df1 = df1[start_date:end_date]
    my_datatime = pd.date_range(end_date_time+' '+start_time, end_date_time+' '+end_time, freq='h')
    df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
    df2.index = df2['时间']
    df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
    df4.to_excel(newfile_acc_dir)
    for i in my_datatime:
        j = i.strftime('%Y-%m-%d %H:%M:%S')
        k = i.strftime('%Y-%m-%d %H%M%S')
        df3 = df2[j:j]
        df = df1.append(df3)
        print(j)
        df.to_excel(file_cen_dir, index=False)
        name = data_opt.tezheng_hour(file_cen_dir, newfile_dir, i)
        data_visual.plot_radar_time_hour(newfile_dir, k, name[0])
        if name in color:
            color.append(('', name[1]))
        else:
            color.append(name)
    print(color)
    pic_bar.line_pic_hour(newfile_acc_dir, "image_file", color)
    # pic_bar.line_pic10(newfile_acc_dir, "image_file", color)
    # pic_bar.line_picco(newfile_acc_dir, "image_file", color)
    # pic_bar.line_picso2(newfile_acc_dir, "image_file", color)
    # pic_bar.line_picno2(newfile_acc_dir, "image_file", color)
    # pic_bar.line_pico3(newfile_acc_dir, "image_file", color)


# 滚动计算每一小时的区域特征雷达图
def area_hour_acc_data():
    area_name = '淮阳县'
    end_date_time = '01/01/2021'
    start_time = '00:00:00'
    end_time = '02:00:00'
    my_datatime = pd.date_range(end_date_time, '12/31/2021')
    result = my_datatime[0].strftime('%Y-%m-%d')
    start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
    end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    file_dir = 'excelfile/周口数据.xls'
    file_cen_dir = 'excelfile/周口数据中间.xls'
    newfile_dir = 'excelfile/周口数据.xlsx'
    newfile_acc_dir = 'excelfile/周口截取数据.xlsx'

    print(start_date,end_date,result,start_time,end_time)
    df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
    df1.index = df1['时间']
    df1 = df1[start_date:end_date]
    my_datatime = pd.date_range(end_date_time+' '+start_time, end_date_time+' '+end_time, freq='h')
    df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
    df2.index = df2['时间']
    df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
    df4.to_excel(newfile_acc_dir)
    for i in my_datatime:
        j = i.strftime('%Y-%m-%d %H:%M:%S')
        k = i.strftime('%Y-%m-%d %H%M%S')
        df3 = df2[j:j]
        df = df1.append(df3)
        print(j)
        df.to_excel(file_cen_dir, index=False)
        name = data_opt.tezheng_area(file_cen_dir, newfile_dir, i,area_name)
        data_visual.plot_radar_time(newfile_dir, k, name[0])


def area_hour_acc_data1():
    area_name = '淮阳县'
    start_date_time = '2021-01-01 02:00:00'
    end_date_time = '2021-01-02 04:00:00'
    start_date_time1 = datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    end_date_time1 = datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    date_times = pd.date_range(start_date_time, end_date_time,freq='D')
    for date_time in date_times:
        date_time = datetime.strptime(date_time.strftime("%Y-%m-%d"),"%Y-%m-%d")
        my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d'), '2050-01-01')
        result = my_datatime[0].strftime('%Y-%m-%d')
        start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
        file_dir = 'excelfile/周口数据.xls'
        file_cen_dir = 'excelfile/周口数据中间.xls'
        newfile_dir = 'excelfile/周口数据.xlsx'
        newfile_acc_dir = 'excelfile/周口截取数据.xlsx'
        df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
        df1.index = df1['时间']
        df1 = df1[start_date:end_date]
        if datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                date_time.strftime('%Y-%m-%d') + ' 23:00:00', '%Y-%m-%d %H:%M:%S'):
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'),
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
        else:
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            end_date_time, freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'), end_date_time, freq='h')
        df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
        df2.index = df2['时间']
        df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
        df4.to_excel(newfile_acc_dir)
        for i in my_datatime:
            j = i.strftime('%Y-%m-%d %H:%M:%S')
            k = i.strftime('%Y-%m-%d %H%M%S')
            df3 = df2[j:j]
            df = df1.append(df3)
            print(j)
            df.to_excel(file_cen_dir, index=False)
            name = data_opt.tezheng_area(file_cen_dir, newfile_dir, i,area_name)
            data_visual.plot_radar_time(newfile_dir, k, name[0])


# 滚动计算每一小时的时间累计特征雷达图
def time_hour_acc_data1():
    start_date_time = '2021-02-10 13:00:00'
    end_date_time = '2021-02-13 04:00:00'
    start_date_time1 = datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    end_date_time1 = datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    date_times = pd.date_range(start_date_time1, end_date_time1, freq='D')
    print(date_times)
    for date_time in date_times:
        date_time = datetime.strptime(date_time.strftime("%Y-%m-%d"), "%Y-%m-%d")
        my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d'), '2050-01-01')
        result = my_datatime[0].strftime('%Y-%m-%d')
        start_date = (my_datatime[0] + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        end_date = (my_datatime[0] + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
        file_dir = 'excelfile/合川区.xls'
        file_cen_dir = 'excelfile/合川区中间.xls'
        newfile_dir = 'excelfile/合川区.xlsx'
        newfile_acc_dir = 'excelfile/合川区截取.xlsx'
        df1 = pd.read_excel(file_dir,sheet_name='Sheet1')
        df1.index = df1['时间']
        df1 = pd.read_excel(file_dir, sheet_name='Sheet1')
        df1.index = df1['时间']
        df1 = df1[start_date:end_date]
        if datetime.strptime(end_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                date_time.strftime('%Y-%m-%d') + ' 23:00:00', '%Y-%m-%d %H:%M:%S'):
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'),
                                            date_time.strftime('%Y-%m-%d') + ' 23:00:00', freq='h')
        else:
            if datetime.strptime(start_date_time, '%Y-%m-%d %H:%M:%S') >= datetime.strptime(
                    date_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'):
                my_datatime = pd.date_range(start_date_time,
                                            end_date_time, freq='h')
            else:
                my_datatime = pd.date_range(date_time.strftime('%Y-%m-%d %H:%M:%S'), end_date_time, freq='h')

        df2 = pd.read_excel(file_dir, sheet_name='Sheet2')
        df2.index = df2['时间']
        df4 = df2[my_datatime[0].strftime('%Y-%m-%d %H:%M:%S'):my_datatime[-1].strftime('%Y-%m-%d %H:%M:%S')]
        df4.to_excel(newfile_acc_dir)
        for i in my_datatime:
            j = i.strftime('%Y-%m-%d %H:%M:%S')
            k = i.strftime('%Y-%m-%d %H%M%S')
            df3 = df2[j:j]
            df = df1.append(df3)
            print(j)
            df.to_excel(file_cen_dir, index=False)
            name = data_opt.tezheng_hour(file_cen_dir, newfile_dir, i)
            data_visual.plot_radar_time_hour(newfile_dir, k, name[0])


# 滚动计算每一天的特征雷达图
def time_roll_data1():
    start_time = '2020-12-10'
    stop_time = '2020-12-31'
    my_datatime = pd.date_range(start_time, stop_time)
    result = my_datatime.strftime('%Y-%m-%d')
    for result in my_datatime:
        print(result.strftime('%Y-%m-%d'))
        yestoday = (result + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        print(yestoday)
        file_dir = 'excelfile/淮阳县整年数据.xls'
        file_cen_dir = 'excelfile/淮阳县整年数据中间.xls'
        newfile_dir = 'excelfile/淮阳县整年数据.xlsx'
        df = pd.read_excel(file_dir)
        df.index = df['时间']
        df = df[yestoday:result.strftime('%Y-%m-%d')]
        df.to_excel(file_cen_dir,index=False)
        name = data_opt.tezheng(file_cen_dir,newfile_dir,result.strftime('%Y-%m-%d'))
        data_visual.plot_radar_time(newfile_dir,result.strftime('%Y-%m-%d'),name[0])



# 滚动计算每一天的区域特征雷达图
def area_roll_data1():
    start_time = '2020-01-11'
    stop_time = '2020-12-31'
    area_name = '淮阳县'
    my_datatime = pd.date_range(start_time, stop_time)
    result = my_datatime.strftime('%Y-%m-%d')
    for result in my_datatime:
        print(result.strftime('%Y-%m-%d'))
        yestoday = (result + datatime.timedelta(days=-31)).strftime("%Y-%m-%d")
        print(yestoday)
        file_dir = 'excelfile/周口市2020年区县全年日数据 .xls'
        file_cen_dir = 'excelfile/周口市2020年区县全年日数据中间.xls'
        newfile_dir = 'excelfile/周口市2020年区县全年日数据.xlsx'
        df = pd.read_excel(file_dir)
        df.index = df['时间']
        df = df[yestoday:result.strftime('%Y-%m-%d')]
        df.to_excel(file_cen_dir)
        name = data_opt.tezheng_area(file_cen_dir,newfile_dir,result.strftime('%Y-%m-%d'),area_name)
        data_visual.plot_radar_time(newfile_dir,result.strftime('%Y-%m-%d'),name[0])


# time_acc_data()
# area_roll_data()
# area_data()
# time_data()
# time_roll_data()
# time_hour_acc_data()
# time_roll_data1()
area_roll_data1()
# area_hour_acc_data1()
# time_hour_acc_data1()