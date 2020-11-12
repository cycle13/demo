import yingzesend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:00','06:00','08:00','12:00','14:00','16:00','18:00','20:00','22:00']
    time_list1 = ['10:30','16:30','20:30']
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            yingzesend.hoursend()
        elif now_time in time_list1:
            print(now_time)
            yingzesend.hourjc()
        time.sleep(60)