import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import colors
from matplotlib.pylab import savefig
import pandas as pd


cmap = colors.ListedColormap(['#00E400', '#FFFF00','#FF7E00','#FF0000','#99004C','#7E0023'])
bounds=[0,50,100,150,200,300,500]
norm = colors.BoundaryNorm(bounds, cmap.N)
data = pd.read_excel("data/t.xlsx",header=None)
data.index = [16,17,18,19,20,21,22,23,24,25,26]
data.columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
sns_plot=sns.heatmap(data, cmap=cmap, norm=norm, linecolor='k', linewidths = 0.1, annot=True,fmt='.20g',annot_kws={'size':8,'weight':'bold', 'color':'blue'}, cbar=False)

u = pd.read_excel("data/u.xlsx",header=None)
v = pd.read_excel("data/v.xlsx",header=None)

x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
y = np.array([1,2,3,4,5,6,7,8,9,10,11])
x, y =np.meshgrid(x, y)
plt.quiver(x + 0.5, y - 0.5, u, v, scale = 200, headwidth = 2, width = 0.003)

plt.rcParams['font.sans-serif']=['SimHei']#设置中文字体
plt.rcParams['axes.unicode_minus'] = False#设置识别
plt.title('风速风向及空气质量等级图',fontsize=20) #设置标题
plt.xlabel('Hour',fontsize=15)#设置x，y轴的标签
plt.ylabel('Date(Feb)',fontsize=15)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5,rotation=360)

sns_plot.tick_params(labelsize=10, direction='in')
cb=sns_plot.figure.colorbar(sns_plot.collections[0]) #显示colorbar
cb.ax.tick_params(labelsize=10) #设置colorbar刻度字体大小。
savefig('picture/county_image.png')
plt.show()