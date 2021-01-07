import requests
from lxml import etree
import xlwt

urlx = 'https://jieqi.supfree.net/cntv.asp?n='
book = xlwt.Workbook()
session = requests.Session()
for i in range(2015, 2021):
    url = urlx + str(i)
    sheet = book.add_sheet(str(i))
    resp = session.get(url)
    resp.encoding = 'gb2312'
    rep = etree.HTML(resp.text)
    a = rep.xpath('//table/tr/td/a/text()')
    b = rep.xpath('//table/tr/td/text()')
    for i in range(len(a)):
        sheet.write(i, 0, a[i])
        sheet.write(i, 1, b[i])

book.save('bookname.xls')