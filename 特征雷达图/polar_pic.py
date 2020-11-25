import data_visual
import data_opt
import spider_data
import pic_bar
from datetime import datetime
import datetime as datatime
import pandas as pd



def area_data():
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d %H")
    file_dir = 'excelfile/' + yestoday + '.xls'
    newfile_dir = 'excelfile/' + yestoday + '.xlsx'
    # 获取数据
    spider_data.save_excel(file_dir)
    for now_time in ["商水县","太康县","扶沟县",'沈丘县','淮阳县','西华县','郸城县','项城市','鹿邑县']:
        name = data_opt.tezheng(file_dir,newfile_dir,now_time)
        data_visual.plot_radar(newfile_dir,now_time,name[0])


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


area_data()
# time_data()