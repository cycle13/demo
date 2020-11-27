import xiaodiansend
import time
import datetime


if __name__ == '__main__':
    time_list = ['10:00']
    f = open('time_file/datafile.txt')
    print('时间文件获取成功')
    time_list1 = f.read()
    name = input('请输入要发送的微信名称：')
    print('微信名称获取成功')
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