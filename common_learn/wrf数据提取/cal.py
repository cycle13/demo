import numpy as np
from datetime import datetime
import datetime as datatime
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import pandas as pd
import nearest_data
import sele_station_data
import data_cal
import wrf_data
import dp_temp


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
l = sele_station_data.station_lon_lat('海口')
start = '01/01/2020'
end = '01/07/2020'
my_datatime = pd.date_range(start, end)
myy_datatime = pd.date_range(start, end,freq='H')
resultt = (myy_datatime+ datatime.timedelta(hours=8)).strftime("%Y-%m-%d %H:00")
result = my_datatime.strftime('%Y-%m-%d')
station_data = []
ind = []
for date_time in result:
    layer,year,month,day = '03',date_time[0:4],date_time[5:7],date_time[8:10]
    path = 'data/wrfout_d{0}_{1}-{2}-{3}_00_00_00'.format(layer,year,month,day)
    data = wrf_data.wrf_data(path)
    for i in nearest_data.nearest_position(float(l[1]) , float(l[2]),data[1], data[2],data[0]):
        ind.append(i)
#新的
for i in resultt:
    station_data.append(data_cal.station_lp(i))
    # exit()
    # for i in range(24):
    #     if i<10:
    #         station_data.append(data_cal.station_l(year, month, day, '0'+str(i)))
    #     else:
    #         station_data.append(data_cal.station_l(year, month, day, str(i)))
    #使用全国站点数据
    # for i in range(3, 24, 6):
    #     station_data.append(data_cal.station(str(int(l[0])),year,str(int(month)),str(int(day)),str(i)))


temp = []
temp_wrf = []
dp_tem = []
dp_tem_wrf = []
press = []
press_wrf = []
U = []
U_wrf = []
V = []
V_wrf = []
for i in range(len(station_data)):
    temp.append(station_data[i][0])
    temp_wrf.append(ind[i][0])
    dp_tem.append(station_data[i][1])
    dp_tem_wrf.append(ind[i][1])
    press.append(station_data[i][2])
    press_wrf.append(ind[i][2])
    U.append(station_data[i][3])
    U_wrf.append(ind[i][3])
    V.append(station_data[i][4])
    V_wrf.append(ind[i][4])
for i in range(len(press)):
    if press[i]==-999.9:
        press[i]= None

press_wrf = dp_temp.calpress(temp_wrf,press_wrf,20)

range_time = range(len(press))
plt.figure(figsize=(20,20), dpi=100)
plt.figure(1)
ax1 = plt.subplot(411)
plt.title('监测值与预测值气象五参折线图')
plt.plot(range_time,temp, color="r",linestyle = "--",label = '监测值温度')
plt.plot(range_time,temp_wrf, color="black",linestyle = "--",label = '预测值温度')
plt.ylabel('温度：℃')
plt.legend(bbox_to_anchor = (1.01,0.55),loc=3,borderaxespad =0 )
ax2 = plt.subplot(412)
plt.plot(range_time,dp_tem,color="r",linestyle = "-",label = '监测值相对湿度')
plt.plot(range_time,dp_tem_wrf,color="black",linestyle = "-",label = '预测值相对湿度')
plt.ylabel('相对湿度：%')
# plt.plot(range_time,dp_tem,color="r",linestyle = "-",label = '监测值露点温度')
# plt.plot(range_time,dp_tem_wrf,color="black",linestyle = "-",label = '预测值露点温度')
# plt.ylabel('露点温度：℃')
plt.legend(bbox_to_anchor = (1.01,0.55),loc=3,borderaxespad =0)
ax3 = plt.subplot(413)
plt.scatter(range_time,press,color="r",linestyle = "-.",label = '监测值压强')
plt.scatter(range_time,press_wrf,color="black",linestyle = "-.",label = '预测值压强')
plt.ylabel('压强：hPa')
plt.legend(bbox_to_anchor = (1.01,0.55),loc=3,borderaxespad =0)
ax4 = plt.subplot(414)
plt.quiver(range_time, 0, U, V, color="r",scale = 80, headwidth = 2, width = 0.003,label = '监测值风速风向')
plt.quiver(range_time, 0, U_wrf, V_wrf, color="black",scale = 80, headwidth = 2, width = 0.003,label = '预测值风速风向')
range_x = []
for i in range(len(press)):
    range_x.append(0)
plt.plot(range_time,range_x,color="black")
plt.ylabel('风速风向：m/s')
plt.legend(bbox_to_anchor = (1.01,0.55),loc=3,borderaxespad =0)
plt.xticks(range_time, range_time)
plt.subplots_adjust(wspace=0,hspace=0)
plt.savefig('app.png')
plt.show()