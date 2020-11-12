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

def send_excelpic(name,excel_file_dir,excel_filenew_dir,excel_add_name,rank_name,name_c,excel_filerank_dir,name_table,excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_rank(excel_file_dir,excel_filenew_dir,excel_add_name,rank_name)
    make_excel.excel_c(excel_filenew_dir,name_c,excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir,name_table,excel_rank_insert)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)

def send_line_pic(name,excel_file_dir,image_file):
    windows_opr.FindWindow(name)
    df = pd.read_excel(excel_file_dir)
    line_bar.line_bar(df['时间'], df['PM2.5'], '西山PM2.5', '时间', '浓度 μg/m3',image_file,"PM25")
    line_bar.line_bar(df['时间'], df['PM10'], '西山PM10', '时间', '浓度 μg/m3', image_file,"PM10")
    line_bar.line_bar(df['时间'], df['NO2'], '西山NO2', '时间', '浓度 μg/m3', image_file,"NO2")
    line_bar.line_bar(df['时间'], df['SO2'], '西山SO2', '时间', '浓度 μg/m3', image_file,"SO2")
    for i in send_text_image.get_file(image_file):
        send_text_image.paste_img(image_file + "\\" + i)
        windows_opr.send()
        time.sleep(1)
    windows_opr.CloseWindow(name)

def wanbaicg():
    # 发送文本
    name = '王彦军'
    l = "【点位空气质量变化情况】\n     {}，西山点位：AQI为{}，{}" \
        "，首要污染物：{}，在全市11个标准站中排名第{}，六城区排名第{}。\n     PM2.5实时浓度为{}μg/m³，" \
        "今日{}时平均浓度为{}μg/m³；\n     PM10实时浓度为{}μg/m³，今日{}时平均浓度为{}μg/m³" \
        "；\n     SO2实时浓度为{}μg/m³，今日{}时平均浓度为{}μg/m³；\n     NO2实时浓度为{}μg/m³，" \
        "今日{}时平均浓度为{}μg/m³；\n     从变化趋势图来看，西山点位{}呈{}趋势。\n      当前气象条件：{}，相对湿度{}，预计未来几个小时我区空气质量以{}为主。".format(
        "2020年11月4日 6时", "95", "二级良",
        "PM10", "十一", "六", "40", "1-6", "30", "140",
        "1-6", "114", "15",
        "1-6", "14", "69", "1-6", "62", "、".join(['PM2.5浓度', 'PM10浓度', 'SO2浓度', 'NO2浓度']), "上升", "西南风一级",
        "47%", "二级")
    send_text(name,l)

    # 发送excel表格
    excel_file_dir = r'excelfiles\万柏林数据.xlsx'
    excel_filenew_dir = r'excelfiles\万柏林数据排名.xlsx'
    excel_filerank_dir = r'excelfiles\万柏林数据排名充填.xlsx'
        # 必须要绝对路径
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\万柏林数据排名充填插入.xlsx'
    excel_add_name = '排名'
    rank_name = 'AQI'
    name_c = '西山'
    name_table = '2020年11月4日6时AQI排名'
    send_excelpic(name,excel_file_dir,excel_filenew_dir,excel_add_name,rank_name,name_c,excel_filerank_dir,name_table,excel_rank_insert)

    # 发送折线图
    excel_file_dir = r'excelfiles\万柏林区详细数据.xlsx'
    image_file = r'image_file'
    send_line_pic(name,excel_file_dir,image_file)



def send_excelpic_rb(name,excel_file_dir,excel_filenew_dir,excel_add_name,rank_name,name_table,excel_rank_insert):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_rb(excel_file_dir,excel_filenew_dir,excel_add_name,rank_name)
    make_excel.table_font_rb(excel_filenew_dir,name_table,excel_rank_insert)
    send_text_image.excel_catch_screen_rb(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)

def send_excelpic_rbdoble(name, excel_filePM25_dir,excel_filePM10_dir,excel_filenewPM25_dir,excel_filenewPM10_dir,excel_rank_insert1,excel_rank_insert2,excel_add_name,rank_name1,rank_name2,name_table1,name_table2):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_rb(excel_filePM25_dir,excel_filenewPM25_dir,excel_add_name,rank_name1)
    make_excel.table_font_db(excel_filenewPM25_dir, name_table1, excel_rank_insert1)
    send_text_image.excel_catch_screen_db(excel_rank_insert1)
    windows_opr.send()

    make_excel.excel_rank_rb(excel_filePM10_dir, excel_filenewPM10_dir, excel_add_name, rank_name2)
    make_excel.table_font_db(excel_filenewPM10_dir,name_table2,excel_rank_insert2)
    send_text_image.excel_catch_screen_db(excel_rank_insert2)
    windows_opr.send()
    windows_opr.CloseWindow(name)

