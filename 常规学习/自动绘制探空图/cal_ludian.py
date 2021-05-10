import math
import pandas as pd
import xlwt


def cal_lu(t,rh):
    a = 6.11
    b = 17.67
    c = 257.14
    d = 234.5
    try:
        ym = math.log(rh*math.exp((b-(t/d))*(t/(c+t)))/100,math.e)
        bhsq = a*math.exp((b-(t/d))*(t/(c+t)))
        tdp = (c*ym)/(b-ym)
        return tdp
    except:
        return 0


df = pd.read_excel('探空数据2.xls',sheet_name=None)
writer = pd.ExcelWriter('tankong.xlsx',mode = 'a',engine='openpyxl')
n = 0
for k in df.keys():
    df = pd.read_excel('探空数据2.xls',sheet_name=k)
    df['TMP'] = df['TMP'].astype("float")
    df['RH'] = df['RH'].astype("float")
    df['dewpoint'] = df.apply(lambda row:cal_lu(row['TMP'],row['RH']),axis=1)
    df.to_excel(writer,sheet_name=k)
    print(df)
writer.save()
