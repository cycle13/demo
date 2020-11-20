import wanbaisend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:00','06:00','12:00','14:00','16:00','18:00','22:00']
    time_list1 = ['08:30']
    time_list2 = ['08:32']
    time_list3 = ['10:30']
    time_list4 = ['20:30']
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            wanbaisend.wanbaicg()
        elif now_time in time_list1:
            print(now_time)
            wanbaisend.wanbairb()
        elif now_time in time_list2:
            print(now_time)
            wanbaisend.wanbaistr()
        elif now_time in time_list3:
            print(now_time)
            wanbaisend.wanbaibz()
        elif now_time in time_list4:
            print(now_time)
            wanbaisend.wanbaiadd()
        time.sleep(60)