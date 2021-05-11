import pandas as pd
import xlwt


book = xlwt.Workbook()

df = pd.read_excel('探空数据1.xls')
print(len(df))
for k in range(len(df)):
    xl = df.loc[k]
    sheet = book.add_sheet(xl['vt'][0:13])
    print(xl['vt'][0:13])
    names = ['HGT','UGRD','VGRD','TMP','RH','pressure']
    n = 1
    ll = len(names)
    for l in range(ll):
        sheet.write(0, l, names[l])
    for i in range(1000,75,-25):
        for name in range(len(names)):
            if names[name] == 'pressure':
                sheet.write(n, name, i)
            else:
                # print(names[name]+'_'+str(i))
                sheet.write(n, name, xl[names[name]+'_'+str(i)].astype('float'))
        n += 1

book.save(r'探空数据2.xls')



