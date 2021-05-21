import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['figure.dpi'] = 600
file = r'all_data.xls'
data = pd.read_excel(file, usecols=['DATE', 'WD', 'WS', 'PM2.5'], index_col=0)
data['WD'] = np.radians(data['WD'])
v = data['WS']
speed = np.linspace(v.min(), v.max(), endpoint=True, num=16)
deg = np.linspace(0, 2*np.pi, endpoint=True, num=32)
def maker(s, sequence):
     for i, val in enumerate(sequence):
        if s <= sequence[i+1]:
            return val
d = data['WD']
data['WS'] = v.apply(maker, sequence=speed)
data['WD'] = d.apply(maker, sequence=deg)
data.head()
data['PM2.5'] = data['PM2.5'].astype(float)
dt = data.pivot_table(values='PM2.5', index='WS', columns='WD', aggfunc=np.mean)
dt.fillna(0, inplace=True)
dt = dt.reindex(index=speed, columns=deg, fill_value=0)
dt.head(6)
theta, r = np.meshgrid(deg, speed)
ax = plt.subplot(projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction('clockwise')
# 自定义cmap颜色
color1 = '#00E400'  # 优
color2 = '#FFFF00'  # 良
color3 = '#FF7E00'  # 轻
color4 = '#FF0000'  # 中
color5 = '#99004C'  # 重
color6 = '#7E0023'  # 严重
cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3,color4, color5, color6])
cm.register_cmap(cmap=cmap2)
levels = np.array([0.00000000001,35,75,115,150,250,350])

pos = ax.contourf(theta, r, dt.to_numpy(), cmap=cm.get_cmap('own2'),levels=levels)
cb = plt.colorbar(pos, ax=ax,pad=0.1)
# 方位中文英文配置
# ax.set_xticklabels(['北','东北','东','东南','南','西南','西','西北'],fontdict={'family':'SimHei','size':15,'color':'red'})
ax.set_xticklabels(['N','NE','E','SE','S','SW','W','NW'],fontdict={'weight':'bold','size':12,'color':'black'})
cb.set_label(r"PM2.5 $\rm \mu g \cdot m^{-3}$",size=8)
cb.ax.tick_params(labelsize=8)
plt.title("PM2.5浓度分布图",y=1.06,size=10)
plt.savefig('plot2.png',dpi=600)
plt.show()# show the graph on screen