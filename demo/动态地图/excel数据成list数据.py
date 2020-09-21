#coding=utf-8
import xlrd
import json


class excel_read:
    def __init__(self, excel_path=r'E:\周口淮阳项目\汇报文件\8月份\乡镇小时数据\9月1日1时至9日0时\demo1.xlsx',encoding='utf-8',index=0):

      self.data=xlrd.open_workbook(excel_path)  ##获取文本对象
      self.table=self.data.sheets()[index]     ###根据index获取某个sheet
      self.rows=self.table.nrows   ##3获取当前sheet页面的总行数,把每一行数据作为list放到 list



    def get_data(self):
        result=[]
        for i in range(self.rows):
            col=self.table.row_values(i)  ##获取每一列数据
            print(col)
            result.append(col)
        print(result)
        return result

if __name__ == '__main__':
    result = excel_read().get_data()
    with open("result.json", "w") as f:
        json.dump(result, f)
        print("加载入文件完成...")




        ##获取的结果样式[[],[],[],[]]
