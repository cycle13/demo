import pandas as pd
import line_bar
import make_excel
import send_text_image
import windows_opr
import time
import yingze_spider


def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excelhour_pic(name, excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir, rank_name)
    make_excel.excel_c(excel_filenew_dir, name_c, excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir, name_table, excel_rank_insert)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def hoursend():
    sl = yingze_spider.zonghe()
    # 发送文本
    name = '王彦军'
    l = "【实时空气质量报告】{} {}，我区综" \
        "合指数为{}，六城区中排名{}；AQI为{}，{}，首要污" \
        "染物：{}。PM2.5实时浓度为{}μg/m³，六城区排名{}；PM10实时" \
        "浓度为{}μg/m³，六城区排名{}；当前气象条件：{}，相对湿度{}%，预计未" \
        "来几个小时我区空气质量以{}。".format('2020年11月4日','12时','6.55','第一','90','二级良','PM10',
                                   '50','第二','130','第一','南风二级','38','二级为主')
    send_text(name, l)

    # 发送excel表格
    excel_file_dir = r'excelfiles\迎泽小时推送数据.xls'
    excel_filenew_dir = r'excelfiles\迎泽小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\迎泽小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\迎泽区\excelfiles\迎泽小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '迎泽区'
    name_table = '{}区域空气质量排名'.format(sl)
    send_excelhour_pic(name, excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert)


def send_excelhourjc_pic(name, excel_file_dir, excel_filenew_dir,rank_name,excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir, rank_name)
    make_excel.table_fontjc(excel_filenew_dir,excel_rank_insert)
    send_text_image.excel_catch_screenjc(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def hourjc():
    # 发送文本
    name = '王彦军'
    l = "【{}迎泽空气质量报告】\n今日{}时老军营点" \
        "位累计综合指数为{}，在全市11个标准站中排名{}，累计AQI为{}，{}，首要" \
        "污染物：{}。\nPM2.5累计浓度为{}μg/m³，在全市11个" \
        "标准站中排名{}。\nPM10累计浓度为{}μg/m³，在全市11个标准" \
        "站中排名{}。\n老军营与桃园国控点、全市平均水平的对比情况如下表：".format('2020年11月4日1-12时','1-12','5.02','第三',
                                                    '78','二级良','NO2,PM10','40','第二','106','第四')
    send_text(name, l)

    # 发送excel表格
    excel_file_dir = r'excelfiles\迎泽降尘小时推送数据.xlsx'
    excel_filenew_dir = r'excelfiles\迎泽降尘小时推送数据排名.xlsx'
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\迎泽区\excelfiles\迎泽降尘小时推送数据排名插入.xlsx'
    rank_name = '累计AQI'
    send_excelhourjc_pic(name, excel_file_dir, excel_filenew_dir,rank_name,excel_rank_insert)


hoursend()