import pandas as pd
import line_bar
import make_excel
import send_text_image
import windows_opr
import time


def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excelhour_pic(name, excel_file_dir, excel_filerank_dir,name_table, excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_c(excel_file_dir, excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir, name_table, excel_rank_insert)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_line_pic(name,excel_file_dir,image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(excel_file_dir)
    line_bar.line_bar(df['时间'],df['瑞山西路'], df['书院路'], df['限值'],'考核点PM2.5浓度折线图', '时间', '浓度 μg/m3',image_file,"PM25")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)


def hoursend():
    # 发送文本
    name = '王彦军'
    l = "【实时空气质量播报】\n{}截止{}\n合川区" \
        "累计AQI为{}，{}。\n书院路站点PM2.5累计" \
        "浓度为{}µg/m³，累计AQI为{}，{}。\n瑞山西" \
        "路站点PM2.5累计浓度为{}µg/m³，累" \
        "计AQI为{}，{}。\n具体各污染物浓度见下表：".format('2020年10月26日','23时','114','三级轻度污染','84','112',
                                                '三级轻度污染','89','118','三级轻度污染')
    send_text(name, l)


    # 发送excel表格1
    excel_file_dir = r'excelfiles\合川区推送数据.xlsx'
    excel_filerank_dir = r'excelfiles\合川区推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\合川\excelfiles\合川区推送数据排名充填插入.xlsx'
    name_table = '2020年10月26日截止23时空气质量累计情况'
    send_excelhour_pic(name, excel_file_dir, excel_filerank_dir,name_table, excel_rank_insert)

    # 发送折线图
    excel_file_dir = r'excelfiles\合川折线图详细数据.xlsx'
    image_file = r'image_file'
    send_line_pic(name, excel_file_dir, image_file)

hoursend()

