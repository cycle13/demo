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


def send_excelhour_pic(name, excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir, rank_name)
    make_excel.excel_c(excel_filenew_dir, name_c, excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir, name_table, excel_rank_insert)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_line_pic(name,excel_file_dir,image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(excel_file_dir)
    line_bar.line_bar(df['时间'], df['二氧化氮浓度'],df['PM2.5质量浓度'], df['PM10质量浓度'],'2020年3月19日01时到08时巨轮 参数对比图', '时间', '浓度 μg/m3',image_file,"PM25")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)


def hoursend():
    # 发送文本
    name = '王彦军'
    l = "【空气质量播报】\n{}巨轮点位综合指数为{}，在太原市八个国控点" \
        "中排名{}，日综合指数与各项污染物排名如下：\n{}巨轮点位累" \
        "计综合指数为{}，在太原市八个国控点中排名{}，管控{}，累计综合指数与各项" \
        "污染物浓度排名及PM2.5、PM10、NO2浓度{}趋势图如下：".format('2020年3月18日','6.12','第八','2020年3月19日1-8时',
                                                    '2.81','第三','良好','1-8时')
    send_text(name, l)

    # 发送excel表格1
    excel_file_dir = r'excelfiles\杏花岭小时推送数据.xlsx'
    excel_filenew_dir = r'excelfiles\杏花岭小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\杏花岭小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\杏花岭\excelfiles\杏花岭小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '巨轮'
    name_table = '2020年3月18日太原市八个国控点的各项污染物的浓度及排名情况'
    send_excelhour_pic(name, excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert)

    # 发送excel表格2
    excel_file_dir = r'excelfiles\杏花岭今日小时推送数据.xlsx'
    excel_filenew_dir = r'excelfiles\杏花岭今日小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\杏花岭今日小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\杏花岭\excelfiles\杏花岭今日小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '巨轮'
    name_table = '2020年3月19日截止8时太原市八个国控点的各项污染物的浓度及排名情况'
    send_excelhour_pic(name, excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert)


    # 发送折线图
    excel_file_dir = r'excelfiles\杏花岭区折线图详细数据.xlsx'
    image_file = r'image_file'
    send_line_pic(name, excel_file_dir, image_file)


def hourlastsend():
    # 发送文本
    name = '王彦军'
    l = "【空气质量播报】\n{}巨轮点位累计综合" \
        "指数为{}，在太原市八个国控点中排名{}，管控{}，累计综" \
        "合指数与各项污染物浓度排名及PM2.5、PM10、NO2浓度{}趋" \
        "势图如下：".format('2020年3月20日1-12时','6.27','第二','良好','1-12时')
    send_text(name, l)

    # 发送excel表格
    excel_file_dir = r'excelfiles\杏花岭最新小时推送数据.xlsx'
    excel_filenew_dir = r'excelfiles\杏花岭最新小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\杏花岭最新小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\杏花岭\excelfiles\杏花岭最新小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '巨轮'
    name_table = '2020年3月18日太原市八个国控点的各项污染物的浓度及排名情况'
    send_excelhour_pic(name, excel_file_dir, excel_filenew_dir, rank_name, name_c, excel_filerank_dir, name_table,
                       excel_rank_insert)

    # 发送折线图
    excel_file_dir = r'excelfiles\杏花岭区最后折线图详细数据.xlsx'
    image_file = r'image_file'
    send_line_pic(name, excel_file_dir, image_file)




