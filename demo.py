import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


def plot_radar(data):
    N = 4  # 属性个数
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)  # 设置雷达图的角度，用于平分切开一个圆面
    angles = np.concatenate((angles, [angles[0]]))  # 为了使雷达图一圈封闭起来
    fig = plt.figure(figsize=(12, 12))  # 设置画布大小
    ax = fig.add_subplot(111, polar=True)  # 这里一定要设置为极坐标格式
    sam = ['r-', 'm-', 'g-', 'b-', 'y-', 'k-', 'w-', 'c-']  # 样式
    lab = []  # 图例标签名
    for i in range(len(data)):
        values = data[i]
        feature = ['Asm', 'Con', 'Ent', 'Idm']  # 设置各指标名称

        # 为了使雷达图一圈封闭起来，需要下面的步骤
        values = np.concatenate((values, [values[0]]))
        ax.plot(angles, values, sam[i], linewidth=2)  # 绘制折线图
        #        ax.fill(angles, values, alpha=0.5) # 填充颜色
        ax.set_thetagrids(angles * 180 / np.pi, feature, font_properties=my_font)  # 添加每个特征的标签
        ax.set_ylim(auto=True)  # 设置雷达图的范围
        plt.title('GLCM灰度特征图', font_properties=my_font)  # 添加标题
        ax.grid(True)  # 添加网格线
        lab.append('邻域块' + str(i + 1))
    plt.savefig("./GLCM灰度特征图.jpg")  # 保存图片到本地
    plt.show()