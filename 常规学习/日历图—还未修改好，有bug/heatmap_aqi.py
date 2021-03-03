import glob
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import calmap

from matplotlib import cm, colors
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib as mpl


## 定义可视化方法
def calendar_heatmap(df, title):
    # 定义颜色
    color_list = ['#009966', '#FFDE33', '#FF9A32', '#CC0033', '#660099']
    levels = [0, 50, 100, 150, 200, 300]

    cmap = colors.ListedColormap(color_list)  
    norm = colors.BoundaryNorm(levels, cmap)
    
    # 绘图
    fig, ax = plt.subplots(figsize=(18, 9))

    calmap.yearplot(
        df,              
        vmin=0, 
        vmax=300,                  
        cmap=cmap, 
        norm=norm, 
        how=None, 
        year=2020,
    )

    cbar_ax  = fig.add_axes([0.94, 0.4, 0.015, 0.2])
    cb  = mpl.colorbar.ColorbarBase(
        cbar_ax, 
        cmap=cmap, 
        ticks=levels,              
        norm=norm, 
        orientation='vertical',               
        extend='neither', 
        extendrect=True,                         
        extendfrac=0.15
    )
    
    # 色标
    cb.set_ticks([0, 50, 100, 150, 200, 300])
    cb.ax.yaxis.set_tick_params(length=0.01)
    ax.set_ylabel('2020', fontdict=dict(fontsize=25, color='grey'))
    
    # 标题
    ax.set_title(f'AQI of {title}', fontweight = 'bold', fontsize = 25)
    
    # 存图
    plt.savefig(f'{title}_calendar_heatmap.png')

## 读取数据
df = pd.read_csv('beijing_2020.csv', index_col=0, header=[0,1], parse_dates=True)['AQI']

cp = df.resample('1d').mean().round(2)['昌平']
calendar_heatmap(cp, 'Changping')

dx = df.resample('1d').mean().round(2)['大兴']
calendar_heatmap(dx, 'DaXing')