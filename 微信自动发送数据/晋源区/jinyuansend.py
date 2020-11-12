import make_excel
import send_text_image
import windows_opr



def send_text(name,l):
    windows_opr.FindWindow(name)
    send_text_image.setText(l)
    windows_opr.send()
    windows_opr.CloseWindow(name)


def send_excel_pic_hour(name,excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,name_c3,excel_filerank_dir1,excel_filerank_dir2):
    windows_opr.FindWindow(name)
    make_excel.excel_rank_str(excel_file_dir1, excel_filenew_dir1, rank_name)
    make_excel.excel_bz_hour(excel_filenew_dir1,name_c1,excel_filerank_dir1)
    make_excel.table_font_any(excel_filerank_dir1, name_table1, excel_rank_insert1)
    send_text_image.excel_catch_screen_hour1(excel_rank_insert1)
    windows_opr.send()

    make_excel.excel_rank_str(excel_file_dir2, excel_filenew_dir2, rank_name)
    make_excel.excel_bz_any(excel_filenew_dir2, name_c2, excel_filerank_dir2)
    make_excel.excel_bz_any(excel_filerank_dir2, name_c3, excel_filerank_dir2)
    make_excel.table_font_any(excel_filerank_dir2, name_table2, excel_rank_insert2)
    send_text_image.excel_catch_screen_any(excel_rank_insert2)
    windows_opr.send()
    windows_opr.CloseWindow(name)



def hoursend():
    name = '王彦军'
    l = '【{}时AQI排名情况】\n{} {}时，晋源' \
        '区AQI为{}，{},首要污染物：{}，在六城区' \
        '中排名{}；\n晋源点位：AQI为{}，{},首要污' \
        '染物：{}，在全市11个标准站中排名{}；金胜' \
        '点位：AQI为{}，{},首要污染物：{}，在全市11个标准站中排名{}。'.format('9','2020年3月20日',
                                                                '9','105','三级轻度污染','PM10','并列第三',
                                                                '105','三级轻度污染','PM10','并列第六','105',
                                                               '三级轻度污染','PM10','并列第六')
    send_text(name, l)


    # 发送excel截图
    excel_file_dir1 = r'excelfiles\太原市六城区空气质量日报.xlsx'
    excel_file_dir2 = r'excelfiles\太原市六城区标站空气质量日报.xlsx'
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
    name_table1 = '2020年3月20日9时区域AQI排名'
    name_table2 = '2020年3月20日9时区域AQI排名'
    send_excel_pic_hour(name,excel_file_dir1,excel_file_dir2,excel_filenew_dir1,excel_filenew_dir2,excel_rank_insert1,excel_rank_insert2,rank_name,name_table1,name_table2,name_c1,name_c2,name_c3,excel_filerank_dir1,excel_filerank_dir2)

