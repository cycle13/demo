import wanbaisend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:25','06:25','12:25','14:25','16:25','18:25','22:25']
    time_list1 = ['08:30']
    time_list2 = ['08:32']
    time_list3 = ['10:30']
    time_list4 = ['20:30']
    name = input('请输入要发送的微信名称：')
    while True:
        try:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now_time in time_list:
                print(now_time)
                wanbaisend.wanbaicg(name)
            # elif now_time in time_list1:
            #     print(now_time)
            #     wanbaisend.wanbairb()
            # elif now_time in time_list2:
            #     print(now_time)
            #     wanbaisend.wanbaistr()
            # elif now_time in time_list3:
            #     print(now_time)
            #     wanbaisend.wanbaibz()
            # elif now_time in time_list4:
            #     print(now_time)
            #     wanbaisend.wanbaiadd()
            time.sleep(60)
        except:
            pass