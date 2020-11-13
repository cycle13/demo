import xinghualingsend
import time
import datetime


if __name__ == '__main__':
    time_list = ['08:00','12:00','16:00','20:00']
    time_list1 = ['16:00','20:00']
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            xinghualingsend.hoursend()
        elif now_time in time_list1:
            print(now_time)
            xinghualingsend.hourlastsend()
        time.sleep(60)