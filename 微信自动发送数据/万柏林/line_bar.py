import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib



def line_bar(x,y_1,y_2,data1,data2,data3,data4):
    # 创建画布
    plt.figure()

    '''绘制第一条数据线
    1、节点为圆圈
    2、线颜色为红色
    3、标签名字为y1-data
    '''
    plt.plot(x, y_1, marker='o', color='r', label=data1)

    '''绘制第二条数据线
    1、节点为五角星
    2、线颜色为蓝色
    3、标签名字为y2-data
    '''
    plt.plot(x, y_2, marker='*', color='b', label=data2)

    # 标注值
    for i in range(len(y_1)):
        plt.text(x[i], y_1[i] + 0.5, '%s' % round(y_1[i], 3), ha='center', fontsize=10)
    for i in range(len(y_2)):
        plt.text(x[i], y_2[i] - 1, '%s' % round(y_2[i], 3), ha='center', fontsize=10, va='bottom')
    plt.legend()

    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title(u"NO2与O3关系图", fontproperties=font1)
    # 横坐标名称
    plt.xlabel(data3)

    # 纵坐标名称
    plt.ylabel(data4)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 保存图片到本地
    plt.savefig('image5/pci.png')
    plt.ylim(0, 20)
    plt.grid(True)
    matplotlib.use('Agg')
    # 显示图片
    plt.show()



x = ['00','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
y_1 = [47, 47, 46, 46, 44, 42, 42, 42, 40, 38, 34, 29, 25, 21, 20, 21, 22, 24, 31, 42, 48, 51, 49, 49]
y_2 = [27, 24, 23, 20, 17, 17, 16, 13, 16, 24, 40, 58, 72, 87, 94, 96, 98, 92, 80, 59, 40, 33, 31, 28]
line_bar(x,y_1,y_2,"NO2","O3","时间：h","浓度：μg/m3")