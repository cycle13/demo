import pandas as pd
import line_bar
import make_excel
import send_text_image
import windows_opr
from datetime import datetime
import huaiyang_spider
import json
import time



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


def hoursend():
    try:
        # 发送文本
        name = "淮阳区环境攻坚群"
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
        datatime_n = datetime.strftime(datetime.now(), '%Y%m%d/%H')
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
                    k = "【实时播报】：\n淮阳区{}时，PM2.5浓度为{}μg/m3，在全市9个区县中排名第{}；PM10浓度为{}μg/m3，在全市9个区县中排名第{}。当前湿度{}%，温度为{}℃，风力为{}，风向为{}。".format(l[0][0:2], l[1], l[2], l[3], l[4], data['humidity'], data['temperature'], data['windpower'],data['winddirect'])
                    print('气象数据获取成功')
                    send_text(name, k)
                    time.sleep(4)
                    send_excel(name, excel_rank_insert)
                else:
                    k = "【实时播报】：\n淮阳区{}时，PM2.5浓度为{}μg/m3，在全市9个区县中排名第{}；PM10浓度为{}μg/m3，在全市9个区县中排名第{}。气象数据缺失！".format(l[0][0:2],l[1],l[2],l[3],l[4])
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
        hoursend()


def hourleijisend():
    try:
        # 发送文本
        name = "淮阳区环境攻坚群"
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
        hourleijisend()



# name = "王彦军"
# image_file = 'image_file'
# image_title = '淮阳区颗粒物0时至{}时折线图--测试'.format("l[0][0:2]")
# my_datatime = datetime.strftime(datetime.now(), '%Y-%m-%d')
# line_date = 'excellinefiles/' + my_datatime
# line_excel = line_date+'/'+'淮阳县' + my_datatime+".xls"
# send_picline(name,line_excel,image_title,image_file)