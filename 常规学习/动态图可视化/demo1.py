import pandas as pd
import matplotlib as mpl
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
from datetime import datetime
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('axes',axisbelow=True)
mpl.rcParams['animation.embed_limit'] = 2**128


df = pd.read_csv('data/BTC.csv')
# for d in df['date']:
#     df['date'] = (datetime.strptime(d, '%Y/%m/%d').date())




def draw_areachart(Num_Date):
    Span_Date=180
    ax.clear()
    if Num_Date<Span_Date:
        df_temp=df.loc[0:Num_Date,:]
        df_span=df.loc[0:Span_Date,:]
        colors = cm.Spectral_r(df_span.price.values / float(max(df_span.price.values)))
        plt.bar(df_temp.date.values,df_temp.price.values,color=colors,width=1.5,align="center",zorder=1)
        plt.plot(df_temp.date, df_temp.price, color='k',zorder=2)
        plt.scatter(df_temp.date.values[-1], df_temp.price.values[-1], color='white',s=150,edgecolor ='k',linewidth=2,zorder=3)
        plt.text(df_temp.date.values[-1], df_temp.price.values[-1]*1.18,s=np.round(df_temp.price.values[-1],1),
size=10,ha='center', va='top')
        plt.ylim(0, df_span.price.max()*1.68)
        plt.xlim(df_span.date.values[0], df_span.date.values[-1])
        plt.xticks(ticks=df_span.date.values[0:Span_Date+1:30],labels=df_span.date.values[0:Span_Date+1:30],rotation=0,fontsize=9)
    else:
        df_temp=df.loc[Num_Date-Span_Date:Num_Date,:]
        colors = cm.Spectral_r(df_temp.price / float(max(df_temp.price)))
        plt.bar(df_temp.date.values[:-2],df_temp.price.values[:-2],color=colors[:-2],width=1.5,align="center",zorder=1)
        plt.plot(df_temp.date[:-2], df_temp.price[:-2], color='k',zorder=2)
        plt.scatter(df_temp.date.values[-4], df_temp.price.values[-4], color='white',s=150,edgecolor ='k',linewidth=2,zorder=3)
        plt.text(df_temp.date.values[-1], df_temp.price.values[-1]*1.18,s=np.round(df_temp.price.values[-1],1),
size=10,ha='center', va='top')
        plt.ylim(0, df_temp.price.max()*1.68)
        plt.xlim(df_temp.date.values[0], df_temp.date.values[-1])
        plt.xticks(ticks=df_temp.date.values[0:Span_Date+1:30],labels=df_temp.date.values[0:Span_Date+1:30],rotation=0,fontsize=9)

    plt.margins(x=0.2)
    ax.spines['top'].set_color('none')  # 设置上‘脊梁’为红色
    ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['left'].set_color('none')  # 设置上‘脊梁’为无色
    plt.grid(axis="y",c=(217/256,217/256,217/256),linewidth=1)         #设置网格线
    plt.text(0.01, 0.95,"BTC平均价格($)",transform=ax.transAxes, size=10, weight='light', ha='left')
    ax.text(-0.07, 1.03, '2013年到2021年的比特币BTC价格变化情况',transform=ax.transAxes, size=17, weight='light', ha='left')


# fig, ax = plt.subplots(figsize=(6,4), dpi=100)
# plt.subplots_adjust(top=1,bottom=0.1,left=0.1,right=0.9,hspace=0,wspace=0)
# draw_areachart(350)
# plt.show()





fig, ax = plt.subplots(figsize=(6,4), dpi=100)
plt.subplots_adjust(left=0.12, right=0.98, top=0.85, bottom=0.1,hspace=0,wspace=0)
animator = animation.FuncAnimation(fig, draw_areachart, frames=np.arange(0,df.shape[0],1),interval=100)
HTML(animator.to_jshtml())

