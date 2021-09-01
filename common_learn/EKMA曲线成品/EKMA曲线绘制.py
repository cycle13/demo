#导入模块
import data_p
# import data_plot
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as col
import matplotlib.cm as cm
import datetime
from scipy.ndimage.filters import gaussian_filter
plt.rcParams['font.sans-serif'] = ['SimHei']


day1 = datetime.datetime(2021,10,22)
day2 = datetime.datetime.now()
d = (day1-day2).days
if d < 0:
    print('授权时间已过，授权无效！')
    exit()
print('授权还有{}天有效期！'.format(d))
name = 'isopleth'
data2 = data_p.data_p(name)
path = 'data/'+name+'.txt'
data = open(path,'r').read()
print('正在处理数据！')
data = data.replace('<P>','')
data = data.replace('</BODY>','')
data = data.replace('</HTML>','')
data = data.replace('\n','')
data1 = data.split(' ')
data1 = filter(None,data1)
data = []
for j in data1:
    print(j)
    data.append(float(j))
voc = []
nox = []
o3 = []
for i in range(int((len(data)/4))):
    voc.append(data[(0+4*i)])
    nox.append(data[(1 + 4 * i)])
    o3.append(data[(2 + 4 * i)])

data = pd.DataFrame({'voc':voc,'nox': nox,'o3': o3})
X=[]
Y=[]
Z=[]
step = 11
for i in range(int(len(data['voc'])/step)):
    x=[]
    for j in range(len(data['voc'][i*step:(i+1)*step])):
        x.append(data['voc'][i*step+j])
    X.append(x)

for i in range(int(len(data['nox'])/step)):
    y=[]
    for j in range(len(data['nox'][i*step:(i+1)*step])):
        y.append(data['nox'][i*step+j])
    Y.append(y)

for i in range(int(len(data['o3'])/step)):
    z=[]
    for j in range(len(data['o3'][i*step:(i+1)*step])):
        z.append(data['o3'][i*step+j])
    Z.append(z)
print('正在对导出数据进行绘图！')
# 自定义色阶
color1 = '#00E400'  # 优
color2 = '#FFFF00'  # 良
color3 = '#FF7E00'  # 轻
color4 = '#FF0000'  # 中
cmap2 = col.LinearSegmentedColormap.from_list('own2', [color1, color2, color3,color4])
cm.register_cmap(cmap=cmap2)
# 绘制云图
sigma = 1
Z = gaussian_filter(Z, sigma)
cset = plt.contourf(X,Y,Z,20,cmap=cm.get_cmap('own2'))
# 绘制等值线
contour = plt.contour(X,Y,Z,20,colors='k')
# plt.plot([0,0.25*4], [0,0.25], '-r')
# plt.plot([0,2], [0,2/8], '-b')
# plt.plot([0,2], [0,2/15], '-g')
plt.xlabel('VOCs/ppm')
plt.ylabel('NOx/ppm')
plt.clabel(contour,fontsize=10,colors='k')
cd = plt.colorbar(cset)
cd.set_label("O3/ppm",size=10)
plt.title("EKMA曲线图",y=1.06,size=10)
# plt.text(2.0, 0, '佳华科技生态环境研究院', fontsize=30, rotation=45, color='gray', ha='right', va='bottom', alpha=0.4)
# plt.scatter(float(data2[0]),float(data2[1]),color = 'black', s=5)
plt.savefig('pic/EKMA曲线.png',dpi=600)
plt.show()
