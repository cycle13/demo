import make_excel
import send_text_image
import windows_opr
import jinyuan_spider



def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excel_pic_hour(excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,name_c3,excel_filerank_dir1,excel_filerank_dir2):
    make_excel.excel_rank_str(excel_file_dir1, excel_filenew_dir1, rank_name)
    l = make_excel.excel_bz_hour(excel_filenew_dir1,name_c1,excel_filerank_dir1)
    make_excel.table_font_any(excel_filerank_dir1, name_table1, excel_rank_insert1)


    make_excel.excel_rank_str(excel_file_dir2, excel_filenew_dir2, rank_name)
    m = make_excel.excel_bz_any(excel_filenew_dir2, name_c2, excel_filerank_dir2)
    n = make_excel.excel_bz_any(excel_filerank_dir2, name_c3, excel_filerank_dir2)
    make_excel.table_font_any(excel_filerank_dir2, name_table2, excel_rank_insert2)
    return (l,m,n)


def send_excel(name,excel_rank_insert1,excel_rank_insert2):
    windows_opr.FindWindow(name)
    send_text_image.excel_catch_screen_hour1(excel_rank_insert1)
    windows_opr.send()
    send_text_image.excel_catch_screen_any(excel_rank_insert2)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def hoursend():
    sl = jinyuan_spider.location()
    sx = jinyuan_spider.station()
    name = '王彦军'
    # l = '【{}时AQI排名情况】\n{} {}时，晋源' \
    #     '区AQI为{}，{},首要污染物：{}，在六城区' \
    #     '中排名{}；\n晋源点位：AQI为{}，{},首要污' \
    #     '染物：{}，在全市11个标准站中排名{}；金胜' \
    #     '点位：AQI为{}，{},首要污染物：{}，在全市11个标准站中排名{}。'.format(sl[1],'2020年3月20日',
    #                                                             '9','105','三级轻度污染','PM10','并列第三',
    #                                                             '105','三级轻度污染','PM10','并列第六','105',
    #                                                            '三级轻度污染','PM10','并列第六')
    # send_text(name, l)


    # 发送excel截图
    excel_file_dir1 = r'excelfiles\太原市六城区空气质量日报.xls'
    excel_file_dir2 = r'excelfiles\太原市六城区标站空气质量日报.xls'
    excel_filenew_dir1 = r'excelfiles\太原市六城区空气质量日报排名.xlsx'
    excel_filenew_dir2 = r'excelfiles\太原市六城区标站空气质量日报排名.xlsx'
    excel_filerank_dir1 = r'excelfiles\太原市六城区空气质量日报排名充填.xlsx'
    excel_filerank_dir2 = r'excelfiles\太原市六城区标站空气质量日报排名充填.xlsx'
    excel_rank_insert1 = r'D:\Program Files\pycharm\微信自动发送数据\晋源区\excelfiles\太原市六城区空气质量日报排名插入.xlsx'
    excel_rank_insert2 = r'D:\Program Files\pycharm\微信自动发送数据\晋源区\excelfiles\太原市六城区标站空气质量日报排名插入.xlsx'
    rank_name = 'AQI'
    name_c1 = '晋源区'
    name_c2 = '晋源'
    name_c3 = '金胜'
    name_table1 = '{}区域AQI排名'.format(sl[0])
    name_table2 = '{}站点AQI排名'.format(sx)
    l = send_excel_pic_hour(excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,name_c3,excel_filerank_dir1,excel_filerank_dir2)
    k = '【{}时AQI排名情况】\n{}，晋源' \
        '区AQI为{}，空气质量等级为{},首要污染物：{}，在六城区' \
        '中排名第{}；\n晋源点位：AQI为{}，空气质量等级为{},首要污' \
        '染物：{}，在全市11个标准站中排名第{}；金胜' \
        '点位：AQI为{}，空气质量等级为{},首要污染物：{}，在全市11个标准站中排名第{}。'.format(sl[1], sl[0],
                                                       l[0][0], l[0][1], l[0][2], l[0][3],
                                                       l[1][0], l[1][1], l[1][2], l[1][3], l[2][0],
                                                       l[2][1], l[2][2], l[2][3])
    send_text(name, k)
    send_excel(name, excel_rank_insert1, excel_rank_insert2)


hoursend()