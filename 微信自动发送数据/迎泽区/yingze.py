import yingzesend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:25','06:25','08:25','12:25','14:25','16:25','18:25','20:26','22:25']
    # time_list1 = ['10:30','16:30','20:30']
    name = '王彦军'
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            yingzesend.hoursend(name)
        # elif now_time in time_list1:
        #     print(now_time)
        #     yingzesend.hourjc(name)
        time.sleep(60)