import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib



def line_barpm10(hour_d):
    df = pd.read_excel(r'D:\Program Files\pycharm\机器人发送数据\周口市区县数据累积排名PM10.xlsx')
    plt.figure()
    for i in range(len(df["区县"])):
        if 50 >= df["PM10"][i] >= 0:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#00E400',edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#00E400')
        elif 150 >= df["PM10"][i] > 50:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FFFF00', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FFFF00')
        elif 250 >= df["PM10"][i] > 150:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FF7E00', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FF7E00')
        elif 350 >= df["PM10"][i] > 250:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FF0000', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#FF0000')
        elif 420 >= df["PM10"][i] > 350:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#99004C', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#99004C')
        else:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM10"][i], fc='#7E0023', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM10"][i], fc='#7E0023')
    for i in range(len(df["PM10"])):
        plt.text(df["区县"][i], df["PM10"][i] + 0.5, '%s' % round(df["PM10"][i], 3), ha='center', fontsize=10)
    # plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title(u"周口市九区县截止今日{}时PM10累计浓度柱状图".format(hour_d), fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    print(len(df["PM10"]))
    # 保存图片到本地
    plt.savefig('image/pci1.png')
    matplotlib.use('Agg')
    # 显示图片
    plt.show()


line_barpm10("12")