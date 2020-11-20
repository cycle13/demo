import huaiyangsend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:32','01:32','02:32','03:32','04:32','05:32','06:32','07:32','08:32','09:32','10:32','11:32','12:32','13:32','14:32','15:32','16:32','17:32','18:32','19:32','20:32','21:32','22:32','23:32']
    time_list1 = ['00:37','01:37','02:37','03:37','04:37','05:37','06:37','07:37','08:37','09:37','10:37','11:37','12:37','13:37','14:37','15:37','16:37','17:37','18:37','19:37','20:37','21:37','22:37','23:37']
    name = input('请输入要发送的微信名称：')
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            huaiyangsend.hoursend(name)
        elif now_time in time_list1:
            print(now_time)
            huaiyangsend.hourleijisend(name)
        time.sleep(60)