def wanbairb():
    # 发送文本
    name = '王彦军'
    l = "【万柏林区{}微观站日报】\n各位领导，{}我区" \
        "各乡/街道 PM10 浓度排名和微观点位颗粒物浓度后十位排名，具体情况如下表所示：\n" \
        "当前气象条件：{}，相对湿度{}%，预计未来几个小时我区空气质量以{}。".format('2020年11月3日','2020年11月3日',
                                                          '南风一级','54','三级为主'
        )
    send_text(name,l)
    # 发第一个表格
    excel_file_dir = r'excelfiles\万柏林乡镇街道数据.xlsx'
    excel_filenew_dir = r'excelfiles\万柏林乡镇街道数据排名.xlsx'
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\万柏林乡镇街道数据排名插入.xlsx'
    excel_add_name = '排名'
    rank_name = 'PM10（μg/m3）'
    name_table = '万柏林区各乡镇街道PM10排名情况（2020-11-03）'
    send_excelpic_rb(name,excel_file_dir,excel_filenew_dir,excel_add_name,rank_name,name_table,excel_rank_insert)

    excel_filePM25_dir = r'excelfiles\万柏林微观站后十名PM2.5数据.xlsx'
    excel_filePM10_dir = r'excelfiles\万柏林微观站后十名PM10数据.xlsx'
    excel_filenewPM25_dir = r'excelfiles\万柏林微观站后十名PM2.5数据排名.xlsx'
    excel_filenewPM10_dir = r'excelfiles\万柏林微观站后十名PM10数据排名.xlsx'
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\万柏林微观站PM2.5后十名数据排名插入.xlsx'
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\万柏林微观站PM10后十名数据排名插入.xlsx'
    excel_add_name = '排名'
    rank_name1 = 'PM2.5（μg/m3)'
    rank_name2 = 'PM10（μg/m3)'
    name_table1= '万柏林区微观站PM2.5浓度后十名排名情况（2020-11-03）'
    name_table2 = '万柏林区微观站PM10浓度后十名排名情况（2020-11-03）'
    send_excelpic_rbdoble(name, excel_filePM25_dir,excel_filePM10_dir,excel_filenewPM25_dir,excel_filenewPM10_dir,excel_rank_insert1,excel_rank_insert2,excel_add_name,rank_name1,rank_name2,name_table1,name_table2)



