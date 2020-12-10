import pandas as pd
import line_bar
import make_excel
import send_text_image
import windows_opr
import pre_air
from datetime import datetime
import datetime as datatime
import huaiyang_spider
import json
import time
import demo



def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)



def make_excelhour(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2,rank_name1,rank_name2,add_name1 ,add_name2,name_c, excel_filerank_dir,name_table, excel_rank_insert):
    huaiyang_spider.save_excel(excel_file_dir)
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2, rank_name1,rank_name2,add_name1,add_name2)
    l = make_excel.excel_c(excel_filenew_dir1, name_c, excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir, name_table.format(l[0][0:2]), excel_rank_insert)
    return l

def make_excelhourleiji(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2,rank_name1,rank_name2,add_name1 ,add_name2,name_c, excel_filerank_dir,name_table, excel_rank_insert):
    huaiyang_spider.saveleiji_excel(excel_file_dir)
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2, rank_name1,rank_name2,add_name1,add_name2)
    l = make_excel.excel_cleiji(excel_filenew_dir1, name_c, excel_filerank_dir)
    make_excel.table_fontleiji(excel_filerank_dir, name_table.format(l[0][0:2]), excel_rank_insert)
    return l



def send_excel(name,excel_rank_insert):
    windows_opr.FindWindow(name)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excelleiji(name,excel_rank_insert):
    windows_opr.FindWindow(name)
    send_text_image.excel_catch_screenleiji(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)



def send_pic(name, excel_filenew_dir1,excel_filenew_dir2,pm10,pm25,image_file):
    windows_opr.FindWindow(name)
    line_bar.line_pic(excel_filenew_dir1,pm25,image_file)
    line_bar.line_picpm10(excel_filenew_dir2,pm10,image_file)
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.ctrlV()
        windows_opr.altS()
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)
    send_text_image.del_files('excelfiles')


def send_picline(name,line_excel,image_title,image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(line_excel)
    line_bar.line_bar(df['时间'], df['PM2.5'], df['PM10'], image_title, '时间', '浓度 μg/m3',image_file, "PM25")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)

def send_pic_line(name, line_excel, line_excel2,image_title_PM25,image_title_PM10, image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(line_excel)
    df2 = pd.read_excel(line_excel2)
    line_bar.line_bar_double(df['时间'], df['PM2.5'], df2['PM2.5'], image_title_PM25, '时间', '浓度 μg/m3',image_file, "PM25")
    line_bar.line_bar_double(df['时间'], df['PM10'], df2['PM10'], image_title_PM10, '时间', '浓度 μg/m3', image_file, "PM10")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)


