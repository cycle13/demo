import hechuansend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:00','23:00']
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            hechuansend.hoursend()
        time.sleep(60)