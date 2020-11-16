import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import pandas as pd


def line_bar(x,y1,y2,data1,data3,data4,image_file,name):
    # 创建画布
    plt.figure(figsize=(6, 5))

    '''绘制第一条数据线
    1、节点为圆圈
    2、线颜色为红色
    3、标签名字为y1-data
    '''
    # plt.tight_layout()
    '''绘制第二条数据线
    1、节点为五角星
    2、线颜色为蓝色
    3、标签名字为y2-data
    '''
    plt.plot(x, y1, marker='*', color='r',label = 'PM2.5')
    plt.plot(x, y2, marker='x', color='y',label = 'PM10')
    # 标注值
    for i in range(len(y1)):
        plt.text(x[i], y1[i] + 0.5, '%s' % round(y1[i], 3), ha='center', fontsize=10)
    for i in range(len(y2)):
        plt.text(x[i], y2[i] - 1, '%s' % round(y2[i], 3), ha='center', fontsize=10, va='bottom')
    # for i in range(len(y3)):
    #     plt.text(x[i], y3[i] - 1, '%s' % round(y3[i], 3), ha='center', fontsize=10, va='bottom')
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    plt.title(data1, fontproperties=font1)
    # 横坐标名称
    # 设置横坐标标注转换角度
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

# 画柱状图
def line_pic(excel_filenew_dir1,hour_d,image_file):
    df = pd.read_excel(excel_filenew_dir1)
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
    plt.title(hour_d, fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig(image_file+'/pci.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()



# 画柱状图
def line_picpm10(excel_filenew_dir2,hour_d,image_file):
    df = pd.read_excel(excel_filenew_dir2)
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
    plt.title(hour_d, fontproperties=font1)
    # 横坐标名称
    plt.xlabel("周口市九区县")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    # 保存图片到本地
    plt.savefig(image_file+'/pci1.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()