def hoursend(name):
    try:
        # 发送文本
        # 发送excel表格1
        excel_file_dir = r'excelfiles\周口市区县数据.xls'
        excel_filenew_dir1 = r'excelfiles\周口市区县数据排名.xlsx'
        excel_filenew_dir2 = r'excelfiles\周口市区县数据排名PM10.xlsx'
        excel_filerank_dir = r'excelfiles\淮阳小时推送数据排名充填.xlsx'
        image_file = 'image_file'
        # 必须要绝对路径
        excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\淮阳\excelfiles\淮阳小时推送数据排名充填插入.xlsx'
        rank_name1 = 'PM2.5'
        rank_name2 = 'PM10'
        add_name1 = 'PM2.5排名'
        add_name2 = 'PM10排名'
        name_c = '淮阳县'
        name_table = '周口市九区县{}时PM2.5和PM10排名及各污染物详情表'
        my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
        line_date = 'excellinefiles/' + my_datatime
        l = make_excelhour(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2,rank_name1,rank_name2,add_name1 ,add_name2,name_c, excel_filerank_dir,name_table, excel_rank_insert)
        print('已对数据排名、充填和插入表标题')
        datatime_n = (datetime.now() + datatime.timedelta(hours =-1)).strftime("%Y%m%d/%H")
        # datatime_n = datetime.strftime(datetime.now(), '%Y%m%d/%H')
        m = huaiyang_spider.qi("101181404", datatime_n)
        print('已获取气象数据')
        data = json.loads(m)
        pm10 = "周口市九区县{}时PM10浓度柱状图".format(l[0][0:2])
        pm25 = "周口市九区县{}时PM2.5浓度柱状图".format(l[0][0:2])
        image_title = '淮阳区颗粒物00时至{}时浓度折线图'.format(l[0][0:2])
        try:
            if l[0][0:2] != "无":
                print('空气质量数据获取成功')
                if data['rcode'] == 200:
                    k = "【实时播报】：\n淮阳区{}时: \n      淮阳区PM2.5浓度为{}μg/m3，在全市9个区县中排名第{}；PM10浓度为{}μg/m3，在全市9个区县中排名第{}。其中：\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。\n      气象条件：当前湿度{}%，温度为{}℃，风力为{}，风向为{}。".format(l[0][0:2],l[1], l[2], l[3], l[4],l[5], l[6],l[7],l[8], l[9],l[10],l[11], l[12],l[13], data['humidity'], data['temperature'], data['windpower'],data['winddirect'])
                    print('气象数据获取成功')
                    send_text(name, k)
                    time.sleep(4)
                    send_excel(name, excel_rank_insert)
                else:
                    k = "【实时播报】：\n淮阳区{}时: \n      淮阳区PM2.5浓度为{}μg/m3，在全市9个区县中排名第{}；PM10浓度为{}μg/m3，在全市9个区县中排名第{}。其中：\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。\n      {}PM2.5浓度为{}µg/m³，PM10浓度为{}µg/m³。气象数" \
                        "据缺失！".format(l[0][0:2],l[1], l[2], l[3], l[4],l[5], l[6],l[7],l[8], l[9],l[10],l[11], l[12],l[13])
                    print('气象数据缺失')
                    send_text(name, k)
                    time.sleep(4)
                    send_excel(name, excel_rank_insert)
                time.sleep(1)
                send_pic(name, excel_filenew_dir1,excel_filenew_dir2,pm10,pm25,image_file)

                # 做折线图
                huaiyang_spider.save_date(line_date)
                line_excel = line_date+'/'+'淮阳县' + my_datatime+".xls"
                send_picline(name,line_excel,image_title,image_file)

                # 做折线图对比图
                image_title_PM25 = '淮阳区与太康县00时至{}时PM2.5浓度折线图'.format(l[0][0:2])
                image_title_PM10 = '淮阳区与太康县00时至{}时PM10浓度折线图'.format(l[0][0:2])
                line_excel = line_date + '/' + '淮阳县' + my_datatime + ".xls"
                line_excel2 = line_date + '/' + '太康县' + my_datatime + ".xls"
                send_pic_line(name, line_excel, line_excel2,image_title_PM25,image_title_PM10, image_file)

            else:
                print('空气质量数据异常')
                raise
        except:
            windows_opr.FindWindow(name)
            send_text_image.setText("数据异常！")
            windows_opr.ctrlV()
            windows_opr.altS()
            time.sleep(1)
            windows_opr.CloseWindow(name)
    except:
        time.sleep(60)
        hoursend(name)


def hourleijisend(name):
    try:
        # 发送文本
        # 发送excel表格1
        excel_file_dir = r'excelfiles\周口市区县数据.xls'
        excel_filenew_dir1 = r'excelfiles\周口市区县数据排名.xlsx'
        excel_filenew_dir2 = r'excelfiles\周口市区县数据排名PM10.xlsx'
        excel_filerank_dir = r'excelfiles\淮阳小时推送数据排名充填.xlsx'
        image_file = 'image_file'
        # 必须要绝对路径
        excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\淮阳\excelfiles\淮阳小时推送数据排名充填插入.xlsx'
        rank_name1 = 'PM2.5'
        rank_name2 = 'PM10'
        add_name1 = 'PM2.5排名'
        add_name2 = 'PM10排名'
        name_c = '淮阳县'
        name_table = "周口市九区县截止{}时PM2.5和PM10累计浓度排名及各污染物详情表"
        l = make_excelhourleiji(excel_file_dir, excel_filenew_dir1,excel_filenew_dir2,rank_name1,rank_name2,add_name1 ,add_name2,name_c, excel_filerank_dir,name_table, excel_rank_insert)
        print('已对数据排名、充填和插入表标题')
        pm10 = "周口市九区县截止今日{}时PM10累积浓度柱状图".format(l[0][0:2])
        pm25 = "周口市九区县截止今日{}时PM2.5累积浓度柱状图".format(l[0][0:2])
        try:
            if l[0][0:2] != "无":
                print('空气质量数据获取成功')
                k = "【今日累计播报】：\n淮阳区截止{}时，PM2.5累计浓度为{}μg/m3，在全市9个区县中排名第{}；PM10累计浓度为{}μg/m3，在全市9个区县中排名第{}。".format(l[0][0:2],l[1],l[2],l[3],l[4])
                send_text(name, k)
                time.sleep(4)
                send_excelleiji(name, excel_rank_insert)
                time.sleep(1)
                send_pic(name, excel_filenew_dir1,excel_filenew_dir2,pm10,pm25,image_file)
            else:
                raise
        except:
            windows_opr.FindWindow(name)
            send_text_image.setText("数据异常！")
            windows_opr.ctrlV()
            windows_opr.altS()
            time.sleep(1)
            windows_opr.CloseWindow(name)
    except:
        time.sleep(60)
        hourleijisend(name)


