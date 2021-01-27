import datetime
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir


# 设置下载时间段（这里是UTC时刻)
start = datetime.datetime(2019,12,30,0)
end = datetime.datetime(2019,12,31,0)


datelist = []
while start<=end:
    datelist.append(start)
    start+=datetime.timedelta(hours=12)

# 选择下载站点
stationlist = ['54511']


# 批量下载
for station in stationlist:
    for date in datelist:
        try:
            df = WyomingUpperAir.request_data(date,station)
            df.to_csv('data/'+station+'_'+date.strftime('%Y%m%d%H')+'.csv',index=False)
            print(f'{date.strftime("%Y%m%d_%H")}下载成功')
        except Exception as e:
            print(f'{date.strftime("%Y%m%d_%H")}下载失败：{e}')
            pass



