import json
import xlwt



def save_excel(dat):
    book = xlwt.Workbook()
    sheet = book.add_sheet('淮阳县空气质量累积数据')
    n = 1
    sheet.write(0,0,'经度')
    sheet.write(0,1,'纬度')
    sheet.write(0,2,'PM2.5')
    data = json.loads(dat)['info']
    for k in data:
        print(k)
        sheet.write(n, 0, k['x'])
        sheet.write(n, 1, k["y"])
        n+=1
    book.save('data.xls')


path = 'station.json'
data = open(path,'r', encoding="utf-8")
dat = data.read()
save_excel(dat)
