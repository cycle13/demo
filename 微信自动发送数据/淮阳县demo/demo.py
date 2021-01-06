import requests
import json
import win32api
import win32gui
import time
import win32con
import win32clipboard as w
from datetime import datetime
import datetime as datatime



session = requests.Session()
huai_url = 'http://1.192.88.18:8007/api/v1/ChinaAir/get24History/411626'
tai_url = 'http://1.192.88.18:8007/api/v1/ChinaAir/get24History/411627'

headers = {
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/N2G48H)'
}

def FindWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    print("找到群聊窗口：%x" % win)
    if win != 0:
        win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        win32gui.ShowWindow(win, win32con.SW_SHOW)
        win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 100, 100, 300, 300, win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(win)  # 获取控制
        time.sleep(1)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % chatroom)
        exit()

def CloseWindow(chatroom):
    win = win32gui.FindWindow(None, chatroom)
    #print("找到关闭窗口：%x" % win)
    time.sleep(3)
    win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)

def ctrlV():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

def altS():
    win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
    win32api.keybd_event(83, 0, 0, 0)  # s键位码
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)

def send():
    ctrlV()
    altS()

def qi(url):
    response = session.get(url=url,headers=headers,timeout=10).text
    return response

def huaiyang():
    data_time1 = (datetime.now() + datatime.timedelta(hours=-1)).strftime("%Y-%m-%dT%H")+':00:00'
    data_time2 = (datetime.now() + datatime.timedelta(hours=-2)).strftime("%Y-%m-%dT%H")+':00:00'
    print(data_time1)
    l = qi(huai_url)
    data = json.loads(l)
    PM1 = []
    PM2 = []
    for data_time in data:
        if data_time['update_time'] == data_time1:
            PM251 = data_time['pm25']
            PM101 = data_time['pm10']
            PM1.append(PM251)
            PM1.append(PM101)
        if data_time['update_time'] == data_time2:
            PM252 = data_time['pm25']
            PM102 = data_time['pm10']
            PM2.append(PM252)
            PM2.append(PM102)

    return PM1,PM2

def taikang():
    data_time1 = (datetime.now() + datatime.timedelta(hours=-1)).strftime("%Y-%m-%dT%H")+':00:00'
    data_time2 = (datetime.now() + datatime.timedelta(hours=-2)).strftime("%Y-%m-%dT%H")+':00:00'
    print(data_time1)
    l = qi(tai_url)
    data = json.loads(l)
    PM1 = []
    PM2 = []
    for data_time in data:
        if data_time['update_time'] == data_time1:
            PM251 = data_time['pm25']
            PM101 = data_time['pm10']
            PM1.append(PM251)
            PM1.append(PM101)
        if data_time['update_time'] == data_time2:
            PM252 = data_time['pm25']
            PM102 = data_time['pm10']
            PM2.append(PM252)
            PM2.append(PM102)

    return PM1,PM2

# 复制文本到剪切板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_text(name,l):
    FindWindow(name)
    setText(l)
    send()
    CloseWindow(name)


def sendd_text(name):
    l = ''
    huai = huaiyang()
    time.sleep(1)
    tai = taikang()
    time.sleep(1)
    print(huai,tai)
    if ((int(huai[0][0])-int(huai[1][0]))/int(huai[1][0]))>=0.3:
        l+='淮阳县PM2.5上升较快'
    if ((int(huai[0][1]) - int(huai[1][1])) / int(huai[1][1])) >= 0.3:
        l += '淮阳县PM10上升较快'
    if (int(huai[0][0])-int(tai[0][0])) >= 10:
        l+='淮阳县跟太康县PM2.5差距较大'
    if (int(huai[0][1])-int(tai[0][1])) >= 10:
        l+='淮阳县跟太康县PM10差距较大'
    if len(l) > 0:
        l = '@所有人 '+l
    send_text(name,l)


# sendd_text('王彦军')