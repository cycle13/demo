import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data1 = pd.read_csv('data/2017年海口市日数据.csv')
data1.head()

def num(listnum,num):
    listname = []
    name = []
    bin = (float(listnum.max())-float(listnum.min()))/num
    ss = listnum.min()
    while(ss <= listnum.max()):
        name.append(round(ss,1))
        ss = ss + bin
    name.append(round(ss,1))
    for i in range(0,num):
        if i == 0:
            cmin = listnum.min()
            cmax = listnum.min()+bin
            mmum = np.where((listnum >= round(cmin,2)) & (round(cmax,2) > listnum))
            listname.append(list(mmum))
        else:
            cmin = cmax
            cmax = cmax+bin
            mmum = np.where((listnum >= round(cmin,2)) & (round(cmax,2) > listnum))
            listname.append(list(mmum))

    sl = []
    for i in list(listname):
        for j in i:
            sl.append(len(j))
    return sl,bin,listnum.min(),name



bin = 20
data =data1.sort_values(by='pm2_5')
# data = data[data['pm2_5'] > 0]
data = data['pm2_5']
print(data)

plt.style.use({'figure.figsize':(15, 10)})
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.hist(data, bins=bin, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
print(num(data,bin))
for i in range(len(num(data,bin)[0])):
    plt.text(num(data,bin)[2]+(num(data,bin)[1]/2)+(num(data,bin)[1]*i), num(data,bin)[0][i]+1, '%s' % round(num(data,bin)[0][i], 3), ha='center', fontsize=10)
# 显示纵轴标签
plt.ylabel("频数")
plt.xlabel("PM2.5浓度")
plt.xticks(num(data,bin)[3])
# 显示图标题
plt.title("2016年海口市PM2.5频数分布直方图")
plt.show()