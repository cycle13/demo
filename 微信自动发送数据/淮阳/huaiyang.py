import huaiyangsend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:10','01:10','02:10','03:10','04:10','05:10','06:10','07:10','08:10','09:10','10:10','11:10','12:10','13:10','14:10','15:10','16:10','17:10','18:10','19:10','20:10','21:10','22:10','23:10']
    # time_list = []
    time_list1 = ['00:15','01:15','02:15','03:15','04:15','05:15','06:15','07:15','08:15','09:15','10:15','11:15','12:15','13:15','14:15','15:15','16:15','17:15','18:15','19:15','20:15','21:15','22:15','23:15']
    # time_list1 = []
    time_list2 = ['00:47', '01:47', '02:47', '03:47', '04:47', '05:47', '06:47', '07:47', '08:47', '09:47', '10:47','11:47', '12:47', '13:47', '14:47', '15:47', '16:47', '17:47', '18:47', '19:47', '20:47', '21:47','22:47', '23:47']
    time_list3 = ['07:00']
    time_list4 = ['12:00']
    time_list5 = ['09:00','19:30']
    name = input('请输入要发送的微信名称：')
    while True:
        try:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now_time in time_list:
                print(now_time)
                huaiyangsend.hoursend(name)
            elif now_time in time_list1:
                print(now_time)
                huaiyangsend.hourleijisend(name)
            elif now_time in time_list3:
                print(now_time)
                huaiyangsend.yearleijisend(name)
            elif now_time in time_list2:
                print(now_time)
                huaiyangsend.save_data()
            elif now_time in time_list4:
                print(now_time)
                huaiyangsend.pre_hn_air(name)
            elif now_time in time_list5:
                print(now_time)
                huaiyangsend.pre_county_air(name)
        except:
            pass
        time.sleep(60)