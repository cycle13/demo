import cv2
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import os
import numpy as np



now_data = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
x = []
for i in range(1,65):
    img = cv2.imread('data/'+str(i)+'.png')
    print('data/'+now_data[0:4]+'/'+now_data[5:7]+'/'+now_data[8:10]+'/'+'pm25'+'/'+str(i)+'.png')
    if img[174, 283][1] == 0:
        if img[174, 283][0]==220:
            data = 10
        if img[174, 283][0]==130:
            data = 100

    if img[174, 283][1] == 60:
        if img[174, 283][0]==255:
            data = 10
        if img[174, 283][0]==60:
            data = 85

    if img[174, 283][1] == 220:
        if img[174, 283][0]==0:
            data = 10
        if img[174, 283][0]==50:
            data = 25
    if img[174, 283][1] == 160:
        data = 10
    if img[174, 283][1] == 210:
        data = 10
    if img[174, 283][1] == 230:
        data = 15
    if img[174, 283][1] == 175:
        data = 40
    if img[174, 283][1] == 130:
        data = 60
    x.append(data)




begin = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
end = (datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y-%m-%d")
time_range= [x.strftime('%Y-%m-%d %H') for x in list(pd.date_range(start=begin+' 00', end=end+' 23',freq="180T"))]
print(len(time_range))
plt.figure(figsize=(15, 5))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(time_range, x,marker='o', color='r')
for i in range(len(x)):
    plt.text(time_range[i], x[i] + 2, '%s' % round(x[i], 3), ha='center', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.xticks(rotation=90)
plt.xlabel('时间')
plt.ylabel('PM2.5浓度:μg/m3')
plt.title('北京市未来7天PM2.5浓度预测折线图')
if not os.path.exists('line/'+now_data[0:4]+"/"+now_data[5:7]):
            os.makedirs('line/'+now_data[0:4]+"/"+now_data[5:7])
plt.savefig('line/'+now_data[0:4]+"/"+now_data[5:7]+'/'+now_data[8:10]+'pm25.png')

