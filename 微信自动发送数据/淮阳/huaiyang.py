import huaiyangsend
import time
import datetime


if __name__ == '__main__':
    time_list = ['00:30','01:30','02:30','03:30','04:30','05:30','06:30','07:30','08:30','09:30','10:30','11:30','12:30','13:30','14:30','15:30','16:30','17:30','18:30','19:30','20:30','21:30','22:30','23:30']
    # time_list = []
    time_list1 = ['00:35','01:35','02:35','03:35','04:35','05:35','06:35','07:35','08:35','09:35','10:35','11:35','12:35','13:35','14:35','15:35','16:35','17:35','18:35','19:35','20:35','21:35','22:35','23:35']
    # time_list1 = []
    time_list2 = ['00:20', '01:20', '02:20', '03:20', '04:20', '05:20', '06:20', '07:20', '08:20', '09:20', '10:20','11:20', '12:20', '13:20', '14:20', '15:20', '16:20', '17:20', '18:20', '19:20', '20:20', '21:20','22:20', '23:20']
    time_list3 = ['07:00']
    time_list4 = ['12:00']
    time_list5 = ['09:00','19:00']
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