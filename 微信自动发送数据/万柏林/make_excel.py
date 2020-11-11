import pandas as pd
import openpyxl.styles
from openpyxl.styles import Border,Side
from openpyxl.styles import PatternFill
import openpyxl
import openpyxl.styles
from openpyxl.styles import Alignment
from openpyxl.styles import Font
import xlrd
import xlwt
from pandas import read_csv
import glob




# excel根据字段排名
def excel_rank(excel_file_dir,excel_filenew_dir,excel_add_name,rank_name):
    df = pd.read_excel(excel_file_dir)
    df[excel_add_name] = df[rank_name].rank(method='min',ascending=True)
    df = df.sort_values(by=rank_name)
    df.reset_index(drop=True, inplace=True)
    df.to_excel(excel_filenew_dir,index=False)

# excel根据字段排名
def excel_rank_rb(excel_file_dir,excel_filenew_dir,excel_add_name,rank_name):
    df = pd.read_excel(excel_file_dir)
    df = df.sort_values(by=rank_name,ascending=False)
    df[excel_add_name] = df[rank_name].rank(method='min', ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.to_excel(excel_filenew_dir,index=False)

def excel_rank_str(excel_file_dir,excel_filenew_dir,rank_name):
    df = pd.read_excel(excel_file_dir)
    df = df.sort_values(by=rank_name)
    df.reset_index(drop=True, inplace=True)
    df.to_excel(excel_filenew_dir,index=False)

# 充填行，按照AQI
def excel_c(excel_filenew_dir,name_c,excel_filerank_dir):
    wb = openpyxl.load_workbook(excel_filenew_dir)
    sheet = wb["Sheet1"]
    n = 0
    for i in range(1,13):
        if sheet.cell(i, 1).value == name_c:
            n = i
    if 50 >= sheet.cell(n, 2).value >= 0:
        color = '00E400'
    elif 100 >= sheet.cell(n, 2).value > 50:
        color = 'FFFF00'
    elif 150 >= sheet.cell(n, 2).value > 100:
        color = 'FF7E00'
    elif 200 >= sheet.cell(n, 2).value > 150:
        color = 'FF0000'
    elif 300 >= sheet.cell(n, 2).value > 200:
        color = '99004C'
    else:
        color = '7E0023'
    fille=PatternFill("solid",fgColor=color)
    for j in range(1,6):
        sheet.cell(n, j).fill = fille
    wb.save(excel_filerank_dir)



#居中对齐，通过遍历方式实现
def set_from_center(excel_rank_insert):
    fileName = excel_rank_insert
    data = openpyxl.load_workbook(fileName)
    table = data.get_sheet_by_name("Sheet1")
    nrows = table.max_row # 获得行数
    ncols = table.max_column
    for i in range(nrows):
        for j in range(ncols):
            table.cell(row=i+1, column=j+1).alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
    data.save(fileName)

def table_border(excel_rank_insert):
    wb = openpyxl.load_workbook(excel_rank_insert)
    # sheet = wb["Sheet1"]
    ws = wb.get_sheet_by_name("Sheet1")
    nrows = ws.max_row
    ncols = ws.max_column
    for i in range(nrows):
        for j in range(ncols):
            border = Border(left=Side(border_style='thin', color ='000000'),
            right = Side(border_style='thin', color ='000000'),
            top = Side(border_style='thin', color ='000000'),
            bottom = Side(border_style='thin', color ='000000'))
            ws.cell(i+1, j+1).border = border
    wb.save(excel_rank_insert)


def table_font(excel_filerank_dir,name_table,excel_rank_insert):
    wb = openpyxl.load_workbook(excel_filerank_dir)
    sheet = wb["Sheet1"]
    sheet.insert_rows(1)
    sheet.column_dimensions['A'].width = 10
    sheet.column_dimensions['C'].width = 12
    sheet.column_dimensions['D'].width = 15
    sheet.row_dimensions[1].height = 20
    sheet.cell(1, 1).value = name_table
    sheet["A1"].font = Font(size = 16,bold = True,color = "FF0000")
    sheet.merge_cells('A1:E1')
    wb.save(excel_rank_insert)
    set_from_center(excel_rank_insert)
    table_border(excel_rank_insert)


def table_font_rb(excel_filenew_dir,name_table,excel_rank_insert):
    wb = openpyxl.load_workbook(excel_filenew_dir)
    sheet = wb["Sheet1"]
    sheet.insert_rows(1)
    sheet.column_dimensions['A'].width = 20
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['C'].width = 20
    sheet.row_dimensions[1].height = 20
    sheet.cell(1, 1).value = name_table
    sheet["A1"].font = Font(size = 14,bold = True,color = "FF0000")
    sheet.merge_cells('A1:C1')
    wb.save(excel_rank_insert)
    set_from_center(excel_rank_insert)
    table_border(excel_rank_insert)


def table_font_db(excel_filenew_dir,name_table,excel_rank_insert):
    wb = openpyxl.load_workbook(excel_filenew_dir)
    sheet = wb["Sheet1"]
    sheet.insert_rows(1)
    sheet.column_dimensions['A'].width = 20
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['C'].width = 20
    sheet.row_dimensions[1].height = 30
    sheet.cell(1, 1).value = name_table
    sheet["A1"].font = Font(size = 14,bold = True,color = "FF0000")
    sheet.merge_cells('A1:D1')
    wb.save(excel_rank_insert)
    set_from_center(excel_rank_insert)
    table_border(excel_rank_insert)


def table_font_str(excel_filenew_dir,name_table,excel_rank_insert,excel_lable):
    wb = openpyxl.load_workbook(excel_filenew_dir)
    sheet = wb["Sheet1"]
    sheet.insert_rows(1)
    sheet.column_dimensions['A'].width = 18
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 20
    sheet.column_dimensions['E'].width = 18
    sheet.row_dimensions[1].height = 30
    sheet.cell(1, 1).value = name_table
    sheet["A1"].font = Font(size = 14,bold = True,color = "FF0000")
    sheet.merge_cells('A1:E1')
    sheet.cell(18, 1).value = excel_lable
    sheet["A18"].font = Font(size=10, bold=True, color="FF0000")
    sheet.merge_cells('A18:E18')
    sheet['A18'].alignment = Alignment(horizontal='left', vertical='center')
    wb.save(excel_rank_insert)
    set_from_center(excel_rank_insert)
    table_border(excel_rank_insert)


# def excel_merge(excel_filenewPM25_dir,excel_filenewPM10_dir,excel_filenewdouble_dir):
#     df = read_csv(excel_filenewPM25_dir, header=None)
#     sample_name = df[0]
#
#     file = "combine"
#     filedestination = "E://excel//"
#
#     # from numpy import *
#     filearray = []
#     for filename in glob.glob(r'E:\excel\*.xlsx'):
#         filearray.append(filename)
#         # 以上是从excel 文件夹下读取所有excel表格，并将所有的名字存储到列表filearray
#     print("在默认文件夹下有%d个文档哦" % len(filearray))
#     ge = len(filearray)
#     matrix = [None] * ge
#
#
#     for i in range(ge):
#         fname = filearray[i]
#         bk = xlrd.open_workbook(excel_filenewPM10_dir)
#         try:
#             sh = bk.sheet_by_name("Sheet1")
#         except:
#             print("在文件%s中没有找到sheet1，读取文件数据失败,要不你换换表格的名字？" % fname)
#
#         ncols = sh.ncols
#         matrix[i] = [0] * (ncols - 1)
#         nrows = sh.nrows
#         for m in range(ncols - 1):
#             matrix[i][m] = ["0"] * nrows
#
#         for k in range(1, ncols):
#             for j in range(0, nrows):
#                 matrix[i][k - 1][j] = sh.cell(j, k).value
#
#
#     filename = xlwt.Workbook(excel_filenewPM10_dir)
#     sheet = filename.add_sheet("Sheet1")
#     # 下面是把第一列写上
#     for i in range(0, len(sample_name)):
#         sheet.write(i, 0, sample_name[i])
#         # 求和前面的文件一共写了多少列
#     zh = 1
#     for i in range(ge):
#         for j in range(len(matrix[i])):
#             for k in range(len(matrix[i][j])):
#                 sheet.write(k, zh, matrix[i][j][k])
#             zh = zh + 1
#     print("我已经将%d个文件合并成1个文件，并命名为%s.xlsx." % (ge, file))
#     filename.save(excel_filenewdouble_dir)
