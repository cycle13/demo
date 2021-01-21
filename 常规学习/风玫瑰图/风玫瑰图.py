import os
import pandas as pd
from matplotlib.font_manager import FontProperties
from matplotlib.pylab import savefig
import windrose
# 重新升级matplotlib到3.0.2版本就行了
# 读取数据
pm25W = pd.read_excel('weatherAll1.xlsx')
#加载字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)


def ShowAndSave_WindroseAxes(pm25W0,iname):
    ax = windrose.WindroseAxes.from_ax()
    ax.bar(pm25W0.wind_x,
           pm25W0.wind_s,
           nsector=16, # 散片个数
           bins=[0,0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1], # 分段列表
           #bins=1, # 分段个数
           normed=True, opening=1, edgecolor='white')
    ax.set_legend() #图例
    #ax.legend(loc=(-0.2,0.9)) #图例位置
    ax.legend(loc=(-0.12,0.8)) #图例位置
    ax.set_title(iname,fontproperties=font) #标题
    savefig('./' + iname + '.png')

pm25W1 = pm25W[pm25W.name == '桃园2019年春节假期']
ShowAndSave_WindroseAxes(pm25W1,'桃园2019年春节假期')