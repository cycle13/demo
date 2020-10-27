import requests
import pandas as pd
import json
import xlwt
import time
import itchat
import win32api, win32gui, win32con
import win32clipboard as clipboard
from apscheduler.schedulers.blocking import BlockingScheduler



session = requests.Session()
first_url_day = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/dayAqi2018_county'
first_url_month = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county'
first_url_year = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/airreport2018_county '
url_list = 'http://1.192.88.18:8115/hnAqi/v1.0/api/air/getCityStationDetail'
headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

def year(url):
    data = {
        'end':'2020-10-22',
        'sort':'asc',
        'start':'2020-01-01'
    }
    response = session.post(url= url,data=data,headers = headers).text
    print(response)
    return response

def month(url):
    data = {
        'sort':'asc',
        'month':'2020-07'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response

def day(url):
    data = {
        'sort':'asc',
        'time':'2020-09-27'
    }
    response = session.post(url= url,data=data,headers = headers).text
    return response


def real(url):
    response = session.get(url= url_list,headers = headers).text
    l = []
    data = json.loads(response)['detail']
    for k in data:
        if k['CITY'] in ['沈丘县', '商水县', '西华县', '扶沟县', '郸城县', '淮阳县', '太康县', '鹿邑县', '项城市', '港区', ]:
            return (k['CITY'], k['CO'], k['O3'], k['SO2'], k['NO2'], k['PM10'], k['PM25'], k['AQI'])
            # l.append([k['CITY'], k['CO'], k['O3'], k['SO2'], k['NO2'], k['PM10'], k['PM25'], k['AQI']])

        # n+=1

###############################
#  微信发送
###############################
def send_m(win):
    # 以下为“CTRL+V”组合键,回车发送，（方法一）
    win32api.keybd_event(17, 0, 0, 0)  # 有效，按下CTRL
    time.sleep(1)  # 需要延时
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 86, 0)  # V
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开CTRL
    time.sleep(1)  # 缓冲时间
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 回车发送
    return
def txt_ctrl_v(txt_str):
    # 定义文本信息,将信息缓存入剪贴板
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, txt_str)
    clipboard.CloseClipboard()
    return
# def day_english():
#     # 获取金山词霸每日一句
#     url = 'http://open.iciba.com/dsapi'
#     r = requests.get(url)
#     content = r.json()['content']
#     note = r.json()['note']
#     print(content + note)
#     return content + note
def get_window(className, titleName):
    title_name = className  # 单独打开，好友名称
    win = win32gui.FindWindow(className, titleName)
    # 窗体前端显示
    # win32gui.SetForegroundWindow(win)
    # 使窗体最大化
    win32gui.ShowWindow(win, win32con.SW_MAXIMIZE)
    win = win32gui.FindWindow(className, titleName)
    print("找到句柄：%x" % win)
    if win != 0:
        left, top, right, bottom = win32gui.GetWindowRect(win)
        print(left, top, right, bottom)  # 最小化为负数
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(0.5)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)
    return win
#######################发送过程=================
def sendTaskLog():
    # 查找微信小窗口
    # win = get_window('ChatWnd', '文件传输助手')
    win = get_window('WeChatMainWndForPC', '环保小子')
    # 读取文本
    file = open(r'E:\tasklog.txt', mode='r', encoding='UTF-8')
    str = file.read()
    print(str)
    txt_ctrl_v(str)
    send_m(win)
scheduler = BlockingScheduler()
# scheduler.add_job(sendTaskLog, 'interval', seconds=3)
# scheduler.add_job(sendTaskLog, 'cron',day_of_week='mon-fri', hour=7,minute=31,second='10',misfire_grace_time=30)
scheduler.add_job(sendTaskLog(), 'cron', day_of_week='mon-fri', hour=6, minute=55, second='10', misfire_grace_time=30)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass


# if __name__ == "__main__":
#     # itchat.auto_login(hotReload=True)
#     itchat.auto_login()
#     users = itchat.get_friends(update=True)
#     print(users)
#     # userName = users['NickName']
#     # while True:
#     #     message = real(url_list)
#     #     itchat.send (message, toUserName="环保小子")
#     #     time.sleep (3600)
#     #     # itchat.logout()