def yearleijisend(name):
    windows_opr.FindWindow(name)
    excel_file_dir = r'D:\Program Files\pycharm\微信自动发送数据\淮阳\excelfiles\周口市区县年累计数据.xls'
    excel_file_dir1 = r'D:\Program Files\pycharm\微信自动发送数据\淮阳\excelfiles\周口市区县年累计数据.xlsx'
    line_date = r"excelimage"
    huaiyang_spider.yearleiji(excel_file_dir)
    make_excel.excel_yearrank(excel_file_dir,excel_file_dir1)
    make_excel.excel_yearc(excel_file_dir1)
    send_text_image.excel_catch_screenyearleiji(excel_file_dir1)
    windows_opr.ctrlV()
    windows_opr.altS()
    demo.year_leiji()
    for i in send_text_image.get_file(line_date):
        send_text_image.paste_img(line_date + "\\" + i)
        windows_opr.ctrlV()
        windows_opr.altS()
    time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(line_date)


def save_data():
    my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
    line_date = 'hnalldata/' + my_datatime
    huaiyang_spider.save_hn_date(line_date)



def pre_hn_air(name):
    data = pre_air.pre_air()
    my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
    if my_datatime == data[0]:
        # l = '河南省区域环境空气质量预报\n    污染提示：{}\n一、未来7天' \
        #     '预报\n    {}\n    {}\n    {}\n    {}' \
        #     '\n    {}\n    {}\n    {}\n    {}\n 二、建议\n    {}'.format(data[1],data[2][0],data[2][1],data[2][2],data[2][3],data[2][4],data[2][5],data[2][6],data[2][7],data[3])

        for i in data[2]:
            if i == data[2][0]:
                m = '       ' + i + '\n'
            else:
                m = m+'       '+i+'\n'
        l = '河南省区域环境空气质量预报\n       污染提示：{}\n一、未来7天' \
            '预报\n{} 二、建议\n       {}'.format(data[1],m,data[3])
        send_text(name,l)
        windows_opr.FindWindow(name)
        for i in send_text_image.get_file("image_pic"):
            send_text_image.paste_img("image_pic" + "\\" + i)
            windows_opr.send()
            time.sleep(1)
        windows_opr.CloseWindow(name)
        send_text_image.del_files("image_pic")


# pre_hn_air('王彦军')
# yearleijisend('王彦军')
# hoursend('王彦军')
# save_data()
# image_file = 'image_file'
# image_title = '淮阳区颗粒物0时至{}时折线图--测试'.format("l[0][0:2]")
# my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
# line_date = 'excellinefiles/' + my_datatime
# line_excel = line_date+'/'+'淮阳县' + my_datatime+".xls"
# send_picline(name,line_excel,image_title,image_file)

# image_file = 'image_file'
# my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
# line_date = 'excellinefiles/' + my_datatime
# image_title_PM25 = '淮阳区与太康县00时至{}时PM2.5浓度折线图'.format("l[0][0:2]")
# image_title_PM10 = '淮阳区与太康县00时至{}时PM10浓度折线图'.format("l[0][0:2]")
# line_excel = line_date + '/' + '淮阳县' + my_datatime + ".xls"
# line_excel2 = line_date + '/' + '太康县' + my_datatime + ".xls"
# send_pic_line('王彦军', line_excel, line_excel2,image_title_PM25,image_title_PM10, image_file)