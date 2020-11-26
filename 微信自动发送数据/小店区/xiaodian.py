import xiaodiansend
import time
import datetime


if __name__ == '__main__':
    time_list = ['10:00']
    time_list1 = ['00:25','01:25','02:25','03:25','04:25','05:25','06:25','07:25','08:25','09:25','10:25','11:25','12:25','13:25','14:25','15:25','16:25','17:25','18:25','19:25','20:25','21:25','22:25','23:25']
    name = input('请输入要发送的微信名称：')
    while True:
        try:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now_time in time_list1:
                print(now_time)
                xiaodiansend.hoursend(name)
            # if now_time in time_list:
            #     print(now_time)
            #     xiaodiansend.daily()
            # elif now_time in time_list1:
            #     print(now_time)
            #     xiaodiansend.hoursend(name)
            time.sleep(60)
        except:
            pass