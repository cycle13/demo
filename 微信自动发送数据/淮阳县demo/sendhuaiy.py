import time
import datetime
import demo
import demo2


if __name__ == '__main__':
    f = open('time_file/datafile.txt')
    print('时间文件获取成功')
    time_list = f.read()
    name = input('请输入要发送的微信名称：')
    print('微信名称获取成功')
    while True:
        try:
            now_time = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now_time in time_list:
                print(now_time)
                demo2.send_excel_pic(name)
                time.sleep(2)
                demo.sendd_text(name)
            time.sleep(60)
        except:
            demo2.send_text(name,'数据异常')
            time.sleep(60)