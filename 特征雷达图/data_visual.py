import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
import matplotlib


def plot_radar(newfile_dir,now_time,name):
    data = pd.read_excel(newfile_dir)
    kinds = data.iloc[:, 0]
    labels = data.iloc[:, 1:].columns
    centers = pd.concat([data.iloc[:, 1:], data.iloc[:, 1]], axis=1)
    centers = np.array(centers)
    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # 设置坐标为极坐标
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 画若干个五边形
    floor = np.floor(centers.min())  # 大于最小值的最大整数
    ceil = np.ceil(centers.max())  # 小于最大值的最小整数
    for i in np.arange(floor, ceil + 0.5, 0.5):
        ax.plot(angles, [i] * (n + 1), '--', lw=0.5, color='black')
    for i in range(n):
        ax.plot([angles[i], angles[i]], [floor, ceil], '--', lw=0.5, color='black')
    for i in range(len(kinds)):
        ax.plot(angles, centers[i], lw=2, label=kinds[i])
        # ax.fill(angles, centers[i])
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
    ax.set_thetagrids(angles * 180 / np.pi, ['SO2', 'PM10', 'PM2.5', 'CO', 'NO2','SO2'], FontProperties=font)  # 设置显示的角度，将弧度转换为角度
    plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0.8))  # 设置图例的位置，在画布外
    ax.set_theta_zero_location('N')  # 设置极坐标的起点（即0°）在正北方向，即相当于坐标轴逆时针旋转90°
    ax.spines['polar'].set_visible(False)  # 不显示极坐标最外圈的圆
    ax.grid(False)  # 不显示默认的分割线
    # ax.set_yticks([])  # 不显示坐标间隔
    plt.tight_layout()
    plt.title(now_time +'：' +name,x=0,y=0.9,fontproperties=font,fontsize=18,color = 'r')
    plt.savefig("image_file" + '/' + now_time + '.png')
    plt.ylim(0, 20)
    plt.grid(True)
    matplotlib.use('Agg')


def plot_radar_time(newfile_dir,now_time,name):
    data = pd.read_excel(newfile_dir)
    kinds = data.iloc[:, 0]
    labels = data.iloc[:, 1:].columns
    centers = pd.concat([data.iloc[:, 1:], data.iloc[:, 1]], axis=1)
    centers = np.array(centers)
    n = len(labels)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # 设置坐标为极坐标
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 画若干个五边形
    floor = np.floor(centers.min())  # 大于最小值的最大整数
    ceil = np.ceil(centers.max())  # 小于最大值的最小整数
    for i in np.arange(floor, ceil + 0.5, 0.5):
        ax.plot(angles, [i] * (n + 1), '--', lw=0.5, color='black')
    for i in range(n):
        ax.plot([angles[i], angles[i]], [floor, ceil], '--', lw=0.5, color='black')
    for i in range(len(kinds)):
        ax.plot(angles, centers[i], lw=2, label=kinds[i])
        # ax.fill(angles, centers[i])
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
    ax.set_thetagrids(angles * 180 / np.pi, ['SO2', 'PM10', 'PM2.5', 'CO', 'NO2','SO2'], FontProperties=font)  # 设置显示的角度，将弧度转换为角度
    plt.legend(loc='lower right', bbox_to_anchor=(1.2, 0.8))  # 设置图例的位置，在画布外
    ax.set_theta_zero_location('N')  # 设置极坐标的起点（即0°）在正北方向，即相当于坐标轴逆时针旋转90°
    ax.spines['polar'].set_visible(False)  # 不显示极坐标最外圈的圆
    ax.grid(False)  # 不显示默认的分割线
    # ax.set_yticks([])  # 不显示坐标间隔
    plt.tight_layout()
    plt.title(name,x=0,y=0.9,fontproperties=font,fontsize=18,color = 'r')
    plt.savefig("image_file" + '/' + now_time + '.png')
    plt.ylim(0, 20)
    plt.grid(True)
    matplotlib.use('Agg')


