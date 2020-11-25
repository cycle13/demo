import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import pandas as pd



# 画柱状图
def line_pic(excel_filenew_dir1,image_file,color):
    df = pd.read_excel(excel_filenew_dir1)
    plt.figure()
    for i in range(len(df["时间"])):
        plt.bar(df["时间"][i], df["PM2.5"][i], fc=color[i][1], edgecolor='black', linewidth=2,label=color[i][0])

    for i in range(len(df["PM2.5"])):
        plt.text(df["时间"][i], df["PM2.5"][i] + 0.5, '%s' % round(df["PM2.5"][i], 3), ha='center', fontsize=10)
    plt.legend()
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title('淮阳区PM2.5浓度图', fontproperties=font1)
    # 横坐标名称
    plt.xlabel("时间")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 纵坐标名称
    plt.ylabel("浓度μg/m3")
    plt.xticks(df["时间"], df["时间"], rotation=60)
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig(image_file+'/pci.png')
    matplotlib.use('Agg')
    # 显示图片
    # plt.show()