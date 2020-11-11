import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import pandas as pd


def line_bar(x,y,data1,data3,data4,image_file,name):
    # 创建画布
    plt.figure(figsize=(6, 5))

    '''绘制第一条数据线
    1、节点为圆圈
    2、线颜色为红色
    3、标签名字为y1-data
    '''
    plt.plot(x, y, marker='o', color='blue')
    # plt.tight_layout()
    '''绘制第二条数据线
    1、节点为五角星
    2、线颜色为蓝色
    3、标签名字为y2-data
    '''
    # plt.plot(x, y_2, marker='*', color='b', label=data2)
    # 标注值
    for i in range(len(y)):
        plt.text(x[i], y[i] + 0.5, '%s' % round(y[i], 3), ha='center', fontsize=10)
    # for i in range(len(y_2)):
    #     plt.text(x[i], y_2[i] - 1, '%s' % round(y_2[i], 3), ha='center', fontsize=10, va='bottom')
    # plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    plt.title(data1, fontproperties=font1)
    # 横坐标名称

    plt.xticks(x, x, rotation=90)
    plt.xlabel(data3)
    # 纵坐标名称
    plt.ylabel(data4)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 保存图片到本地
    plt.tight_layout()
    plt.savefig(image_file+'/'+name+'.png')
    plt.ylim(0, 20)
    plt.grid(True)
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()

# 画柱状图
def line_pic(hour_d):
    df = pd.read_excel(r'D:\Program Files\pycharm\机器人发送数据\周口市区县数据累积排名充填.xlsx')
    plt.figure()
    for i in range(len(df["区县"])):
        if 35 >= df["PM2.5"][i] >= 0:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#00E400',edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#00E400')
        elif 75 >= df["PM2.5"][i] > 35:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FFFF00', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FFFF00')
        elif 115 >= df["PM2.5"][i] > 75:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FF7E00', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FF7E00')
        elif 150 >= df["PM2.5"][i] > 115:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FF0000', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#FF0000')
        elif 250 >= df["PM2.5"][i] > 150:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#99004C', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#99004C')
        else:
            if df["区县"][i] == '淮阳县':
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#7E0023', edgecolor='black')
            else:
                plt.bar(df["区县"][i], df["PM2.5"][i], fc='#7E0023')
    for i in range(len(df["PM2.5"])):
        plt.text(df["区县"][i], df["PM2.5"][i] + 0.5, '%s' % round(df["PM2.5"][i], 3), ha='center', fontsize=10)
    # plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title(u"周口市九区县截止今日{}时PM2.5累积浓度柱状图".format(hour_d), fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig('image/pci.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()



# 画柱状图
def line_picpm10(hour_d):
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
    plt.title(u"周口市九区县截止今日{}时PM10累积浓度柱状图".format(hour_d), fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig('image/pci1.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()



#
# x = ['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
# y_1 = [47, 47, 46, 46, 44, 42, 42, 42, 40, 38, 34, 29, 25, 21, 20, 21, 22, 24, 31, 42, 48, 51, 49, 49]
# y_2 = [27, 24, 23, 20, 17, 17, 16, 13, 16, 24, 40, 58, 72, 87, 94, 96, 98, 92, 80, 59, 40, 33, 31, 28]
# line_bar(x,y_1,y_2,"NO2","O3","时间：h","浓度：μg/m3")