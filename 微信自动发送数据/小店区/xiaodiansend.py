import make_excel
import send_text_image
import windows_opr
import xiaodian_spider


def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)

def send_excel_pic(name, excel_file_dir, excel_filenew_dir, excel_filerank_dir, excel_rank_insert, rank_name, name_c,name_table):
    windows_opr.FindWindow(name)
    make_excel.excel_rank(excel_file_dir,excel_filenew_dir,rank_name)
    make_excel.excel_c(excel_filenew_dir,name_c,excel_filerank_dir)
    make_excel.table_font(excel_filerank_dir,name_table,excel_rank_insert)
    send_text_image.excel_catch_screen(excel_rank_insert)
    windows_opr.send()
    windows_opr.CloseWindow(name)

def send_excel_pic_doble(name, excel_file_dir1, excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name1,rank_name2,name_table1,name_table2):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_rb(excel_file_dir1,excel_filenew_dir1,rank_name1)
    make_excel.table_font_db(excel_filenew_dir1, name_table1, excel_rank_insert1)
    send_text_image.excel_catch_screen_db(excel_rank_insert1)
    windows_opr.send()

    make_excel.excel_rank_rb(excel_file_dir2, excel_filenew_dir2, rank_name2)
    make_excel.table_font_db(excel_filenew_dir2,name_table2,excel_rank_insert2)
    send_text_image.excel_catch_screen_db(excel_rank_insert2)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def daily():
    # 发送文本
    name = '王彦军'
    l = "【空气质量播报】\n{}，小店区综合指数为{}，城六区排名{}：\n" \
        "太原六区综合指数由小到大排名如下：\n" \
        "{}综合指数为{}，排名{}；\n" \
        "{}综合指数为{}，排名{}；\n" \
        "{}综合指数为{}，排名{}；\n" \
        "{}综合指数为{}，排名{}；\n" \
        "{}综合指数为{}，排名{}；\n" \
        "{}综合指数为{}，排名{}。".format('2020年11月3日','4.94','第六','万柏林区','3.22','第一',
                                    '尖草坪区','3.83','第二','迎泽区','4.27','第三','晋源区','4.35','第四',
                                    '杏花岭区','4.56','第五','小店区','4.94','第六')
    send_text(name, l)

    # 发送excel截图
    excel_file_dir = r'excelfiles\小店区日报数据.xlsx'
    excel_filenew_dir = r'excelfiles\小店区日报数据日报排名.xlsx'
    excel_filerank_dir = r'excelfiles\小店区日报数据排名充填.xlsx'
    excel_rank_insert = r'D:\Program Files\pycharm\微信自动发送数据\小店区\excelfiles\小店区日报数据排名插入.xlsx'
    rank_name = '排名'
    name_c = '小店区'
    name_table = '空气质量播报'
    send_excel_pic(name, excel_file_dir, excel_filenew_dir, excel_filerank_dir, excel_rank_insert, rank_name, name_c,name_table)


    l = "{}小店区街道乡镇PM2.5、PM10浓度均值排名如下表所示：".format('2020年11月3日')
    send_text(name, l)


    # 发送excel截图
    excel_file_dir1 = r'excelfiles\小店区街道乡镇PM2.5数据.xlsx'
    excel_file_dir2 = r'excelfiles\小店区街道乡镇PM10数据.xlsx'
    excel_filenew_dir1 = r'excelfiles\小店区街道乡镇数据PM2.5排名.xlsx'
    excel_filenew_dir2 = r'excelfiles\小店区街道乡镇数据PM10排名.xlsx'
    # excel_filerank_dir1 = r'excelfiles\小店区街道乡镇数据PM2.5排名充填.xlsx'
    # excel_filerank_dir2 = r'excelfiles\小店区街道乡镇数据PM10排名充填.xlsx'
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\小店区\excelfiles\小店区街道乡镇数据PM2.5排名插入.xlsx'
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\小店区\excelfiles\小店区街道乡镇数据PM10排名插入.xlsx'
    rank_name1 = 'PM2.5'
    rank_name2 = 'PM10'
    name_table1= '2020年11月03日小店区街道乡镇审核前PM2.5浓度均值排名'
    name_table2 = '2020年11月03日小店区街道乡镇审核前PM10浓度均值排名'

    send_excel_pic_doble(name, excel_file_dir1, excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name1,rank_name2,name_table1,name_table2)




def send_excel_pic_hour(name, excel_file_dir1, excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_filerank_dir1,excel_filerank_dir2,excel_rank_insert1,excel_rank_insert2,rank_name1,rank_name2,name_table1,name_table2,name_c1,name_c2):
    windows_opr.FindWindow(name)
    print('窗口打开成功')
    make_excel.excel_rank_rb(excel_file_dir1,excel_filenew_dir1,rank_name1)
    print('综合指数数排名成功')
    make_excel.excel_c_hour(excel_filenew_dir1,name_c1,name_c2,excel_filerank_dir1)
    print('综合指数数表格颜色充填成功')
    make_excel.table_font_hour(excel_filerank_dir1, name_table1, excel_rank_insert1)
    print('综合指数数表格表头插入成功')
    send_text_image.excel_catch_screen_hour(excel_rank_insert1)
    print('综合指表格成功截图')
    windows_opr.send()
    print('综合指数数发送成功')

    make_excel.excel_rank_rb(excel_file_dir2, excel_filenew_dir2, rank_name2)
    print('AQI数据排名成功')
    make_excel.excel_czh_hour(excel_filenew_dir2, name_c1, name_c2, excel_filerank_dir2)
    print('AQI数据表格颜色充填成功')
    make_excel.table_font_hour(excel_filerank_dir2, name_table2, excel_rank_insert2)
    print('AQI数据表格表头插入成功')
    send_text_image.excel_catch_screen_hour(excel_rank_insert2)
    print('AQI表格成功截图')
    windows_opr.send()
    print('AQI数数发送成功')
    windows_opr.CloseWindow(name)
    print('窗口关闭成功')



def hoursend(name):
    xiaodian_spider.zonghe()
    print('综合指数数据获取成功')
    sl = xiaodian_spider.aqi()
    print('AQI数据获取成功')
    # 发送excel截图
    excel_file_dir1 = r'excelfiles\小店区两站点AQI数据.xls'
    excel_file_dir2 = r'excelfiles\小店区两站点综合指数数据.xls'
    excel_filenew_dir1 = r'excelfiles\小店区两站点AQI数据排名.xlsx'
    excel_filenew_dir2 = r'excelfiles\小店区两站点综合指数数据排名.xlsx'
    excel_filerank_dir1 = r'excelfiles\小店区两站点AQI数据排名充填.xlsx'
    excel_filerank_dir2 = r'excelfiles\小店区两站点综合指数数据排名充填.xlsx'
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\小店区\excelfiles\小店区两站点AQI数据排名插入.xlsx'
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\小店区\excelfiles\小店区两站点综合指数数据排名插入.xlsx'
    rank_name1 = 'AQI'
    rank_name2 = '综合指数'
    name_c1 = '坞城'
    name_c2 = '小店'
    name_table1 = '{}小店区2站点AQI排名'.format(sl)
    name_table2 = '{}小店区2站点综合指数排名'.format(sl)

    send_excel_pic_hour(name, excel_file_dir1, excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_filerank_dir1,excel_filerank_dir2,excel_rank_insert1,excel_rank_insert2,rank_name1,rank_name2,name_table1,name_table2,name_c1,name_c2)
