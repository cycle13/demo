import xinghualingsend
import time
import datetime


if __name__ == '__main__':
    # time_list = ['08:00','12:00','16:00','20:00']
    # time_list1 = ['16:00','20:00']
    f = open('time_file/datafile.txt')
    print('时间文件获取成功')
    time_list = f.read()
    name = input('请输入要发送的微信名称：')
    print('微信名称获取成功')
    while True:
        now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
        if now_time in time_list:
            print(now_time)
            xinghualingsend.hoursend(name)
        # elif now_time in time_list1:
        #     print(now_time)
        #     xinghualingsend.hourlastsend()
        time.sleep(60)