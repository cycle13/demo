import pandas as pd
import line_bar
import make_excel
import send_text_image
import windows_opr
import time
import xinghualing_spider


def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excelhour_pic(excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert):
    make_excel.excel_rank(excel_file_dir, excel_filenew_dir, rank_name)
    l = make_excel.excel_c(excel_filenew_dir, name_c, excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir, name_table, excel_rank_insert)
    return l


def send_excel(name,excel_rank_insert):
    windows_opr.FindWindow(name)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)



def send_line_pic(name,excel_file_dir,image_title,image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(excel_file_dir)
    line_bar.line_bar(df['时间'], df['NO2'],df['PM2.5'], df['PM10'],image_title, '时间', '浓度μg/m3',image_file,"PM25")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)
    send_text_image.del_files(image_file)


def hoursend(name):
    sl = xinghualing_spider.station()
    sx = xinghualing_spider.station1()
    # 发送文本
    # name = '王彦军'
    # 发送excel表格1
    excel_file_dir = r'excelfiles\杏花岭小时推送数据.xls'
    excel_filenew_dir = r'excelfiles\杏花岭小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\杏花岭小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\杏花岭\excelfiles\杏花岭小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '巨轮'
    name_table = '{}太原市八个国控点的各项污染物的浓度及排名情况'.format(sl)
    l = send_excelhour_pic(excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert1)

    # 发送excel表格2
    excel_file_dir = r'excelfiles\杏花岭今日小时推送数据.xls'
    excel_filenew_dir = r'excelfiles\杏花岭今日小时推送数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\杏花岭今日小时推送数据排名充填.xlsx'
    # 必须要绝对路径
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\杏花岭\excelfiles\杏花岭今日小时推送数据排名充填插入.xlsx'
    rank_name = '综合指数'
    name_c = '巨轮'
    name_table = '{}太原市八个国控点的各项污染物的浓度及排名情况'.format(sx[0]+sx[1])
    m = send_excelhour_pic(excel_file_dir, excel_filenew_dir,rank_name, name_c, excel_filerank_dir,name_table, excel_rank_insert2)
    k = "【空气质量播报】\n{}巨轮点位综合指数为{}，在太原市八个国控点" \
        "中排名{}，日综合指数与各项污染物排名如下：\n{}巨轮点位累" \
        "计综合指数为{}，在太原市八个国控点中排名{}，管控{}，累计综合指数与各项" \
        "污染物浓度排名及PM2.5、PM10、NO2浓度{}趋势图如下：".format(sl, l[0], l[1], sx[0]+sx[1],
                                                  m[0], m[1], '良好', sx[1])
    send_text(name, k)

    send_excel(name, excel_rank_insert1)
    send_excel(name, excel_rank_insert2)

    # 发送折线图
    excel_file_dir = r'excelfiles\杏花岭区折线图详细数据.xls'
    xinghualing_spider.leiji(excel_file_dir)
    image_file = r'image_file'
    send_line_pic(name, excel_file_dir,sx[0]+sx[1], image_file)


def hourlastsend(name):
    # 发送文本
    # name = '王彦军'
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


hoursend('王彦军')

