import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import pandas as pd
import requests
import json
import xlwt
import xlrd
from xlutils.copy import copy
from datetime import datetime
import os
import datetime as datatime



session = requests.Session()
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

def day(url,yestoday):
    data = {
        'sort':'asc',
        'time':yestoday
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response


def mean_lj(name):
    df = pd.read_excel(r"excelleiji/周口市区县全年日数据.xls")
    df = df.loc[df['区县'] == name]
    a = df["PM10"]
    b = a[a > 0]
    c = df["PM2.5"]
    d = c[c > 0]
    pm10 = round(b.mean(),2)
    pm25 = round(d.mean(),2)
    return pm25,pm10


def list_num():
    b = []
    numname = []
    numpm25 = []
    numpm10 = []
    name_list = ['沈丘县','商水县','西华县','扶沟县','郸城县','淮阳县','太康县','鹿邑县','项城市']
    for i in name_list:
        a = []
        a.append(i)
        a.append(mean_lj(i)[0])
        a.append(mean_lj(i)[1])
        numname.append(i)
        numpm25.append(mean_lj(i)[0])
        numpm10.append(mean_lj(i)[1])
        b.append(a)
    df = pd.DataFrame(b, columns=['区县', 'PM2.5', 'PM10'])
    df = df.sort_values(by="PM2.5")
    df.reset_index(drop=True, inplace=True)
    df1 = df.sort_values(by="PM10")
    df1.reset_index(drop=True, inplace=True)
    return df,df1

def line_picpm(pm25,title_name,wr_name):
    plt.figure()
    for i in range(len(pm25['区县'])):
        if 35 >= pm25["PM2.5"][i] >= 0:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#00E400',edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#00E400')
        elif 75 >= pm25["PM2.5"][i] > 35:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#FFFF00', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#FFFF00')
        elif 115 >= pm25["PM2.5"][i] > 75:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#FF7E00', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#FF7E00')
        elif 150 >= pm25["PM2.5"][i] > 115:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#FF0000', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i],pm25["PM2.5"][i], fc='#FF0000')
        elif 250 >= pm25[i] > 150:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#99004C', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#99004C')
        else:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#7E0023', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM2.5"][i], fc='#7E0023')
    for i in range(len(pm25["PM2.5"])):
        plt.text(pm25['区县'][i], pm25["PM2.5"][i] + 0.5, '%s' % round(pm25["PM2.5"][i], 3), ha='center', fontsize=10)
    # plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=16)
    plt.title(title_name, fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig('excelimage/'+wr_name+'.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()


def line_picpm10(pm25,title_name,wr_name):
    plt.figure()
    for i in range(len(pm25['区县'])):
        if 50 >= pm25["PM10"][i] >= 0:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#00E400',edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#00E400')
        elif 150 >= pm25["PM10"][i] > 50:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#FFFF00', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#FFFF00')
        elif 250 >= pm25["PM10"][i] > 150:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#FF7E00', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#FF7E00')
        elif 350 >= pm25["PM10"][i] > 250:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#FF0000', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i],pm25["PM10"][i], fc='#FF0000')
        elif 420 >= pm25["PM10"][i] > 350:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#99004C', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#99004C')
        else:
            if pm25['区县'][i] == '淮阳县':
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#7E0023', edgecolor='black',linewidth=2)
            else:
                plt.bar(pm25['区县'][i], pm25["PM10"][i], fc='#7E0023')
    for i in range(len(pm25["PM10"])):
        plt.text(pm25['区县'][i], pm25["PM10"][i] + 0.5, '%s' % round(pm25["PM10"][i], 3), ha='center', fontsize=10)
    # plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=16)
    plt.title(title_name, fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig('excelimage/'+wr_name+'.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()


def save_date(line_date):
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%Y-%m-%d")
    l = day(first_url_day,yestoday)
    data = json.loads(l)['data']
    d1 = datetime(2020, 1, 1)
    d2 = datetime.now()
    n = (int((d2 - d1).days) - 1) * 9
    print(data)
    for k in data:
        if k['city'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市']:
            if not os.path.exists(line_date):
                os.system(line_date)
                workbook = xlwt.Workbook(encoding='utf-8')
                worksheet = workbook.add_sheet('淮阳县空气质量数据')
                worksheet.write(0,0,label = '区县')
                worksheet.write(0,1,label = '时间')
                worksheet.write(0,2,label = 'CO')
                worksheet.write(0,3,label = 'O3')
                worksheet.write(0,4,label = 'SO2')
                worksheet.write(0,5,label = 'NO2')
                worksheet.write(0,6,label = 'PM10')
                worksheet.write(0, 7, label='PM2.5')
                worksheet.write(0,8,label = 'AQI')
                worksheet.write(0,9,label = '首要污染物')
                workbook.save(line_date)
            rb = xlrd.open_workbook(line_date)
            wb = copy(rb)
            sheet = wb.get_sheet(0)
            sheet.write(n+1,0,label = k['city'])
            sheet.write(n+1,1,label = yestoday)
            sheet.write(n+1,2,label = k['co'])
            sheet.write(n+1,3,label = k['o3'])
            sheet.write(n+1,4,label = k['so2'])
            sheet.write(n+1,5,label = k['no2'])
            sheet.write(n+1,6,label = k['pm10'])
            sheet.write(n+1,7,label = k['pm25'])
            sheet.write(n + 1, 8, label=k['aqi'])
            sheet.write(n+1,9,label = k['primary'])
            os.remove(line_date)
            wb.save(line_date)
            n+=1


def year_leiji():
    line_date = r"excelleiji/周口市区县全年日数据.xls"
    save_date(line_date)
    x = list_num()
    yestoday = (datetime.now() + datatime.timedelta(days=-1)).strftime("%m")+"月"+(datetime.now() + datatime.timedelta(days=-1)).strftime("%d")+"日"
    line_picpm(x[0],'2020年截止{}周口市九区县PM2.5年累计柱状图'.format(yestoday),"pm25")
    line_picpm10(x[1],'2020年截止{}周口市九区县PM10年累计柱状图'.format(yestoday),"pm10")