def send_excel_pic(name,excel_file_dir,excel_filenew_dir,rank_name,name_table,excel_rank_insert,excel_lable):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_str(excel_file_dir, excel_filenew_dir,rank_name)
    make_excel.table_font_str(excel_filenew_dir, name_table, excel_rank_insert,excel_lable)
    send_text_image.excel_catch_screen_str(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def wanbaistr():
    # 发送文本
    name = '王彦军'
    l = "各位领导，{}我区各乡街的空气质量日报如下，请查收。".format('2020年11月3日')
    send_text(name,l)

    # 发送excel截图
    excel_file_dir = r'excelfiles\万柏林区各乡镇空气质量日报.xlsx'
    excel_filenew_dir = r'excelfiles\万柏林区各乡镇空气质量日报排名.xlsx'
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\万柏林区各乡镇空气质量日报排名插入.xlsx'
    rank_name = 'AQI'
    name_table = '（2020-11-03）万柏林区各乡镇空气质量日报'
    excel_lable = '备注：所有站点各乡街数据采用各自辖区内的微观站监测数据的平均值进行计算'
    send_excel_pic(name,excel_file_dir,excel_filenew_dir,rank_name,name_table,excel_rank_insert,excel_lable)




def send_excelbz_pic(name,excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,excel_filerank_dir1,excel_filerank_dir2):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_str(excel_file_dir1, excel_filenew_dir1, rank_name)
    make_excel.excel_bz_six(excel_filenew_dir1,name_c1,excel_filerank_dir1)
    make_excel.table_font_six(excel_filerank_dir1, name_table1, excel_rank_insert1)
    send_text_image.excel_catch_screen_six(excel_rank_insert1)
    windows_opr.send()

    make_excel.excel_rank_str(excel_file_dir2, excel_filenew_dir2, rank_name)
    make_excel.excel_bz_any(excel_filenew_dir2, name_c2, excel_filerank_dir2)
    make_excel.table_font_any(excel_filerank_dir2, name_table2, excel_rank_insert2)
    send_text_image.excel_catch_screen_any(excel_rank_insert2)
    windows_opr.send()
    windows_opr.CloseWindow(name)



def wanbaibz():
    # 发送文本
    name = '王彦军'
    l = "【万柏林区{}空气质量日报】\n{}，万柏林区综合" \
        "指数为{}，在太原市六城区中排名{}。太原市全市AQI为{}，{}，首要" \
        "污染物：{}。万柏林区全区AQI值为{}，{}，首要污染物：{}，在太原市六" \
        "城区中排名{}。在太原市11个标准站中，西山点位AQI值为{}，排名{}。\n当前气象" \
        "条件：{}，相对湿度{}%，预计未来几个小时我区空气质量以{}。".format('2020年11月3日','2020年11月3日','3.22',
                                                     '第一' ,'70','二级良','NO2','56','二级良','PM10','第一','56',
                                                      '第二','南风二级','38','三级为主')
    send_text(name,l)

    # 发送excel截图
    excel_file_dir1 = r'excelfiles\太原市六城区空气质量日报.xlsx'
    excel_file_dir2 = r'excelfiles\太原市六城区标站空气质量日报.xlsx'
    excel_filenew_dir1 = r'excelfiles\太原市六城区空气质量日报排名.xlsx'
    excel_filenew_dir2 = r'excelfiles\太原市六城区标站空气质量日报排名.xlsx'
    excel_filerank_dir1 = r'excelfiles\太原市六城区空气质量日报排名充填.xlsx'
    excel_filerank_dir2 = r'excelfiles\太原市六城区标站空气质量日报排名充填.xlsx'
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\太原市六城区空气质量日报排名插入.xlsx'
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\太原市六城区标站空气质量日报排名插入.xlsx'
    rank_name = 'AQI'
    name_c1 = '万柏林区'
    name_c2 = '西山'
    name_table1 = '2020年11月3日全市六城区综合指数排名情况'
    name_table2 = '2020年11月3日全市所有标站AQI排名情况'
    send_excelbz_pic(name,excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,excel_filerank_dir1,excel_filerank_dir2)




def send_exceladd_pic(name,excel_file_dir,excel_filenew_dir,excel_filerank_dir,excel_rank_insert,rank_name,name_c,name_table):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_str(excel_file_dir, excel_filenew_dir, rank_name)
    make_excel.excel_add(excel_filenew_dir, name_c, excel_filerank_dir)
    make_excel.color_scale(excel_filerank_dir)
    make_excel.table_font_add(excel_filerank_dir, name_table, excel_rank_insert)
    send_text_image.excel_catch_screen_add(excel_rank_insert)
    windows_opr.send()



def wanbaiadd():
    # 发送文本
    name = '王彦军'
    l = "【夜间累计浓度变化情况】\n{}时，西山点位累计AQI" \
        "为{}，{}，首要污染物：{}，今日{}时PM2.5平均浓度为{}μg/m³；今" \
        "日{}时PM10平均浓度为{}μg/m³。\n 当前气象条件：{}，相对湿度{}%，预计未" \
        "来几个小时我区空气质量以{}。".format('2020年11月2日20','44','一级优','无',
                                   '1-20','9','1-20','44','西北风二级','30','一级为主')
    send_text(name,l)



    # 发送excel截图
    excel_file_dir = r'excelfiles\太原市六城区空气质量累计日报.xlsx'
    excel_filenew_dir = r'excelfiles\太原市六城区空气质量累计日报排名.xlsx'
    excel_filerank_dir = r'excelfiles\太原市六城区空气质量累计日报排名充填.xlsx'
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\万柏林\excelfiles\太原市六城区空气质量累计日报排名插入.xlsx'
    rank_name = 'PM2.5'
    name_c = '西山'
    name_table = '备注：各点位按PM2.5当日累计浓度排序'

    send_exceladd_pic(name,excel_file_dir,excel_filenew_dir,excel_filerank_dir,excel_rank_insert,rank_name,name_c,name_table)
