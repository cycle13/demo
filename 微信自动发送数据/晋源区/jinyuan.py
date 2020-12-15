import jinyuansend
import time
import datetime


if __name__ == '__main__':
    # time_list = ['00:25','01:25','02:25','03:25','04:25','05:25','06:25','07:25','08:25','09:25','10:25','11:25','12:25','13:25','14:25','15:25','16:25','17:25','18:25','19:25','20:25','21:25','22:25','23:25']
    f = open('time_file/datafile.txt')
    print('时间文件获取成功')
    time_list = f.read()
    name1 = input('请输入要发送的微信名称1：')
    name2 = input('请输入要发送的微信名称2：')
    print('微信名称获取成功')
    try:
        while True:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now_time in time_list:
                print(now_time)
                jinyuansend.hoursend(name1,name2)
            time.sleep(60)
    except:
        pass