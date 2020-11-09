import openpyxl
import openpyxl.styles
from openpyxl.styles import Alignment
from openpyxl.styles import Font


#居中对齐，通过遍历方式实现
def set_from_center():
    fileName = r"D:\Program Files\pycharm\机器人发送数据\周口市区县数据累积排名插入.xlsx"
    data = openpyxl.load_workbook(fileName)
    table = data.get_sheet_by_name("Sheet1")
    nrows = table.max_row # 获得行数
    ncols = table.max_column
    for i in range(nrows):
        for j in range(ncols):
            table.cell(row=i+1, column=j+1).alignment = Alignment(horizontal='center', vertical='center')
    data.save(fileName)


def table_font(name):
    wb = openpyxl.load_workbook(r"D:\Program Files\pycharm\机器人发送数据\周口市区县数据累积排名充填.xlsx")
    sheet = wb["Sheet1"]
    sheet.insert_rows(1)
    sheet.cell(1, 1).value = name
    sheet["A1"].font = Font(size = 15,bold = True,color = "000000")
    sheet.merge_cells('A1:J1')
    wb.save(r"D:\Program Files\pycharm\机器人发送数据\周口市区县数据累积排名插入.xlsx")
    set_from_center()
