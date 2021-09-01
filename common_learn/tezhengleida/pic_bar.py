import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import pandas as pd



# 画柱状图
def line_pic(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i].strftime('%Y-%m-%d'), df["PM2.5"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["PM2.5"])):
        plt.text(df["时间"][i].strftime('%Y-%m-%d'), df["PM2.5"][i] + 0.5, '%s' % round(df["PM2.5"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区PM2.5浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"].astype('str'), df["时间"].astype('str'), rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/pm25.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()

def line_pic10(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["PM10"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["PM10"])):
        plt.text(df["时间"][i], df["PM10"][i] + 0.5, '%s' % round(df["PM10"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区PM10浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/pm10.png')
    matplotlib.use('Agg')

def line_picco(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["CO"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["CO"])):
        plt.text(df["时间"][i], df["CO"][i] + 0.5, '%s' % round(df["CO"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区CO浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度mg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/CO.png')
    matplotlib.use('Agg')


def line_picso2(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["SO2"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["SO2"])):
        plt.text(df["时间"][i], df["SO2"][i] + 0.5, '%s' % round(df["SO2"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区SO2浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/SO2.png')
    matplotlib.use('Agg')


def line_picno2(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["NO2"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["NO2"])):
        plt.text(df["时间"][i], df["NO2"][i] + 0.5, '%s' % round(df["NO2"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区NO2浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/NO2.png')
    matplotlib.use('Agg')

def line_pico3(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["O3"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["O3"])):
        plt.text(df["时间"][i], df["O3"][i] + 0.5, '%s' % round(df["O3"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区O3浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/O3.png')
    matplotlib.use('Agg')



def line_pic_hour(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i].strftime('%Y-%m-%d %H:%M:%S'), df["PM2.5"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["PM2.5"])):
        plt.text(df["时间"][i].strftime('%Y-%m-%d %H:%M:%S'), df["PM2.5"][i] + 0.5, '%s' % round(df["PM2.5"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区PM2.5浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")

    plt.xticks(df["时间"].astype('str'), df["时间"].astype('str'), rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/pm25.png')
    matplotlib.use('Agg')